# Troubleshooting Guide

Common issues and solutions for the Clockify RAG system.

## Quick Diagnostics

Run the built-in doctor command first:

```bash
python -m clockify_rag.cli_modern doctor --json
```

This checks:
- Ollama connectivity
- Index file presence
- Embedding backend availability
- Configuration validity

---

## Connection Issues

### Ollama Connection Timeout

**Symptoms:**
- `Connection refused` or `timeout` errors
- `LLMUnavailableError` exceptions
- Slow or hanging queries

**Causes:**
1. Ollama server not running
2. Wrong Ollama URL configured
3. VPN not connected (for corporate Ollama)
4. Firewall blocking connection

**Solutions:**

```bash
# 1. Check if Ollama is running
curl http://10.127.0.192:11434/api/tags  # Corporate VPN
curl http://127.0.0.1:11434/api/tags      # Local

# 2. Verify configuration
echo $RAG_OLLAMA_URL

# 3. Test with explicit URL
RAG_OLLAMA_URL=http://127.0.0.1:11434 python -m clockify_rag.cli_modern doctor

# 4. For corporate VPN, verify VPN connection
ping 10.127.0.192

# 5. Start local Ollama if needed
ollama serve
```

### Connection Pooling Exhaustion

**Symptoms:**
- Intermittent timeouts under load
- `Too many open connections` errors

**Solutions:**
- Increase connection pool size via environment variables
- Restart the service to reset connections

---

## FAISS Index Issues

### FAISS Not Available on M1 Mac

**Symptoms:**
- `ImportError: No module named 'faiss'`
- Fallback to linear search messages in logs

**Solution:**
Install FAISS via conda (pip wheels don't work on Apple Silicon):

```bash
# Create or activate conda environment
conda create -n rag-env python=3.12
conda activate rag-env

# Install FAISS
conda install -c conda-forge faiss-cpu

# Verify installation
python -c "import faiss; print(faiss.IndexFlatIP(768))"
```

### FAISS Dimension Mismatch

**Symptoms:**
- `Dimension mismatch: stored=384, expected=768`
- FAISS falling back to linear search

**Cause:**
Switching embedding backends without rebuilding the index.

**Solution:**
Rebuild the index with the current backend:

```bash
python -m clockify_rag.cli_modern ingest --force
```

### Stale FAISS Index

**Symptoms:**
- Index not reflecting recent corpus changes
- Old answers from deleted articles

**Solution:**

```bash
# Force rebuild
python -m clockify_rag.cli_modern ingest --force

# Or delete and rebuild
rm -f faiss.index chunks.jsonl vecs_n.npy bm25.json meta.jsonl
python -m clockify_rag.cli_modern ingest
```

---

## Cache Issues

### Query Cache Not Working

**Symptoms:**
- High latency on repeated queries
- Cache hit rate near 0%

**Diagnosis:**

```bash
# Check cache stats via API
curl http://localhost:8000/v1/metrics | jq '.cache_hits, .cache_misses'
```

**Solutions:**

1. Verify cache is enabled:
   ```bash
   echo $RAG_CACHE_ENABLED  # Should be empty or "true"
   ```

2. Check cache size:
   ```bash
   # Default is 100 queries, 1 hour TTL
   echo $CACHE_MAXSIZE
   echo $CACHE_TTL
   ```

3. Clear cache if corrupted:
   ```bash
   rm -f query_cache.json
   ```

### Excessive Disk Usage from Query Logs

**Symptoms:**
- `rag_queries.jsonl` growing unbounded
- Disk space warnings

**Solution:**
Query logs now use rotation (10MB max, 5 backups). For old installations:

```bash
# Clean up old logs manually
rm -f rag_queries.jsonl.old.*

# Or archive them
gzip rag_queries.jsonl.1 rag_queries.jsonl.2
```

---

## Index Build Issues

### Build Lock Stuck

**Symptoms:**
- `Build already in progress; timed out waiting for lock release`
- Build hangs indefinitely

**Cause:**
Previous build crashed without cleaning up lock file.

**Solution:**

```bash
# Check and remove stale lock
cat .build.lock  # Shows PID and timestamp
rm .build.lock   # Remove if PID is dead

# Or wait for automatic cleanup (15 minute TTL)
```

### Out of Memory During Indexing

**Symptoms:**
- `MemoryError` during embedding computation
- System becoming unresponsive

**Solutions:**

1. Reduce batch size:
   ```bash
   EMB_BATCH_SIZE=16 python -m clockify_rag.cli_modern ingest
   ```

2. Use local embeddings (smaller model):
   ```bash
   EMB_BACKEND=local python -m clockify_rag.cli_modern ingest
   ```

3. Process in smaller chunks by splitting corpus

### Embedding Dimension Errors

**Symptoms:**
- `BuildError: Cached embedding has dimension X, expected Y`
- Mixed dimension arrays

**Solution:**
Clear embedding cache and rebuild:

```bash
rm -f emb_cache.jsonl
python -m clockify_rag.cli_modern ingest --force
```

---

## API Issues

### 503 Service Unavailable

**Symptoms:**
- `/v1/query` returns 503
- "Index not ready" error

**Solutions:**

1. Wait for startup index load (check `/health`)
2. Trigger manual ingest:
   ```bash
   curl -X POST http://localhost:8000/v1/ingest
   ```
3. Check index files exist:
   ```bash
   ls -la chunks.jsonl vecs_n.npy bm25.json meta.jsonl
   ```

### 429 Rate Limited

**Symptoms:**
- `Rate limit exceeded` errors
- Requests rejected

**Solutions:**

1. Wait the specified retry time
2. Increase rate limit:
   ```bash
   RATE_LIMIT_REQUESTS=100 RATE_LIMIT_WINDOW=60 python -m clockify_rag.api
   ```
3. Disable rate limiting (dev only):
   ```bash
   RATE_LIMIT_ENABLED=false python -m clockify_rag.api
   ```

### Slow Query Performance

**Symptoms:**
- Queries taking > 5 seconds
- High latency in `/v1/metrics`

**Diagnosis:**

```bash
curl http://localhost:8000/v1/metrics | jq '.query_latency_ms'
```

**Solutions:**

1. Enable FAISS if not using:
   ```bash
   USE_ANN=faiss python -m clockify_rag.cli_modern ingest --force
   ```

2. Reduce pack_top for faster responses:
   ```bash
   DEFAULT_PACK_TOP=5 python -m clockify_rag.api
   ```

3. Check Ollama latency:
   ```bash
   time curl -X POST http://10.127.0.192:11434/api/generate \
     -d '{"model":"qwen2.5:32b","prompt":"Hi"}'
   ```

---

## LLM Issues

### Refusal Responses ("I don't know")

**Symptoms:**
- All queries return "I don't know based on the MD"
- Low confidence scores (< 40)

**Causes:**
1. Query not matching corpus content
2. Retrieval threshold too high
3. Insufficient context in corpus

**Solutions:**

1. Lower similarity threshold:
   ```bash
   DEFAULT_THRESHOLD=0.15 python -m clockify_rag.cli_modern query "..."
   ```

2. Check corpus coverage:
   ```bash
   # Search corpus directly
   grep -i "your topic" knowledge_base/*.md
   ```

3. Increase context window:
   ```bash
   DEFAULT_PACK_TOP=10 python -m clockify_rag.cli_modern query "..."
   ```

### JSON Parse Errors in LLM Response

**Symptoms:**
- `JSONDecodeError` in logs
- Malformed answer structure

**Cause:**
LLM not following JSON output format.

**Solution:**
Automatic retry handles most cases. If persistent:

1. Check model is correct:
   ```bash
   echo $RAG_CHAT_MODEL  # Should be qwen2.5:32b
   ```

2. Increase retries:
   ```bash
   DEFAULT_RETRIES=3 python -m clockify_rag.cli_modern query "..."
   ```

---

## Environment Issues

### Python Version Incompatibility

**Symptoms:**
- Import errors
- Syntax errors

**Requirements:**
- Python 3.11, 3.12, or 3.13
- Python 3.14+ not supported

**Check:**

```bash
python --version  # Must be 3.11.x - 3.13.x
```

### Missing Dependencies

**Symptoms:**
- `ModuleNotFoundError`
- Import failures

**Solution:**

```bash
pip install -e ".[dev]"

# Or for specific features:
pip install -e ".[embeddings]"  # Local embeddings
pip install -e ".[eval]"        # RAGAS evaluation
```

---

## Getting Help

If issues persist:

1. **Check logs** with DEBUG level:
   ```bash
   RAG_LOG_LEVEL=DEBUG python -m clockify_rag.cli_modern query "test"
   ```

2. **Run full diagnostics:**
   ```bash
   python -m clockify_rag.cli_modern doctor --json > diagnostics.json
   ```

3. **Verify test suite passes:**
   ```bash
   pytest -q tests/
   ```

4. **Report issues** with:
   - Python version
   - Platform (macOS/Linux)
   - Full error traceback
   - Output of `doctor --json`
