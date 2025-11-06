# Implementation Prompt: Fix All Analysis Issues

**Session Goal**: Systematically implement all fixes and improvements identified in the comprehensive RAG codebase analysis.

**Context**: A detailed analysis was completed (see `ANALYSIS_REPORT1.md`, `IMPROVEMENTS1.jsonl`, `QUICK_WINS1.md`, `ARCHITECTURE_VISION1.md`) identifying 40+ improvements across correctness, performance, RAG quality, and code quality.

**Branch**: `claude/rag-fixes-implementation-[SESSION_ID]`

---

## Session Objectives

Implement all improvements in priority order:
1. **Critical Bugs** (5 issues) - Fix correctness issues
2. **Quick Wins** (10 issues) - High-impact, low-effort improvements
3. **High-Priority Improvements** (Top 20 from IMPROVEMENTS1.jsonl)
4. **Test Coverage** - Add missing tests for critical paths
5. **Documentation Updates** - Document thread safety, add examples

**Expected Outcome**: Production-ready codebase with:
- ✅ All bugs fixed
- ✅ Thread safety implemented
- ✅ Performance optimized (50-200ms faster)
- ✅ Test coverage >60% (from ~20%)
- ✅ Ground truth evaluation dataset created
- ✅ Cross-encoder reranking enabled

---

## Pre-Implementation Checklist

Before starting, read these files to understand the issues:

```bash
# Essential reading (in order)
1. ANALYSIS_REPORT1.md        # Overall analysis and findings
2. IMPROVEMENTS1.jsonl         # Prioritized improvements (Rank 1-30)
3. QUICK_WINS1.md             # Quick wins (<30 min each)
4. ARCHITECTURE_VISION1.md     # Long-term vision (reference only)

# Quick summary
grep -A 5 "Critical Issues" ANALYSIS_REPORT1.md
grep -A 5 "Bugs Found" ANALYSIS_REPORT1.md
```

---

## Implementation Plan

### Phase 1: Critical Bug Fixes (1 hour)

Fix all 5 bugs identified in `ANALYSIS_REPORT1.md`:

#### Bug #1: Build Lock Deadline Not Respected
**File**: `clockify_rag/utils.py:585` and `clockify_support_cli_final.py:585`
**Issue**: Lock can hang longer than 10s due to deadline reset in retry loop

```python
# FIND this code in both files:
if time.time() > deadline:
    raise RuntimeError("Build already in progress; timed out waiting for lock release")
end = time.time() + 10.0  # BUG: resets deadline
while time.time() < end:
    time.sleep(0.25)
    if not os.path.exists(BUILD_LOCK):
        break
else:
    raise RuntimeError("Build already in progress; timed out waiting for lock release")

# REPLACE with:
if time.time() > deadline:
    raise RuntimeError("Build already in progress; timed out waiting for lock release")
while time.time() < deadline:  # Use deadline directly
    time.sleep(0.25)
    if not os.path.exists(BUILD_LOCK):
        break
    if time.time() > deadline:  # Check deadline in loop
        raise RuntimeError("Build already in progress; timed out waiting for lock release")
```

**Validation**: Run `python3 -c "from clockify_rag.utils import build_lock; import time; s=time.time(); build_lock().__enter__(); print(f'Acquired in {time.time()-s:.1f}s')"` - should complete in <0.1s

#### Bug #2: Score Normalization Loses Information
**File**: `clockify_support_cli_final.py:1290`
**Issue**: Returns zeros when std=0, losing rank information

```python
# FIND:
def normalize_scores_zscore(arr):
    a = np.asarray(arr, dtype="float32")
    if a.size == 0:
        return a
    m, s = a.mean(), a.std()
    if s == 0:
        return np.zeros_like(a)  # BUG: loses information
    return (a - m) / s

# REPLACE with:
def normalize_scores_zscore(arr):
    a = np.asarray(arr, dtype="float32")
    if a.size == 0:
        return a
    m, s = a.mean(), a.std()
    if s == 0:
        return a  # FIXED: preserve original when no variance
    return (a - m) / s
```

**Validation**: `python3 -c "from clockify_support_cli_final import normalize_scores_zscore; import numpy as np; print(normalize_scores_zscore([0.5, 0.5, 0.5]))"` - should output `[0.5 0.5 0.5]`

#### Bug #3: Sliding Chunks Overlap Edge Case
**Files**: `clockify_support_cli_final.py:977-983`, `clockify_rag/chunking.py:104-108`
**Issue**: Character-based fallback for oversized sentences doesn't handle overlap correctly

```python
# FIND in sliding_chunks() function:
# Split long sentence by characters
i = 0
while i < sent_len:
    j = min(i + maxc, sent_len)
    out.append(sent[i:j].strip())
    i = j - overlap if j < sent_len else j  # BUG: inconsistent overlap
    continue

# REPLACE with:
# Split long sentence by characters with consistent overlap
i = 0
while i < sent_len:
    j = min(i + maxc, sent_len)
    out.append(sent[i:j].strip())
    if j >= sent_len:
        break
    i = j - overlap if overlap < j else 0  # FIXED: respect overlap
```

**Validation**: Test with long sentence >1600 chars, verify chunks overlap by 200 chars

#### Bug #4: Thread Safety Gaps (CRITICAL)
**Files**: `clockify_rag/caching.py`, `clockify_support_cli_final.py:1398,2063,2170`
**Issue**: Global state not protected by locks

**Step 1**: Add locks to `QueryCache` and `RateLimiter` in `clockify_rag/caching.py`:

```python
import threading

class QueryCache:
    def __init__(self, maxsize=100, ttl_seconds=3600):
        self.maxsize = maxsize
        self.ttl_seconds = ttl_seconds
        self.cache: dict = {}
        self.access_order: deque = deque()
        self.hits = 0
        self.misses = 0
        self._lock = threading.RLock()  # ADD: Reentrant lock

    def get(self, question: str):
        with self._lock:  # WRAP all methods with lock
            # ... existing logic unchanged ...

    def put(self, question: str, answer: str, metadata: dict):
        with self._lock:
            # ... existing logic unchanged ...

    def clear(self):
        with self._lock:
            # ... existing logic unchanged ...

    def stats(self) -> dict:
        with self._lock:
            # ... existing logic unchanged ...

class RateLimiter:
    def __init__(self, max_requests=10, window_seconds=60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests: deque = deque()
        self._lock = threading.RLock()  # ADD

    def allow_request(self) -> bool:
        with self._lock:
            # ... existing logic unchanged ...

    def wait_time(self) -> float:
        with self._lock:
            # ... existing logic unchanged ...
```

**Step 2**: Protect `_FAISS_INDEX` loading in `clockify_rag/indexing.py`:

```python
# ADD at module level
_FAISS_INDEX = None
_FAISS_LOCK = threading.Lock()

def load_faiss_index(path: str = None):
    """Load FAISS index with thread-safe lazy loading."""
    global _FAISS_INDEX
    if path is None or not os.path.exists(path):
        return None

    # Double-checked locking pattern
    if _FAISS_INDEX is not None:
        return _FAISS_INDEX

    with _FAISS_LOCK:
        if _FAISS_INDEX is not None:  # Check again inside lock
            return _FAISS_INDEX

        faiss = _try_load_faiss()
        if faiss:
            _FAISS_INDEX = faiss.read_index(path)
            _FAISS_INDEX.nprobe = ANN_NPROBE
            logger.debug(f"Loaded FAISS index from {path}")
        return _FAISS_INDEX
```

**Step 3**: Do same for `clockify_support_cli_final.py` (search for `_FAISS_INDEX` global)

**Validation**: Run `pytest tests/test_thread_safety.py -v` (create this test - see Phase 4)

#### Bug #5: Exception Handling Masks Bugs
**File**: `clockify_support_cli_final.py:1159`
**Issue**: Catches `EmbeddingError` then re-raises, also catches broad `Exception`

```python
# FIND in embed_texts():
try:
    # embedding code
    vecs.append(emb)
except (requests.exceptions.ConnectTimeout, ...):
    raise EmbeddingError(...) from e
except requests.exceptions.RequestException as e:
    raise EmbeddingError(...) from e
except EmbeddingError:
    raise  # REDUNDANT
except Exception as e:  # TOO BROAD
    raise EmbeddingError(...) from e

# REPLACE with:
try:
    # embedding code
    vecs.append(emb)
except EmbeddingError:
    raise  # Re-raise our own errors as-is
except (requests.exceptions.ConnectTimeout, ...):
    raise EmbeddingError(...) from e
except requests.exceptions.RequestException as e:
    raise EmbeddingError(...) from e
except (KeyError, IndexError, TypeError) as e:  # SPECIFIC errors
    raise EmbeddingError(f"Embedding chunk {i}: invalid response format: {e}") from e
except Exception as e:
    logger.error(f"Unexpected error in embed_texts chunk {i}: {e}", exc_info=True)
    raise  # Let unexpected errors propagate
```

**Validation**: Trigger embedding error, verify traceback is preserved

---

### Phase 2: Quick Wins (1.5 hours)

Implement all 10 quick wins from `QUICK_WINS1.md`:

#### Quick Win #1: Already done above (Build Lock Fix)

#### Quick Win #2: Preload FAISS Index (10 min)
**File**: `clockify_support_cli_final.py:1846` (in `load_index()`)

```python
# FIND load_index() function, ADD after loading bm:

# Preload FAISS index if enabled (Quick Win #2)
global _FAISS_INDEX
if USE_ANN == "faiss" and os.path.exists(FILES["faiss_index"]):
    try:
        _FAISS_INDEX = load_faiss_index(FILES["faiss_index"])
        if _FAISS_INDEX:
            _FAISS_INDEX.nprobe = ANN_NPROBE
            logger.info(f"✓ Preloaded FAISS index: nprobe={ANN_NPROBE}")
        else:
            logger.info("FAISS index file exists but failed to load, will fall back")
    except Exception as e:
        logger.warning(f"Failed to preload FAISS: {e}, will lazy-load on first query")
        _FAISS_INDEX = None

# Return statement unchanged
return chunks, vecs_n, bm, hnsw
```

**Validation**: Run query, check logs for "✓ Preloaded FAISS index" message

#### Quick Win #3: Already done above (Score Normalization Fix)

#### Quick Win #4: Lower BM25 Early Termination Threshold (5 min)
**Files**: `clockify_rag/indexing.py:163`, `clockify_support_cli_final.py:1215`

```python
# FIND:
if top_k is not None and top_k > 0 and len(doc_lens) > top_k * 2:

# REPLACE with:
if top_k is not None and top_k > 0 and len(doc_lens) > top_k * 1.5:  # Lower threshold
```

**Validation**: Benchmark BM25 on 1k-10k docs, verify 2-3x speedup

#### Quick Win #5: Add 'make dev' Target (5 min)
**File**: `Makefile:111`

```makefile
# ADD after 'clean:' target:

dev: venv install pre-commit-install
	@echo ""
	@echo "✅ Development environment ready!"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Activate venv: source rag_env/bin/activate"
	@echo "  2. Build index: make build"
	@echo "  3. Start chat: make chat"
	@echo ""
	@echo "Or run all steps: source rag_env/bin/activate && make build && make chat"
	@echo ""
```

**Validation**: Fresh clone, run `make dev`, verify all setup completes

#### Quick Win #6: Extract Magic Numbers to Config (15 min)
**File**: `clockify_rag/config.py:97`

```python
# ADD to config.py:

# ====== RETRIEVAL CONFIG (CONTINUED) ======
# FAISS candidate generation
FAISS_CANDIDATE_MULTIPLIER = 3  # Retrieve top_k * 3 candidates for reranking
ANN_CANDIDATE_MIN = 200  # Minimum candidates even if top_k is small

# Reranking
RERANK_SNIPPET_MAX_CHARS = 500  # Truncate chunk text for reranking prompt
RERANK_MAX_CHUNKS = 12  # Maximum chunks to send to reranking

# Retrieval thresholds
COVERAGE_MIN_CHUNKS = 2  # Minimum chunks above threshold to proceed
```

**Then replace all hardcoded values**:
```bash
# Search for magic numbers and replace:
grep -n "max(200, top_k" clockify_support_cli_final.py
# Replace with: max(ANN_CANDIDATE_MIN, top_k * FAISS_CANDIDATE_MULTIPLIER)

grep -n "chunk\['text'\]\[:500\]" clockify_support_cli_final.py
# Replace with: chunk['text'][:RERANK_SNIPPET_MAX_CHARS]

grep -n "len(selected) < 2" clockify_support_cli_final.py
# Replace with: len(selected) < COVERAGE_MIN_CHUNKS
```

**Validation**: `grep -n '\b[0-9]{3,}\b' clockify_support_cli_final.py` - verify no unexplained magic numbers

#### Quick Win #7: Add Type Hints for Return Values (20 min)

```python
# ADD return types to key functions:

def load_index() -> tuple[list[dict], np.ndarray, dict, object] | None:
    """Load index artifacts. Returns (chunks, vecs_n, bm, hnsw) or None."""
    ...

def retrieve(
    question: str,
    chunks: list[dict],
    vecs_n: np.ndarray,
    bm: dict,
    top_k: int = 12,
    hnsw: object = None,
    retries: int = 0
) -> tuple[list[int], dict[str, np.ndarray]]:
    """Hybrid retrieval. Returns (filtered_indices, scores_dict)."""
    ...

def answer_once(
    question: str,
    chunks: list[dict],
    vecs_n: np.ndarray,
    bm: dict,
    top_k: int = 12,
    pack_top: int = 6,
    threshold: float = 0.30,
    use_rerank: bool = False,
    debug: bool = False,
    hnsw: object = None,
    seed: int = DEFAULT_SEED,
    num_ctx: int = DEFAULT_NUM_CTX,
    num_predict: int = DEFAULT_NUM_PREDICT,
    retries: int = 0
) -> tuple[str, dict]:
    """Answer a single question. Returns (answer_text, metadata)."""
    ...
```

**Validation**: Run `mypy clockify_support_cli_final.py --check-untyped-defs`

#### Quick Win #8: Improve Error Messages with Hints (15 min)

```python
# UPDATE all error messages to include hints:

# In load_index():
raise IndexError(
    f"{FILES['index_meta']} missing. "
    f"Run 'python3 clockify_support_cli.py build knowledge_full.md' to create index."
)

# In embed_texts():
raise EmbeddingError(
    f"Embedding chunk {i} failed: {e}\n"
    f"Hints:\n"
    f"  - Check Ollama is running: curl {OLLAMA_URL}/api/version\n"
    f"  - Increase timeout: EMB_READ_TIMEOUT=120 (current: {EMB_READ_T}s)\n"
    f"  - Use local embeddings: EMB_BACKEND=local"
) from e

# In build():
raise BuildError(
    f"{md_path} not found.\n"
    f"Expected knowledge base file at this location.\n"
    f"Hint: Ensure knowledge_full.md exists in current directory."
)
```

**Validation**: Trigger errors intentionally, verify hints are helpful

#### Quick Win #9: Add Cache Hit Logging (10 min)
**File**: `clockify_support_cli_final.py:2406`

```python
# FIND in answer_once():
cached_result = QUERY_CACHE.get(question)
if cached_result is not None:
    answer, metadata = cached_result
    metadata["cached"] = True
    metadata["cache_hit"] = True
    # ADD:
    cache_age = time.time() - metadata.get("timestamp", time.time())
    logger.info(f"[cache] HIT question_len={len(question)} cache_age={cache_age:.1f}s")
    return answer, metadata
```

**Validation**: Ask same question twice, verify cache hit logged on second query

#### Quick Win #10: Document Thread Safety Requirement (5 min)
**File**: `CLAUDE.md:94`

```markdown
## Thread Safety

**IMPORTANT**: The current implementation is **thread-safe as of v5.1** due to locks added to shared state.

### Deployment Options

**Option 1: Multi-threaded (RECOMMENDED)**
- Deploy with multi-worker, multi-threaded processes (e.g., `gunicorn -w 4 --threads 4`)
- Thread safety locks protect shared state (QueryCache, RateLimiter, _FAISS_INDEX)
- Cache and rate limiter shared across threads within same process

**Option 2: Single-threaded (legacy)**
- Deploy with single-worker processes (e.g., `gunicorn -w 4 --threads 1`)
- Each worker has its own process memory (no shared state)
- Cache and rate limiter per-process

### Thread Safety Validation
Run concurrent tests: `pytest tests/test_thread_safety.py -v -n 4`
```

---

### Phase 3: High-Priority Improvements (2-3 hours)

Implement Top 10 from `IMPROVEMENTS1.jsonl`:

#### Improvement #1: Create Ground Truth Evaluation Dataset (HIGH impact, LOW effort)

**Create**: `eval_datasets/clockify_v1.jsonl`

```jsonl
{"query": "How do I track time in Clockify?", "relevant_chunk_ids": ["<find from chunks.jsonl>"], "difficulty": "easy", "tags": ["time-tracking", "basic"], "language": "en"}
{"query": "What are the pricing tiers?", "relevant_chunk_ids": ["<find from chunks.jsonl>"], "difficulty": "easy", "tags": ["pricing", "billing"], "language": "en"}
{"query": "How do I set up SSO with Okta?", "relevant_chunk_ids": ["<find from chunks.jsonl>"], "difficulty": "hard", "tags": ["sso", "authentication", "advanced"], "language": "en"}
{"query": "Can I track time offline on mobile?", "relevant_chunk_ids": ["<find from chunks.jsonl>"], "difficulty": "medium", "tags": ["mobile", "offline"], "language": "en"}
{"query": "What's the difference between Basic and Pro plans?", "relevant_chunk_ids": ["<find from chunks.jsonl>"], "difficulty": "medium", "tags": ["pricing", "comparison"], "language": "en"}
```

**Steps**:
1. Load `chunks.jsonl` to see available chunks
2. Create 50-100 representative questions from documentation
3. For each question, manually identify 2-5 relevant chunk IDs
4. Add difficulty labels (easy/medium/hard)
5. Save as JSONL format

**Helper script**:
```python
# create_ground_truth.py
import json

# Load chunks
with open("chunks.jsonl") as f:
    chunks = [json.loads(line) for line in f if line.strip()]

# Interactive helper
print(f"Loaded {len(chunks)} chunks")
print("\nSample questions to create ground truth for:")
questions = [
    "How do I track time?",
    "What are the pricing plans?",
    "How do I invite team members?",
    "Can I export timesheets to CSV?",
    # Add 46 more...
]

for q in questions:
    print(f"\nQ: {q}")
    print("Search chunks for relevant ones...")
    # Manual process: search chunks, identify IDs
```

**Validation**: Run `python3 eval.py --dataset eval_datasets/clockify_v1.jsonl`, verify metrics computed

#### Improvement #2: Already done above (Thread Safety)

#### Improvement #3: Enable Cross-Encoder Reranking (HIGH impact, LOW effort)

**Step 1**: Add dependency to `requirements.txt`:
```
sentence-transformers==3.3.1  # Already included, supports cross-encoder
```

**Step 2**: Create `clockify_rag/reranking/cross_encoder.py`:
```python
from sentence_transformers import CrossEncoder
import numpy as np

class CrossEncoderReranker:
    """Rerank using cross-encoder model."""

    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L6-v2"):
        self.model = CrossEncoder(model_name)
        logger.info(f"Loaded cross-encoder: {model_name}")

    def rerank(self, question: str, chunks: list, top_k: int = 6) -> list:
        """Rerank chunks using cross-encoder."""
        if not chunks:
            return []

        # Prepare pairs: (question, chunk_text)
        pairs = [(question, c["text"][:512]) for c in chunks]  # Truncate to 512 chars

        # Predict scores (batch inference)
        scores = self.model.predict(pairs, show_progress_bar=False)

        # Sort by score
        ranked = sorted(zip(range(len(chunks)), scores), key=lambda x: x[1], reverse=True)
        return [chunks[idx] for idx, score in ranked[:top_k]]
```

**Step 3**: Update config to enable by default:
```python
# clockify_rag/config.py
USE_RERANK_DEFAULT = True
RERANK_MODEL = "cross-encoder/ms-marco-MiniLM-L6-v2"
```

**Step 4**: Update `answer_once()` signature:
```python
def answer_once(..., use_rerank=USE_RERANK_DEFAULT, ...):
```

**Validation**: Query with `--rerank`, verify cross-encoder used and improves accuracy

#### Improvement #4: Add Retrieval Pipeline Tests (HIGH impact, MEDIUM effort)

**Create**: `tests/test_retrieval.py`

```python
import pytest
import numpy as np
from clockify_support_cli_final import retrieve, build_bm25, normalize_scores_zscore

@pytest.fixture
def sample_data():
    """Sample chunks and embeddings for testing."""
    chunks = [
        {"id": "1", "title": "Time Tracking", "section": "Basics", "text": "Track time by clicking the timer button"},
        {"id": "2", "title": "Pricing", "section": "Plans", "text": "Free plan includes unlimited users"},
        {"id": "3", "title": "Time Tracking", "section": "Advanced", "text": "Manual time entries can be added"},
    ]
    # Create simple embeddings (3 chunks, 384 dims)
    vecs = np.random.randn(3, 384).astype("float32")
    vecs = vecs / np.linalg.norm(vecs, axis=1, keepdims=True)  # Normalize
    bm = build_bm25(chunks)
    return chunks, vecs, bm

def test_retrieve_returns_correct_top_k(sample_data):
    """Verify retrieval returns exactly top_k results."""
    chunks, vecs, bm = sample_data
    question = "How do I track time?"

    selected, scores = retrieve(question, chunks, vecs, bm, top_k=2)

    assert len(selected) <= 2, "Should return at most top_k results"
    assert all(idx < len(chunks) for idx in selected), "Indices should be valid"

def test_retrieve_with_empty_query(sample_data):
    """Verify retrieval handles empty query gracefully."""
    chunks, vecs, bm = sample_data

    # Should raise ValueError due to sanitization
    with pytest.raises(ValueError, match="Question cannot be empty"):
        retrieve("", chunks, vecs, bm)

def test_normalize_scores_zscore_edge_cases():
    """Test score normalization edge cases."""
    # All equal scores
    scores = [0.5, 0.5, 0.5]
    result = normalize_scores_zscore(scores)
    assert np.allclose(result, [0.5, 0.5, 0.5]), "Should preserve values when std=0"

    # Empty array
    result = normalize_scores_zscore([])
    assert len(result) == 0

    # Normal case
    scores = [1.0, 2.0, 3.0]
    result = normalize_scores_zscore(scores)
    assert abs(result.mean()) < 0.01, "Mean should be ~0 after normalization"
    assert abs(result.std() - 1.0) < 0.01, "Std should be ~1 after normalization"
```

**Create**: `tests/test_thread_safety.py`

```python
import pytest
import threading
from clockify_rag.caching import QueryCache, RateLimiter

def test_query_cache_thread_safe():
    """Verify cache works correctly with concurrent access."""
    cache = QueryCache()
    results = []
    errors = []

    def worker(question, answer):
        try:
            cache.put(question, answer, {})
            result = cache.get(question)
            results.append((question, result))
        except Exception as e:
            errors.append(e)

    threads = [threading.Thread(target=worker, args=(f"q{i}", f"a{i}")) for i in range(100)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert len(errors) == 0, f"No errors should occur: {errors}"
    assert len(results) == 100, "All threads should complete"
    # Verify all queries cached correctly
    for question, result in results:
        if result is None:
            # Query may have been evicted if cache full
            assert len(cache.cache) >= cache.maxsize

def test_rate_limiter_thread_safe():
    """Verify rate limiter works correctly with concurrent access."""
    limiter = RateLimiter(max_requests=50, window_seconds=1)
    allowed_count = [0]
    denied_count = [0]
    lock = threading.Lock()

    def worker():
        if limiter.allow_request():
            with lock:
                allowed_count[0] += 1
        else:
            with lock:
                denied_count[0] += 1

    threads = [threading.Thread(target=worker) for _ in range(100)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert allowed_count[0] + denied_count[0] == 100
    assert allowed_count[0] <= 50, "Should not exceed max_requests"
    assert denied_count[0] >= 50, "Should deny excess requests"
```

**Validation**: Run `pytest tests/test_retrieval.py tests/test_thread_safety.py -v`

#### Improvements #5-10: See `IMPROVEMENTS1.jsonl` for details

For each improvement:
1. Read the JSON entry for implementation details
2. Follow the proposed changes
3. Test with the expected validation
4. Commit with descriptive message

---

### Phase 4: Test Coverage Expansion (1-2 hours)

Add comprehensive tests to reach 60%+ coverage:

```bash
# Create missing test files:
tests/test_mmr.py              # MMR diversification tests
tests/test_reranking.py        # Reranking tests (LLM + cross-encoder)
tests/test_llm.py              # LLM interaction tests
tests/test_integration.py      # End-to-end tests
tests/test_faiss.py            # FAISS index tests
tests/conftest.py              # Shared fixtures

# Run coverage
pytest tests/ --cov=clockify_support_cli_final --cov=clockify_rag --cov-report=html --cov-report=term
```

**Shared fixtures** (`tests/conftest.py`):

```python
import pytest
import numpy as np
import json
import tempfile
import os

@pytest.fixture
def sample_chunks():
    """Sample chunks for testing."""
    return [
        {"id": "1", "title": "Time Tracking", "section": "Basics", "text": "Track time by clicking the timer button", "url": "https://clockify.me/help"},
        {"id": "2", "title": "Pricing", "section": "Plans", "text": "Free plan includes unlimited users", "url": "https://clockify.me/pricing"},
        {"id": "3", "title": "Time Tracking", "section": "Advanced", "text": "Manual time entries can be added", "url": "https://clockify.me/help"},
    ]

@pytest.fixture
def sample_embeddings():
    """Sample embeddings for testing (384-dim for local, 768-dim for Ollama)."""
    from clockify_rag.config import EMB_DIM
    vecs = np.random.randn(3, EMB_DIM).astype("float32")
    vecs = vecs / np.linalg.norm(vecs, axis=1, keepdims=True)  # Normalize
    return vecs

@pytest.fixture
def sample_bm25(sample_chunks):
    """Sample BM25 index for testing."""
    from clockify_support_cli_final import build_bm25
    return build_bm25(sample_chunks)

@pytest.fixture
def temp_index_dir(sample_chunks, sample_embeddings, sample_bm25):
    """Temporary directory with full index artifacts."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Write chunks
        with open(os.path.join(tmpdir, "chunks.jsonl"), "w") as f:
            for c in sample_chunks:
                f.write(json.dumps(c) + "\n")

        # Write embeddings
        np.save(os.path.join(tmpdir, "vecs_n.npy"), sample_embeddings)

        # Write BM25
        with open(os.path.join(tmpdir, "bm25.json"), "w") as f:
            json.dump(sample_bm25, f)

        # Write metadata
        meta = {"chunks": len(sample_chunks), "emb_rows": len(sample_embeddings), "bm25_docs": len(sample_bm25["doc_lens"])}
        with open(os.path.join(tmpdir, "index.meta.json"), "w") as f:
            json.dump(meta, f)

        yield tmpdir
```

---

### Phase 5: Documentation Updates (30 min)

Update documentation to reflect fixes:

#### Update `CLAUDE.md`:
```markdown
## Recent Improvements (v5.1)

### Bug Fixes
- ✅ Fixed build lock deadline bug (lock now respects 10s timeout)
- ✅ Fixed score normalization edge case (preserves rank information when std=0)
- ✅ Added thread safety locks to all shared state (QueryCache, RateLimiter, _FAISS_INDEX)
- ✅ Improved error messages with actionable hints

### Performance Improvements
- ✅ Preload FAISS index at startup (50-200ms faster first query)
- ✅ Lower BM25 early termination threshold (2-3x speedup on mid-size corpora)
- ✅ Extract magic numbers to config constants (better maintainability)

### Quality Improvements
- ✅ Added ground truth evaluation dataset (50 examples in eval_datasets/)
- ✅ Enabled cross-encoder reranking by default (10-15% accuracy improvement)
- ✅ Added comprehensive test coverage (60%+ coverage, up from 20%)

### Developer Experience
- ✅ Added `make dev` target for one-command setup
- ✅ Added type hints for better IDE support
- ✅ Improved error messages with hints
- ✅ Added cache hit logging for observability
```

#### Update `README.md`:
```markdown
## Testing

Run full test suite:
```bash
# All tests
make test

# With coverage report
pytest tests/ --cov=clockify_rag --cov-report=html
open htmlcov/index.html

# Thread safety tests
pytest tests/test_thread_safety.py -v -n 4

# Integration tests
pytest tests/test_integration.py -v
```

## Deployment

### Thread Safety (v5.1+)
This version is **thread-safe** and can be deployed with multiple threads:
```bash
# Multi-threaded deployment (RECOMMENDED)
gunicorn -w 4 --threads 4 app:app

# Or with uvicorn
uvicorn app:app --workers 4
```

### Evaluation
Run evaluation on ground truth dataset:
```bash
make eval
# Or: python3 eval.py --dataset eval_datasets/clockify_v1.jsonl
```
```

---

## Testing Checklist

After implementing all changes, run comprehensive validation:

```bash
# 1. Unit tests (should pass 100%)
pytest tests/ -v

# 2. Coverage (should be >60%)
pytest tests/ --cov=clockify_rag --cov=clockify_support_cli_final --cov-report=term

# 3. Thread safety tests (should pass)
pytest tests/test_thread_safety.py -v -n 4

# 4. Smoke tests (should pass)
bash scripts/smoke.sh

# 5. Build test (should complete in <10 min)
make clean
time make build  # Should complete in <10 min for 10k chunks

# 6. Query test (should work)
make chat
> How do I track time?  # Should see cache miss
> How do I track time?  # Should see cache hit
> :exit

# 7. Evaluation (should show metrics)
make eval  # Should output MRR, NDCG, P@5

# 8. Benchmark (should show improvements)
make benchmark-quick  # Compare with baseline

# 9. Type checking (should pass)
mypy clockify_support_cli_final.py clockify_rag/

# 10. Linting (should pass)
make lint
```

---

## Git Workflow

Follow this exact workflow:

```bash
# 1. Create new branch
git checkout -b claude/rag-fixes-implementation-011CUrvxHsqtUG3XsqWiAY6c

# 2. Implement changes incrementally
# After each phase, commit:
git add -A
git commit -m "fix: implement Phase 1 - critical bug fixes

- Fix build lock deadline bug (utils.py, clockify_support_cli_final.py)
- Fix score normalization edge case
- Add thread safety locks to QueryCache, RateLimiter, _FAISS_INDEX
- Fix sliding chunks overlap edge case
- Improve exception handling in embed_texts()

All 5 critical bugs now fixed and tested."

# 3. Continue for each phase
git commit -m "feat: implement Phase 2 - quick wins

- Preload FAISS index (50-200ms faster)
- Lower BM25 threshold (2-3x speedup)
- Add make dev target
- Extract magic numbers to config
- Add type hints for key functions
- Improve error messages with hints
- Add cache hit logging
- Document thread safety

All 10 quick wins implemented."

git commit -m "feat: implement Phase 3 - high priority improvements

- Create ground truth evaluation dataset (50 examples)
- Enable cross-encoder reranking by default
- Add retrieval pipeline tests
- Add thread safety tests
- Implement improvements #4-10 from IMPROVEMENTS1.jsonl

High-priority improvements complete."

git commit -m "test: expand test coverage to 60%+

- Add test_retrieval.py (hybrid retrieval tests)
- Add test_thread_safety.py (concurrency tests)
- Add test_mmr.py (diversification tests)
- Add test_integration.py (end-to-end tests)
- Add test_faiss.py (FAISS index tests)
- Add conftest.py (shared fixtures)

Coverage increased from 20% to 60%+."

git commit -m "docs: update documentation with v5.1 improvements

- Update CLAUDE.md with bug fixes and improvements
- Update README.md with testing and deployment instructions
- Document thread safety guarantees
- Add evaluation instructions

Documentation now reflects all v5.1 changes."

# 4. Push to remote
git push -u origin claude/rag-fixes-implementation-011CUrvxHsqtUG3XsqWiAY6c

# 5. Verify all checks pass
# Check GitHub actions (if configured)

# 6. Ready for PR
echo "Implementation complete! Create PR to merge fixes."
```

---

## Success Criteria

All criteria must be met before considering the session complete:

### Bugs Fixed (5/5)
- [x] Build lock deadline respected
- [x] Score normalization preserves information
- [x] Sliding chunks overlap correct
- [x] Thread safety locks added
- [x] Exception handling specific

### Quick Wins (10/10)
- [x] All 10 quick wins from QUICK_WINS1.md implemented
- [x] Performance improvements verified

### High-Priority Improvements (Top 10)
- [x] Ground truth dataset created (50+ examples)
- [x] Thread safety implemented
- [x] Cross-encoder reranking enabled
- [x] Retrieval tests added
- [x] Improvements #5-10 implemented

### Test Coverage
- [x] Coverage >60% (up from 20%)
- [x] All tests passing
- [x] Thread safety validated

### Documentation
- [x] CLAUDE.md updated
- [x] README.md updated
- [x] Thread safety documented

### Validation
- [x] All tests pass: `pytest tests/ -v`
- [x] Smoke tests pass: `bash scripts/smoke.sh`
- [x] Type checking passes: `mypy`
- [x] Linting passes: `make lint`
- [x] Build completes: `make build`
- [x] Evaluation runs: `make eval`
- [x] Benchmarks show improvement

---

## Expected Outcomes

After completing this session:

### Performance
- First query: 50-200ms faster (FAISS preload)
- BM25 queries: 2-3x faster (lower threshold)
- Thread-safe: Can handle concurrent queries

### Quality
- Cross-encoder reranking: 10-15% accuracy improvement
- Ground truth evaluation: Metrics tracked (MRR, NDCG, P@5)
- Test coverage: 60%+ (critical paths tested)

### Reliability
- All bugs fixed
- Thread-safe for multi-threaded deployment
- Better error messages

### Developer Experience
- One-command setup: `make dev`
- Better documentation
- Type hints for IDE support

---

## Timeline Estimate

- **Phase 1 (Bugs)**: 1 hour
- **Phase 2 (Quick Wins)**: 1.5 hours
- **Phase 3 (High Priority)**: 2-3 hours
- **Phase 4 (Tests)**: 1-2 hours
- **Phase 5 (Docs)**: 0.5 hours

**Total**: 6-8 hours for complete implementation

---

## Troubleshooting

### If tests fail:
1. Check error messages carefully
2. Verify fixtures are correct
3. Run single test: `pytest tests/test_file.py::test_name -v`
4. Check test isolation (tests should not depend on each other)

### If build fails:
1. Clean artifacts: `make clean`
2. Rebuild: `make build`
3. Check logs for specific errors
4. Verify knowledge_full.md exists

### If imports fail:
1. Verify virtual environment activated: `source rag_env/bin/activate`
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Check Python version: `python3 --version` (should be 3.9+)

---

## Final Verification

Before creating PR, run this final checklist:

```bash
# Clean slate
make clean

# Full test suite
make test  # All tests pass

# Build from scratch
make build  # Completes successfully

# Evaluation
make eval  # Shows metrics (MRR, NDCG, P@5)

# Smoke tests
make smoke  # All pass

# Type checking
mypy clockify_support_cli_final.py clockify_rag/  # No errors

# Linting
make lint  # No issues

# Coverage report
pytest tests/ --cov=clockify_rag --cov-report=term  # >60%

# Integration test
make chat
> How do I track time?
> How do I track time?  # Should see cache hit
> :exit

echo "✅ All verification complete - ready for PR!"
```

---

**IMPORTANT**: Document any deviations from this plan in commit messages. If you encounter blockers, document them clearly and propose alternatives.

---

**End of Implementation Prompt**

This prompt should enable systematic implementation of all identified fixes and improvements. Good luck! 🚀
