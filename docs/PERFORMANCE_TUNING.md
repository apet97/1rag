# Performance Tuning Guide

Optimize Clockify RAG for your specific workload and hardware.

## Quick Performance Checklist

1. **FAISS enabled** - 10-50x faster retrieval
2. **Appropriate chunk size** - Balance context vs precision
3. **Optimal pack_top** - Reduce LLM tokens for speed
4. **Query caching** - 100% cache hit on repeats
5. **Connection pooling** - Reduce Ollama overhead

---

## Retrieval Performance

### FAISS Index Configuration

FAISS provides approximate nearest neighbor (ANN) search for 10-50x speedup.

**Enable FAISS:**
```bash
USE_ANN=faiss python -m clockify_rag.cli_modern ingest --force
```

**Tuning parameters:**

| Parameter | Default | Description | Trade-off |
|-----------|---------|-------------|-----------|
| `ANN_NLIST` | 64 | Number of IVF clusters | Higher = slower build, faster search |
| `ANN_NPROBE` | 16 | Clusters to search per query | Higher = more accurate, slower |
| `FAISS_IVF_MIN_ROWS` | 20000 | Minimum rows for IVF vs Flat | Below threshold uses linear search |

**Recommendations:**
- Small corpus (< 5K chunks): Use defaults, FAISS will use FlatIP
- Medium corpus (5K-50K): `ANN_NLIST=64`, `ANN_NPROBE=16`
- Large corpus (50K+): `ANN_NLIST=256`, `ANN_NPROBE=32`

```bash
# For large corpus
ANN_NLIST=256 ANN_NPROBE=32 python -m clockify_rag.cli_modern ingest --force
```

### BM25 Configuration

BM25 provides lexical search alongside dense retrieval.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `BM25_K1` | 1.2 | Term frequency saturation |
| `BM25_B` | 0.65 | Document length normalization |

**For technical documentation:**
```bash
# Slightly favor term matching (default is good for most cases)
BM25_K1=1.5 BM25_B=0.70 python -m clockify_rag.cli_modern ingest
```

### Hybrid Search Tuning

Control the balance between dense (semantic) and lexical (BM25) search.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `ALPHA_HYBRID` | 0.5 | BM25 weight (0=pure dense, 1=pure BM25) |
| `MMR_LAMBDA` | 0.75 | Relevance vs diversity (higher = more relevance) |

**Query type recommendations:**

| Query Type | Alpha | Reason |
|------------|-------|--------|
| Technical/procedural | 0.65 | BM25 better for exact terms |
| Conceptual/factual | 0.35 | Dense better for semantics |
| Mixed/general | 0.50 | Balanced (default) |

```bash
# For technical support queries
ALPHA_HYBRID=0.6 python -m clockify_rag.cli_modern query "..."
```

---

## Chunking Strategy

Chunk size affects both retrieval precision and LLM context quality.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `CHUNK_CHARS` | 1600 | Characters per chunk |
| `CHUNK_OVERLAP` | 200 | Overlap between chunks |

### Trade-offs

**Smaller chunks (800-1200 chars):**
- Pros: Better precision, more specific matches
- Cons: May miss context, more chunks to process

**Larger chunks (1600-2400 chars):**
- Pros: More context per match
- Cons: May include irrelevant content

**Recommendations:**
- FAQ/short answers: 800-1200 chars
- Procedures/tutorials: 1600-2000 chars (default)
- Long-form documentation: 2000-2400 chars

```bash
# For FAQ-style content
CHUNK_CHARS=1000 CHUNK_OVERLAP=150 python -m clockify_rag.cli_modern ingest
```

---

## LLM Performance

### Context Window Management

| Parameter | Default | Description |
|-----------|---------|-------------|
| `CTX_TOKEN_BUDGET` | 12000 | Max tokens for context |
| `DEFAULT_NUM_CTX` | 32768 | LLM context window |
| `DEFAULT_NUM_PREDICT` | 512 | Max response tokens |

**Reduce latency by limiting context:**
```bash
# Faster but less context
DEFAULT_PACK_TOP=5 CTX_TOKEN_BUDGET=8000 python -m clockify_rag.cli_modern query "..."
```

### Pack Top Tuning

`pack_top` controls how many chunks are sent to the LLM.

| Scenario | pack_top | Latency | Quality |
|----------|----------|---------|---------|
| Speed priority | 3-5 | Fast | May miss context |
| Balanced | 8 | Medium | Good (default) |
| Quality priority | 10-15 | Slower | Best coverage |

```bash
# For complex multi-part questions
DEFAULT_PACK_TOP=12 python -m clockify_rag.cli_modern query "Compare all pricing tiers"
```

### Connection Management

**Timeout settings:**

| Parameter | Default | Description |
|-----------|---------|-------------|
| `DEFAULT_CONNECT_TIMEOUT` | 3s | Connection timeout |
| `DEFAULT_READ_TIMEOUT` | 120s | Response timeout |
| `DEFAULT_RETRIES` | 2 | Retry attempts |

```bash
# For unstable connections
DEFAULT_CONNECT_TIMEOUT=5 DEFAULT_RETRIES=3 python -m clockify_rag.api
```

---

## Caching

### Query Cache

The query cache eliminates recomputation for repeated queries.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `CACHE_MAXSIZE` | 100 | Max cached queries |
| `CACHE_TTL` | 3600 | TTL in seconds (1 hour) |

**High-traffic deployments:**
```bash
# More cache entries, longer TTL
CACHE_MAXSIZE=500 CACHE_TTL=7200 python -m clockify_rag.api
```

### Embedding Cache

Embeddings are cached to avoid recomputation during rebuilds.

**Location:** `emb_cache.jsonl`

**Clear if changing embedding model:**
```bash
rm emb_cache.jsonl
```

---

## Embedding Backend

### Ollama (Remote) - Default

- Model: `nomic-embed-text` (768-dim)
- Speed: Fast (GPU accelerated)
- Network: Requires Ollama connection

```bash
EMB_BACKEND=ollama RAG_EMBED_MODEL=nomic-embed-text python -m clockify_rag.cli_modern ingest
```

### Local Embeddings - Fallback

- Model: `all-MiniLM-L6-v2` (384-dim)
- Speed: Slower (CPU only)
- Network: No network required

```bash
EMB_BACKEND=local python -m clockify_rag.cli_modern ingest
```

### Batch Processing

Control parallel embedding computation:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `EMB_BATCH_SIZE` | 32 | Texts per batch |
| `EMB_MAX_WORKERS` | 8 | Parallel workers |

**For memory-constrained systems:**
```bash
EMB_BATCH_SIZE=16 EMB_MAX_WORKERS=4 python -m clockify_rag.cli_modern ingest
```

---

## Rate Limiting

Prevent overload with token bucket rate limiting.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `RATE_LIMIT_ENABLED` | false | Enable rate limiting |
| `RATE_LIMIT_REQUESTS` | 10 | Requests per window |
| `RATE_LIMIT_WINDOW` | 60 | Window in seconds |

```bash
# Allow 30 requests per minute
RATE_LIMIT_ENABLED=true RATE_LIMIT_REQUESTS=30 python -m clockify_rag.api
```

---

## Benchmarking

### Measure Query Latency

```bash
# Single query timing
time python -m clockify_rag.cli_modern query "How do I lock timesheets?"

# Batch benchmark
for i in {1..10}; do
  time curl -s -X POST http://localhost:8000/v1/query \
    -d '{"question":"How do I lock timesheets?"}' > /dev/null
done 2>&1 | grep real
```

### Latency Breakdown

Query the API for timing breakdown:

```bash
curl -X POST http://localhost:8000/v1/query \
  -d '{"question":"...", "debug":true}' | jq '.timing'
```

Output:
```json
{
  "embedding_ms": 45.2,
  "retrieval_ms": 120.8,
  "llm_ms": 1050.3
}
```

### Metrics Analysis

```bash
# Get latency percentiles
curl http://localhost:8000/v1/metrics | jq '.histograms.query_latency_ms'
```

---

## Hardware Recommendations

### M1/M2/M3 Mac (Development)

- 16GB RAM minimum for comfortable operation
- FAISS via conda (not pip)
- Local embeddings work well
- Enable Metal acceleration in Ollama

### Production Server

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | 4 cores | 8+ cores |
| RAM | 8GB | 16GB+ |
| GPU | Optional | NVIDIA with 8GB+ VRAM |
| Storage | SSD | NVMe SSD |

### Docker Deployment

```dockerfile
# Increase ulimits for connection handling
--ulimit nofile=65535:65535

# Memory limits
--memory=8g --memory-swap=8g
```

---

## Common Bottlenecks

### 1. Slow Embeddings

**Symptoms:** High `embedding_ms` in timing

**Solutions:**
- Use Ollama with GPU acceleration
- Reduce chunk count during ingest
- Use embedding cache

### 2. Slow Retrieval

**Symptoms:** High `retrieval_ms`

**Solutions:**
- Enable FAISS indexing
- Reduce `top_k` parameter
- Increase `ANN_NPROBE` for better accuracy/speed balance

### 3. Slow LLM

**Symptoms:** High `llm_ms`

**Solutions:**
- Reduce `pack_top` (fewer chunks in context)
- Use faster model (smaller parameter count)
- Enable GPU acceleration

### 4. Memory Issues

**Symptoms:** OOM errors, swapping

**Solutions:**
- Reduce `CACHE_MAXSIZE`
- Use smaller embedding batch size
- Use local embeddings (smaller model)

---

## Configuration Summary

Recommended configurations by use case:

### Low Latency (Speed Priority)
```bash
DEFAULT_PACK_TOP=5
CTX_TOKEN_BUDGET=8000
ANN_NPROBE=8
CACHE_MAXSIZE=200
```

### High Quality (Accuracy Priority)
```bash
DEFAULT_PACK_TOP=12
CTX_TOKEN_BUDGET=15000
ANN_NPROBE=32
ALPHA_HYBRID=0.4
```

### Resource Constrained
```bash
EMB_BACKEND=local
EMB_BATCH_SIZE=16
CACHE_MAXSIZE=50
DEFAULT_PACK_TOP=5
```

### High Traffic
```bash
CACHE_MAXSIZE=500
CACHE_TTL=7200
RATE_LIMIT_ENABLED=true
RATE_LIMIT_REQUESTS=100
```
