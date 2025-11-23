# RAG System Data Flow

This document explains the complete data flow through the Clockify RAG system, from knowledge ingestion to answer generation.

## Overview

The RAG system processes user questions through a multi-stage pipeline combining keyword search (BM25), semantic search (dense embeddings), and LLM-based answer generation.

## Visual Data Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    INGESTION PHASE (Offline)                     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────┐
│ Knowledge Base  │  clockify_help_corpus.en.md (UpdateHelpGPT export; falls back to knowledge_full.md)
│   (Markdown)    │  ~150 pages of documentation
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Chunking     │  chunking.py: split_md_by_headings()
│  ## Headings    │  • Split by second-level headings (##)
│                 │  • Max 1600 chars per chunk
│                 │  • Overlap: 200 chars for continuity
│                 │  • Result: ~500 chunks
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Embedding     │  indexing.py: build_faiss() + build_bm25()
│ nomic-embed-text│  • Model: nomic-embed-text via Ollama
│                 │  • Dimensions: 768-dim vectors
│                 │  • Normalization: L2-normalized for cosine similarity
│                 │  • BM25: keyword index for sparse retrieval
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Storage      │  File artifacts in project root:
│  Index Files    │  • vecs_n.npy - NumPy array [N x 768] float32
│                 │  • chunks.jsonl - Text content (JSONL format)
│                 │  • meta.jsonl - Metadata (IDs, titles, context)
│                 │  • bm25.json - BM25 index (pickled)
│                 │  • hnsw_cosine.bin - HNSW index (optional, fast)
│                 │  • index.meta.json - Build metadata + MD5 hash
└─────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    QUERY PHASE (Online/Runtime)                  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────┐
│  User Query     │  "How do I track time in Clockify?"
│  (Text Input)   │  • API: POST /v1/query {"question": "..."}
│                 │  • CLI: python -m clockify_rag.cli_modern query "..."
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Sanitization   │  utils.py: sanitize_question()
│  & Validation   │  • Strip excessive whitespace
│                 │  • Block XSS patterns (<script>, javascript:, eval)
│                 │  • Reject non-printable characters
│                 │  • Length limit: enforced via MAX_QUERY_LENGTH (default 1,000,000 chars; CLI/UX may set lower)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Query Embed    │  embedding.py: embed_query()
│  nomic-embed    │  • Same model as ingestion (consistency)
│                 │  • Returns 768-dim vector (normalized)
│                 │  • Caching: None (queries are unique)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Retrieval     │  retrieval.py: retrieve_hybrid()
│  Hybrid Search  │  • Balanced BM25 + dense (intent-aware alpha)
│                 │  • Top-K: 15 candidates retrieved
│                 │  • MMR: Maximal Marginal Relevance (λ=0.75)
│                 │    - Diversifies results (avoid redundancy)
│                 │    - Balances relevance vs diversity
│                 │  • Coverage Check: ≥2 chunks with score ≥ threshold
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Reranking &   │  retrieval.py: pack_snippets()
│  Token Budget   │  • Sort by hybrid score (BM25 + dense)
│                 │  • Pack top 8 chunks (DEFAULT_PACK_TOP)
│                 │  • Token budget: 60% of num_ctx (~7,200 tokens)
│                 │  • Reserve 40% for system prompt + generation
│                 │  • Truncation: Ellipsis if chunk exceeds budget
│                 │  • Result: Packed context with [id_123] citations
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Context Format │  answer.py: format_context()
│  with Citations │  Example output:
│                 │  ```
│                 │  [id_42] ## Time Tracking Methods
│                 │  You can track time in three ways:
│                 │  1. Manual entry...
│                 │
│                 │  [id_87] ## Starting a Timer
│                 │  Click the green "Start" button...
│                 │  ```
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   LLM Call      │  api_client.py: ask_llm()
│ qwen2.5:32b     │  • Model: qwen2.5:32b (32k context window)
│                 │  • Temperature: 0.0 (deterministic)
│                 │  • System prompt: "Answer using only provided docs"
│                 │  • Timeout: 120s read, 3s connect (configurable)
│                 │  • Retry: Max 1 retry on transient failures
│                 │  • Input: system prompt + packed context + question
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Answer Extract │  answer.py: answer_once()
│  & Validation   │  • Extract LLM response
│                 │  • **Citation Validation**:
│                 │    - Verify [id_123] citations exist in packed context
│                 │    - Remove fake/hallucinated citations
│                 │  • **Confidence Scoring**:
│                 │    - High: Multiple citations, detailed answer
│                 │    - Low: Vague or single-citation answers
│                 │  • **Refusal Detection**:
│                 │    - Detects: "I don't know based on the MD."
│                 │    - Sets refused=True flag
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Confidence      │  confidence_routing.py: get_routing_action()
│    Routing      │  • Confidence < 40: Escalate to human
│   (Optional)    │  • Refused answers: Escalate or augment KB
│                 │  • High confidence: Return immediately
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Response      │  QueryResponse (Pydantic model)
│  to Client      │  • answer: str (LLM-generated text)
│                 │  • sources: List[str] (e.g., ["id_42", "id_87"])
│                 │  • confidence: float (0-100)
│                 │  • refused: bool (True if "I don't know")
│                 │  • routing: Dict (escalation recommendation)
│                 │  • timing: Dict (latency breakdown in ms)
│                 │  • metadata: Dict (debug info, if requested)
└─────────────────┘
```

## Detailed Component Descriptions

### 1. Knowledge Base Ingestion

**File**: `clockify_help_corpus.en.md` (legacy: `knowledge_full.md`)
**Size**: ~6.9 MB (150 pages)
**Format**: Markdown with hierarchical headings

The knowledge base is ingested once (or when updated) using:
```bash
ragctl ingest clockify_help_corpus.en.md
```

### 2. Chunking Strategy

**Module**: `clockify_rag/chunking.py`
**Function**: `split_md_by_headings()`

**Rules**:
- Split on second-level Markdown headings (`##`)
- Maximum chunk size: 1600 characters
- Overlap: 200 characters (for continuity at boundaries)
- Preserves heading hierarchy for context

**Example**:
```markdown
## Time Tracking Methods

You can track time in three ways:
1. Manual entry
2. Timer
3. Calendar integration

### Manual Entry
Enter start and end times directly...
```

Becomes chunk:
```
id: 42
title: "Time Tracking Methods"
text: "## Time Tracking Methods\n\nYou can track time in three ways:\n1. Manual entry\n..."
```

### 3. Embedding Generation

**Module**: `clockify_rag/indexing.py`
**Model**: `nomic-embed-text` (768 dimensions)

**Process**:
1. Send chunk text to Ollama API
2. Receive 768-dim embedding vector
3. L2-normalize for cosine similarity
4. Store in `vecs_n.npy` (NumPy memmap for efficiency)

**Why nomic-embed-text?**
- Open-source and fast
- Strong performance on retrieval tasks
- 768-dim is a good balance (quality vs speed)
- Works well with Ollama

### 4. Storage Format

**Files Generated**:
- `vecs_n.npy`: Float32 array [N_chunks × 768]
- `chunks.jsonl`: One JSON object per line `{"id": int, "text": str}`
- `meta.jsonl`: Metadata `{"id": int, "title": str, "context": str}`
- `bm25.json`: Pickled BM25 index from `rank_bm25`
- `hnsw_cosine.bin`: HNSW index (optional, faster than brute-force)
- `index.meta.json`: Build timestamp + MD5 hash of source

### 5. Query Processing

**Entry Points**:
- API: `POST /v1/query` (FastAPI endpoint)
- CLI: `ragctl ask "question"`

**Sanitization** (`utils.py:sanitize_question()`):
- Prevents XSS: blocks `<script>`, `javascript:`, `eval()`
- Strips excessive whitespace
- Validates printable characters only
- Enforces length limits (1-10,000 chars)

### 6. Hybrid Retrieval

**Module**: `clockify_rag/retrieval.py`
**Function**: `retrieve_hybrid()`

**Two-Stage Retrieval**:

**Stage 1: Parallel Retrieval**
- **BM25 (Sparse)**: Keyword matching
  - Scores based on term frequency + inverse document frequency
  - Good for exact term matches (e.g., "SSO", "API key")
  - Weight: 30% of final score

- **Dense (Semantic)**: Cosine similarity
  - Scores based on embedding similarity
  - Good for semantic/paraphrased queries
  - Weight: 70% of final score

**Stage 2: Fusion + Reranking**
- Combine BM25 and dense scores (weighted average)
- Apply MMR (Maximal Marginal Relevance):
  - λ=0.75: Balance relevance (75%) vs diversity (25%)
  - Prevents retrieving 10 nearly-identical chunks
  - Diversifies information in final context

**Stage 3: Coverage Check**
- Require ≥2 chunks with score ≥ threshold (default: 0.25)
- If insufficient coverage → refuse to answer
- Prevents low-confidence hallucinations

### 7. Token Budget Management

**Module**: `clockify_rag/retrieval.py`
**Function**: `pack_snippets()`

**Budget Allocation**:
- Total context window: `num_ctx` (e.g., 32k tokens for qwen2.5:32b)
- Context budget: 60% of `num_ctx` (~19k tokens)
- Reserved: 40% for system prompt + answer generation (~13k tokens)

**Packing Strategy**:
1. Always include top-1 chunk (highest relevance)
2. Add chunks 2-N until budget exhausted
3. If chunk exceeds remaining budget → truncate with ellipsis
4. Format: `[id_N] {title}\n{text}\n\n`

### 8. LLM Answer Generation

**Module**: `clockify_rag/api_client.py`
**Function**: `ask_llm()`

**Configuration**:
- Model: `qwen2.5:32b` (configurable via `RAG_CHAT_MODEL`)
- Temperature: 0.0 (deterministic)
- Timeout: 180s read, 3s connect
- Retry: Max 1 retry with 0.5s backoff

**System Prompt** (simplified):
```
You are a Clockify documentation assistant.

RULES:
1. Answer ONLY using the provided documentation snippets below
2. Cite sources using [id_N] format
3. If information is not in the snippets, respond: "I don't know based on the MD."
4. Be concise and accurate

DOCUMENTATION:
{packed_context}

USER QUESTION: {question}
```

### 9. Answer Validation & Routing

**Citation Validation** (`answer.py`):
- Extract all `[id_N]` citations from LLM response
- Verify each ID exists in `packed_ids` (context actually sent to LLM)
- Remove hallucinated citations (fake IDs)

**Confidence Scoring** (`answer.py:calculate_confidence()`):
- Factors:
  - Number of citations (more = higher confidence)
  - Answer length (too short = low confidence)
  - Keyword presence (e.g., "I don't know" = low)
- Range: 0-100

**Routing** (`confidence_routing.py`):
- Confidence < 40 → Escalate to human support
- Refused answer → Suggest KB augmentation
- High confidence → Return to user immediately

## Performance Characteristics

### Latency Breakdown (Typical)

| Stage | Time | % of Total |
|-------|------|------------|
| Query embedding | 50-100ms | 5-10% |
| BM25 retrieval | 10-20ms | 1-2% |
| Dense retrieval | 30-50ms | 3-5% |
| MMR reranking | 5-10ms | <1% |
| **LLM generation** | **800-1500ms** | **80-90%** |
| Citation validation | 1-5ms | <1% |
| **Total** | **~1000ms** | **100%** |

**Bottleneck**: LLM generation dominates latency (80-90% of total time).

### Throughput

- **Sequential**: ~1 query/second (limited by LLM)
- **Concurrent** (with threading): ~4-8 queries/second (depends on CPU cores)
- **Async** (with `async_support.py`): ~10-15 queries/second

### Memory Usage

- **Index loading**: ~500 MB (vectors + BM25 + HNSW)
- **Per query**: ~10-20 MB (transient, for context packing)
- **LLM**: Managed by Ollama (separate process)

## Error Handling

### Common Failure Modes

1. **Ollama Unavailable**:
   - Detection: Connection refused on `http://127.0.0.1:11434`
   - Handling: Return 503 Service Unavailable
   - Mitigation: Health check endpoint monitors Ollama

2. **Index Not Ready**:
   - Detection: `app.state.index_ready == False`
   - Handling: Return 503 with message "Run /v1/ingest first"
   - Mitigation: Startup loads index automatically

3. **Low Coverage**:
   - Detection: `coverage_ok()` returns False (<2 chunks with score ≥ threshold)
   - Handling: Return refused answer ("I don't know based on the MD.")
   - Mitigation: Lower threshold or improve KB coverage

4. **LLM Timeout**:
   - Detection: Read timeout after 180s
   - Handling: Retry once, then return error
   - Mitigation: Increase `CHAT_READ_TIMEOUT` env var

5. **Concurrent State Update**:
   - Detection: Race condition during `/v1/ingest` + `/v1/query`
   - Handling: `threading.RLock()` ensures atomic state snapshots
   - Mitigation: Lock added in v5.9 (api.py:_state_lock)

## Configuration & Tuning

### Key Environment Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `RAG_OLLAMA_URL` | `http://127.0.0.1:11434` | Ollama API endpoint |
| `RAG_CHAT_MODEL` | `qwen2.5:32b` | LLM model for generation |
| `RAG_EMBED_MODEL` | `nomic-embed-text` | Embedding model |
| `DEFAULT_TOP_K` | 15 | Candidates to retrieve |
| `DEFAULT_PACK_TOP` | 8 | Chunks to pack into context |
| `DEFAULT_THRESHOLD` | 0.25 | Minimum similarity score |
| `MMR_LAMBDA` | 0.75 | Relevance vs diversity balance |
| `CTX_TOKEN_BUDGET` | 12000 | Token budget for context |

### Tuning Tips

**For Higher Accuracy**:
- Increase `DEFAULT_TOP_K` (retrieve more candidates)
- Increase `DEFAULT_PACK_TOP` (use more context)
- Lower `DEFAULT_THRESHOLD` (accept lower-scoring chunks)

**For Lower Latency**:
- Decrease `DEFAULT_TOP_K` (fewer candidates)
- Decrease `DEFAULT_PACK_TOP` (smaller context)
- Use smaller LLM model (e.g., `qwen2.5:7b`)

**For Better Diversity**:
- Increase `MMR_LAMBDA` (favor diversity over pure relevance)
- Increase `DEFAULT_PACK_TOP` (include more varied chunks)

## Related Documentation

- [ARCHITECTURE.md](ARCHITECTURE.md) - System architecture overview
- [THREAD_SAFETY.md](THREAD_SAFETY.md) - Concurrency guarantees
- [ASYNC_GUIDE.md](ASYNC_GUIDE.md) - Async usage patterns
- [DEPLOYMENT.md](DEPLOYMENT.md) - Multi-worker deployment
- [CONFIG.md](CONFIG.md) - Complete configuration reference

## Version History

- **v5.9**: Added confidence routing, async support, thread safety
- **v5.1**: Thread safety locks for multi-worker deployment
- **v2.0**: Hybrid retrieval (BM25 + dense + MMR)
- **v1.0**: Simple cosine similarity retrieval
