# API Examples

Complete examples for all Clockify RAG API endpoints.

## Base URL

```
http://localhost:8000
```

## Authentication

If API key authentication is enabled:

```bash
# Header format
-H "x-api-key: YOUR_API_KEY"
```

---

## Endpoints

### GET /health

Check system health and readiness.

**Request:**
```bash
curl http://localhost:8000/health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-11-26T10:30:00.000000",
  "version": "5.9.1",
  "platform": "Darwin arm64",
  "index_ready": true,
  "ollama_connected": true
}
```

**Status Values:**
- `healthy`: Index ready, Ollama connected
- `degraded`: Index ready, Ollama unavailable
- `unavailable`: Index not ready

---

### GET /v1/config

Get current configuration settings.

**Request:**
```bash
curl http://localhost:8000/v1/config
```

**Response:**
```json
{
  "ollama_url": "http://10.127.0.192:11434",
  "gen_model": "qwen2.5:32b",
  "emb_model": "nomic-embed-text",
  "chunk_size": 1600,
  "top_k": 15,
  "pack_top": 8,
  "threshold": 0.25
}
```

---

### POST /v1/query

Submit a question and get an answer.

**Request:**
```bash
curl -X POST http://localhost:8000/v1/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "How do I lock timesheets in Clockify?",
    "top_k": 15,
    "pack_top": 8,
    "threshold": 0.25,
    "debug": false
  }'
```

**Parameters:**
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| question | string | required | The question to answer (1-10000 chars) |
| top_k | int | 15 | Number of chunks to retrieve (1-100) |
| pack_top | int | 8 | Number of chunks to include in context (1-50) |
| threshold | float | 0.25 | Minimum similarity score (0.0-1.0) |
| debug | bool | false | Include debug information |

**Response:**
```json
{
  "question": "How do I lock timesheets in Clockify?",
  "answer": "To lock timesheets in Clockify:\n\n1. Go to Settings > Workspace settings\n2. Enable 'Lock timesheets'\n3. Set the lock date...",
  "confidence": 85.5,
  "sources": ["timesheet-locking-001", "admin-settings-042"],
  "timestamp": "2024-11-26T10:30:00.000000",
  "processing_time_ms": 1250.5,
  "refused": false,
  "metadata": {
    "reasoning": "Found direct documentation about timesheet locking",
    "sources_used": ["timesheet-locking-001"]
  },
  "routing": {
    "level": "HIGH",
    "action": "answer_autonomously"
  },
  "timing": {
    "embedding_ms": 45.2,
    "retrieval_ms": 120.8,
    "llm_ms": 1050.3
  }
}
```

**Error Responses:**

400 Bad Request:
```json
{
  "detail": "Question cannot be empty after whitespace removal"
}
```

429 Rate Limited:
```json
{
  "detail": "Rate limit exceeded. Retry after 30.00 seconds."
}
```

503 Service Unavailable:
```json
{
  "detail": "Index not ready. Run /v1/ingest first or wait for startup."
}
```

---

### POST /v1/ingest

Trigger index build/rebuild.

**Request:**
```bash
curl -X POST http://localhost:8000/v1/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "input_file": "knowledge_base",
    "force": true
  }'
```

**Parameters:**
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| input_file | string | null | Path to input markdown file or directory |
| force | bool | false | Force rebuild even if index exists |

**Response:**
```json
{
  "status": "processing",
  "message": "Index build started in background from knowledge_base",
  "timestamp": "2024-11-26T10:30:00.000000",
  "index_ready": false
}
```

**Note:** Build runs asynchronously. Check `/health` to verify completion.

---

### GET /v1/metrics

Get system metrics in various formats.

**JSON (default):**
```bash
curl http://localhost:8000/v1/metrics
```

**Response:**
```json
{
  "timestamp": 1732616400.0,
  "uptime_seconds": 3600.5,
  "counters": {
    "queries_total": 150,
    "cache_hits": 45,
    "cache_misses": 105,
    "errors_total": 2,
    "refusals_total": 10
  },
  "gauges": {
    "cache_size": 45,
    "index_size": 1250
  },
  "histograms": {
    "query_latency_ms": {
      "count": 150,
      "min": 450.5,
      "max": 3200.8,
      "mean": 1250.3,
      "p50": 1100.2,
      "p95": 2500.6,
      "p99": 3100.4
    }
  },
  "index_ready": true,
  "chunks_loaded": 1250
}
```

**Prometheus format:**
```bash
curl "http://localhost:8000/v1/metrics?format=prometheus"
# Or use standard endpoint:
curl http://localhost:8000/metrics
```

**Response:**
```
# HELP queries_total Total queries processed
# TYPE queries_total counter
queries_total 150

# HELP cache_hits Cache hit count
# TYPE cache_hits counter
cache_hits 45

# HELP query_latency_ms Query latency histogram
# TYPE query_latency_ms histogram
query_latency_ms_bucket{le="100"} 5
query_latency_ms_bucket{le="500"} 25
query_latency_ms_bucket{le="1000"} 80
query_latency_ms_bucket{le="2000"} 140
query_latency_ms_bucket{le="+Inf"} 150
query_latency_ms_sum 187545.5
query_latency_ms_count 150
```

**CSV format:**
```bash
curl "http://localhost:8000/v1/metrics?format=csv"
```

---

### GET /metrics

Standard Prometheus scraping endpoint.

**Request:**
```bash
curl http://localhost:8000/metrics
```

Equivalent to `/v1/metrics?format=prometheus`.

**Prometheus scrape config:**
```yaml
scrape_configs:
  - job_name: 'clockify-rag'
    static_configs:
      - targets: ['localhost:8000']
```

---

## Complete Examples

### Query with all parameters

```bash
curl -X POST http://localhost:8000/v1/query \
  -H "Content-Type: application/json" \
  -H "x-api-key: my-secret-key" \
  -d '{
    "question": "What are the time tracking limits for free users?",
    "top_k": 20,
    "pack_top": 10,
    "threshold": 0.20,
    "debug": true
  }' | jq .
```

### Check readiness before querying

```bash
#!/bin/bash
# Wait for service to be ready
while true; do
  status=$(curl -s http://localhost:8000/health | jq -r '.status')
  if [ "$status" = "healthy" ]; then
    echo "Service ready"
    break
  fi
  echo "Waiting for service... (status: $status)"
  sleep 2
done

# Now query
curl -X POST http://localhost:8000/v1/query \
  -H "Content-Type: application/json" \
  -d '{"question": "How do I export reports?"}'
```

### Monitor metrics in Grafana

```bash
# Continuously fetch metrics
watch -n 5 'curl -s http://localhost:8000/v1/metrics | jq ".counters"'
```

### Batch queries with jq

```bash
# Query multiple questions
for q in "How to lock timesheets?" "What is billable time?" "How to export?"; do
  echo "Q: $q"
  curl -s -X POST http://localhost:8000/v1/query \
    -H "Content-Type: application/json" \
    -d "{\"question\": \"$q\"}" | jq -r '.answer' | head -3
  echo "---"
done
```

---

## Error Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad request (invalid parameters) |
| 401 | Missing API key |
| 403 | Invalid API key |
| 404 | Resource not found (e.g., input file for ingest) |
| 429 | Rate limit exceeded |
| 500 | Internal server error |
| 503 | Service unavailable (index not ready) |
