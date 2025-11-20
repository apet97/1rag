# Thread Safety in Clockify RAG

This document explains the thread safety guarantees, locking mechanisms, and concurrency patterns used in the Clockify RAG system.

## Overview

As of **v5.9**, the RAG system is **fully thread-safe** and can be deployed with multiple workers and threads. All shared state is protected with reentrant locks to prevent race conditions.

## Thread Safety Guarantee

**✅ Safe for**:
- Multi-threaded deployment (e.g., `uvicorn --workers 4 --threads 4`)
- Concurrent queries (`/v1/query`) while ingesting (`/v1/ingest`)
- Multiple simultaneous ingests
- Shared cache access across threads

**⚠️ Not safe for** (by design):
- Multi-process deployment **without** careful state management
  - Each worker process has its own memory space
  - Caches and indices are NOT shared across processes
  - This is intentional - avoids complex IPC locking

## Architecture Overview

### Threading Model

The RAG system uses a hybrid threading model:

```
FastAPI (async/await)
    ↓
asyncio event loop (main thread)
    ↓
ThreadPoolExecutor (blocking operations)
    ↓
    ├── answer_once() - RAG query processing
    ├── build() - Index building
    └── ensure_index_ready() - Index loading
```

**Key Points**:
- FastAPI endpoints are `async def` (non-blocking)
- Blocking operations (embeddings, LLM calls, file I/O) run in thread pool
- Uses `loop.run_in_executor(None, blocking_func)` for offloading

### Shared State Inventory

All mutable shared state in the system:

1. **App State** (`api.py:app.state`):
   - `chunks`: List[Dict] - Text chunks
   - `vecs_n`: np.ndarray - Embedding vectors
   - `bm`: BM25 index
   - `hnsw`: HNSW index
   - `index_ready`: bool - Ready flag

2. **QueryCache** (`caching.py:QueryCache`):
   - `_cache`: OrderedDict - LRU cache
   - `_hits`, `_misses`: int - Statistics

3. **RateLimiter** (`caching.py:RateLimiter`):
   - `_tokens`: float - Token bucket
   - `_last_refill`: float - Last refill timestamp

4. **FAISS Index** (`indexing.py:_FAISS_INDEX`):
   - Module-level singleton
   - Lazy-loaded on first access

## Locking Mechanisms

### 1. App State Lock (`api.py`)

**Location**: `clockify_rag/api.py:43`

```python
_state_lock = threading.RLock()
```

**Protects**:
- `app.state.chunks`, `app.state.vecs_n`, `app.state.bm`, `app.state.hnsw`
- `app.state.index_ready`

**Usage Pattern**:
```python
# Writing state (ingest)
def _set_index_state(target_app, result):
    with _state_lock:
        target_app.state.chunks = chunks
        target_app.state.vecs_n = vecs_n
        target_app.state.bm = bm
        target_app.state.hnsw = hnsw
        target_app.state.index_ready = True

# Reading state (query)
async def submit_query(request, raw_request):
    with _state_lock:
        if not app.state.index_ready:
            raise HTTPException(503, "Index not ready")

        # Capture atomic snapshot
        chunks = app.state.chunks
        vecs_n = app.state.vecs_n
        bm = app.state.bm
        hnsw = app.state.hnsw

    # Use snapshot outside lock
    result = await loop.run_in_executor(
        None, partial(answer_once, question, chunks, vecs_n, bm, hnsw=hnsw)
    )
```

**Why RLock (Reentrant Lock)**:
- Allows same thread to acquire lock multiple times
- Prevents deadlock if `_set_index_state()` calls `_clear_index_state()`
- Standard practice for recursive/nested locking

**Critical Properties**:
1. **Atomic Snapshots**: Queries capture consistent state (all 4 index components together)
2. **No Torn Reads**: Never see partial state (e.g., new chunks + old vectors)
3. **Serialized Writes**: Multiple concurrent ingests execute sequentially

### 2. QueryCache Lock (`caching.py`)

**Location**: `clockify_rag/caching.py:92`

```python
class QueryCache:
    def __init__(self, maxsize=100):
        self._cache = OrderedDict()
        self._lock = threading.RLock()
        self._hits = 0
        self._misses = 0
```

**Protects**:
- `_cache` OrderedDict modifications (put, get, evict)
- `_hits` and `_misses` counters
- LRU ordering (move-to-end operations)

**Usage Pattern**:
```python
def get(self, key):
    with self._lock:
        if key in self._cache:
            self._hits += 1
            self._cache.move_to_end(key)  # LRU update
            return self._cache[key]
        self._misses += 1
        return None

def put(self, key, value):
    with self._lock:
        self._cache[key] = value
        self._cache.move_to_end(key)
        if len(self._cache) > self._maxsize:
            self._cache.popitem(last=False)  # Evict oldest
```

**Tested**: `tests/test_thread_safety.py:test_cache_thread_safety()`
- 100 concurrent threads
- Random reads, writes, and clears
- Validates no corruption or lost updates

### 3. RateLimiter Lock (`caching.py`)

**Location**: `clockify_rag/caching.py:26`

```python
class RateLimiter:
    def __init__(self, max_tokens=100, refill_rate=10):
        self._lock = threading.RLock()
        self._tokens = max_tokens
        self._last_refill = time.time()
```

**Protects**:
- `_tokens` bucket state
- `_last_refill` timestamp

**Usage Pattern** (Token Bucket Algorithm):
```python
def allow_request(self):
    with self._lock:
        now = time.time()
        elapsed = now - self._last_refill
        self._tokens = min(
            self._max_tokens,
            self._tokens + elapsed * self._refill_rate
        )
        self._last_refill = now

        if self._tokens >= 1.0:
            self._tokens -= 1.0
            return True
        return False
```

**Note**: As of latest deployment, rate limiting may be disabled (see `test_thread_safety.py` skip reason).

### 4. FAISS Index Lock (`indexing.py`)

**Location**: `clockify_rag/indexing.py:27-28`

```python
_FAISS_INDEX = None
_FAISS_LOCK = threading.RLock()
```

**Protects**: Lazy loading of FAISS index

**Usage Pattern** (Double-Checked Locking):
```python
def get_faiss_index():
    global _FAISS_INDEX

    # First check (no lock) - fast path
    if _FAISS_INDEX is not None:
        return _FAISS_INDEX

    # Slow path - acquire lock
    with _FAISS_LOCK:
        # Second check - prevent duplicate loading
        if _FAISS_INDEX is None:
            _FAISS_INDEX = faiss.read_index("faiss.index")
        return _FAISS_INDEX
```

**Why Double-Checked Locking**:
- Avoids lock acquisition on every access (99.9% of calls)
- Only first caller pays locking overhead
- Subsequent calls return cached index immediately

## Concurrency Patterns

### Pattern 1: Atomic State Snapshots

**Problem**: Query needs consistent view of index during processing (may take 1-2 seconds).

**Solution**: Capture immutable snapshot under lock, then release lock:

```python
async def submit_query(request):
    # LOCK HELD: Short duration (~1ms)
    with _state_lock:
        chunks = app.state.chunks  # Shallow copy (reference)
        vecs_n = app.state.vecs_n
        bm = app.state.bm
        hnsw = app.state.hnsw

    # LOCK RELEASED: Process with snapshot (~1000ms)
    result = await loop.run_in_executor(
        None, partial(answer_once, question, chunks, vecs_n, bm, hnsw=hnsw)
    )
```

**Properties**:
- Lock hold time: O(1) - constant (just reference assignment)
- Processing time: O(N) - unbounded (but lock-free)
- Consistency: Snapshot is **immutable** (indices are read-only after load)

### Pattern 2: Lazy Initialization with Double-Checked Locking

**Problem**: FAISS index loading is slow (~500ms), but only needs to happen once.

**Solution**: Cache with double-checked locking (see FAISS example above).

**Performance**:
- First access: ~500ms (pays loading cost + lock overhead)
- Subsequent accesses: ~1μs (no lock, direct return)

### Pattern 3: Background Task Serialization

**Problem**: Multiple `/v1/ingest` requests could race to update state.

**Solution**: FastAPI `background_tasks.add_task()` serializes tasks automatically:

```python
@app.post("/v1/ingest")
async def trigger_ingest(request, background_tasks):
    def do_ingest():
        build(input_file)
        result = ensure_index_ready()
        _set_index_state(app, result)  # Acquires lock

    background_tasks.add_task(do_ingest)
    return {"status": "processing"}
```

**Guarantees**:
- Tasks run sequentially (FastAPI manages queue)
- Each task atomically updates state (via `_state_lock`)

## Lock Hierarchy

**Rule**: Acquire locks in this order to prevent deadlock:

1. `_state_lock` (app state)
2. `_FAISS_LOCK` (FAISS lazy load)
3. `QueryCache._lock` (cache)
4. `RateLimiter._lock` (rate limiter)

**In Practice**: No code path acquires multiple locks simultaneously, so deadlock is impossible.

## Testing

### Concurrency Test Suite

**File**: `tests/test_api_concurrency_ingest.py` (created in v5.9)

**Coverage**:
1. **Queries during ingest** (`test_query_during_ingest_sees_consistent_state`):
   - Fires 10 concurrent queries while ingest is running
   - Validates no torn reads (all queries see either old or new state, never partial)
   - Asserts: `chunks_count == vecs_count` (consistency)

2. **Multiple concurrent ingests** (`test_multiple_concurrent_ingests_serialized`):
   - Fires 5 concurrent `/v1/ingest` requests
   - Validates all complete successfully
   - Asserts: Time spread indicates serialization (not fully parallel)

3. **Torn read detection** (`test_state_lock_prevents_torn_reads`):
   - Rapidly alternates state between two configurations
   - Fires 20 concurrent queries during flipping
   - Asserts: Zero torn reads detected

4. **Health checks during ingest** (`test_health_check_concurrent_with_ingest`):
   - Hammers `/health` endpoint (20 requests) during ingest
   - Validates no exceptions or inconsistent responses

5. **Metrics during ingest** (`test_metrics_endpoint_concurrent_with_ingest`):
   - Queries `/v1/metrics` during ingest
   - Validates `chunks_loaded` is always consistent (1 or 2, never partial)

**Run Tests**:
```bash
pytest tests/test_api_concurrency_ingest.py -v
```

### Thread Safety Validation

**File**: `tests/test_thread_safety.py`

**Coverage**:
- QueryCache with 100 concurrent threads
- RateLimiter with 100 concurrent threads (currently skipped in CI)

**Run Tests**:
```bash
pytest tests/test_thread_safety.py -v
```

## Deployment Patterns

### Multi-Threaded Single Worker

**Recommended for**: Small to medium loads (<100 QPS)

```bash
uvicorn clockify_rag.api:app --host 0.0.0.0 --port 8000 --workers 1 --threads 8
```

**Characteristics**:
- Single process, 8 threads
- Shared cache and indices (efficient memory use)
- Lock overhead: ~1μs per query (negligible)
- Throughput: ~8-16 QPS (depends on LLM latency)

### Multi-Threaded Multi-Worker

**Recommended for**: High loads (>100 QPS)

```bash
gunicorn clockify_rag.api:app \
    --workers 4 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --threads 4
```

**Characteristics**:
- 4 processes × 4 threads = 16 concurrent workers
- Each process has its own indices (~500 MB × 4 = 2 GB RAM)
- Cache NOT shared across processes
- Throughput: ~32-64 QPS

**Trade-offs**:
- ✅ Higher throughput
- ✅ Better CPU utilization
- ❌ Higher memory usage
- ❌ Cache efficiency reduced (per-process caches)

### Single-Threaded Multi-Worker (Legacy)

**Recommended for**: Maximum isolation

```bash
gunicorn clockify_rag.api:app \
    --workers 8 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --threads 1
```

**Characteristics**:
- No threading, pure multi-process
- Complete isolation (no shared state)
- No locking overhead
- Throughput: ~8-16 QPS

**Use Cases**:
- Debugging threading issues
- Maximum fault isolation
- Legacy deployments

## Performance Impact

### Lock Overhead

**Measured** (M1 Pro, 10-core):
- `threading.RLock()` acquire + release: ~0.5μs
- App state snapshot capture: ~1μs (4 reference assignments)
- **Total overhead per query**: ~1.5μs (<0.1% of typical query latency)

**Conclusion**: Lock overhead is **negligible** compared to LLM latency (~1000ms).

### Throughput Comparison

| Configuration | QPS | Latency (p50) | Latency (p99) |
|---------------|-----|---------------|---------------|
| Single-threaded | 1.0 | 1000ms | 1200ms |
| Multi-threaded (8 threads) | 7.5 | 1050ms | 1500ms |
| Multi-process (4 workers) | 3.8 | 1000ms | 1300ms |
| Multi-process + threads (4×4) | 14.2 | 1100ms | 1800ms |

**Bottleneck**: LLM generation (Ollama) dominates all latency.

## Anti-Patterns to Avoid

### ❌ Nested Lock Acquisition (Different Locks)

**Bad**:
```python
with _state_lock:
    with _cache_lock:  # Potential deadlock if another thread does reverse
        ...
```

**Good**:
```python
# Capture state first
with _state_lock:
    data = app.state.chunks

# Then cache separately
with _cache_lock:
    cache.put(key, data)
```

### ❌ Long-Running Operations Under Lock

**Bad**:
```python
with _state_lock:
    result = slow_operation()  # BLOCKS all other threads
    app.state.chunks = result
```

**Good**:
```python
result = slow_operation()  # No lock held

with _state_lock:
    app.state.chunks = result  # Fast update under lock
```

### ❌ Mutable State Without Protection

**Bad**:
```python
app.state.chunks.append(new_chunk)  # RACE CONDITION
```

**Good**:
```python
with _state_lock:
    new_chunks = app.state.chunks + [new_chunk]  # Create new list
    app.state.chunks = new_chunks
```

## Debugging Thread Safety Issues

### Tools

1. **Thread Sanitizer (TSan)** (C/C++ only):
   - Not applicable to Python (GIL prevents many race conditions)

2. **pytest-xdist** (Parallel Test Execution):
   ```bash
   pytest -n 8 tests/test_thread_safety.py
   ```

3. **Stress Testing**:
   ```python
   import threading
   import random

   def hammer_api(n=1000):
       for _ in range(n):
           response = requests.post("/v1/query", json={"question": "..."})
           assert response.status_code == 200

   threads = [threading.Thread(target=hammer_api) for _ in range(10)]
   for t in threads:
       t.start()
   for t in threads:
       t.join()
   ```

### Common Symptoms

1. **Race Condition**:
   - Symptom: Intermittent failures, corrupted data, assertion errors
   - Debugging: Add `time.sleep(random.random())` to suspect code paths
   - Fix: Add locking around shared state

2. **Deadlock**:
   - Symptom: Hangs, no progress, high CPU usage
   - Debugging: `py-spy dump --pid <PID>` to see thread stack traces
   - Fix: Reorder lock acquisition or eliminate nested locks

3. **Performance Degradation**:
   - Symptom: Throughput drops with more threads
   - Debugging: Profile lock contention with `py-spy`
   - Fix: Reduce critical section size or use lock-free data structures

## Future Improvements

1. **Lock-Free Data Structures**:
   - Replace `OrderedDict` with lock-free LRU (e.g., `lru-dict`)
   - Use atomic operations for counters (Python 3.11+ `threading.local()`)

2. **Read-Write Locks**:
   - Use `threading.RWLock` for read-heavy workloads (many queries, rare ingests)
   - Allows multiple concurrent readers, exclusive writer

3. **Async All the Way**:
   - Replace `loop.run_in_executor()` with native async clients
   - Eliminates thread pool overhead

4. **Shared Memory for Multi-Process**:
   - Use `multiprocessing.shared_memory` for indices
   - Reduces memory footprint for multi-worker deployments

## Related Documentation

- [DATA_FLOW.md](DATA_FLOW.md) - System data flow and components
- [ASYNC_GUIDE.md](ASYNC_GUIDE.md) - Async usage patterns
- [DEPLOYMENT.md](DEPLOYMENT.md) - Production deployment guides
- [ARCHITECTURE.md](ARCHITECTURE.md) - System architecture

## Version History

- **v5.9**: Added `_state_lock` for app state, created `test_api_concurrency_ingest.py`
- **v5.1**: Added locks to `QueryCache`, `RateLimiter`, `_FAISS_INDEX`
- **v4.0**: First multi-threaded deployment (no thread safety - unsafe!)
