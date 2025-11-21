# Clockify RAG Architecture

This document describes the current Retrieval-Augmented Generation (RAG) stack that powers the Clockify support assistant. Use it as the single source of truth for understanding how data moves through the system, the responsibilities of each component, and the external dependencies we rely on.

## High-Level Responsibilities

| Stage | Responsibility | Key Modules / Files |
|-------|----------------|---------------------|
| **Ingestion & Normalization** | Convert Markdown/HTML/PDF/txt/docx sources into normalized Markdown with UpdateHelpGPT front matter (or legacy `# [ARTICLE]` convention). Supports single files or entire trees. | `clockify_rag/ingestion.py`, `clockify_help_corpus.en.md`, `docs/INGESTION.md` |
| **Chunking** | Parse Markdown articles, split by headings/sentences with overlap, and emit normalized chunks with stable IDs. | `clockify_rag/chunking.py`, `CHUNKING.md` |
| **Embedding Layer** | Produce semantic vectors using local SentenceTransformers (default) or the Ollama embedding endpoint. Handles batching, retries, caching, and validation. | `clockify_rag/embedding.py`, `emb_cache.jsonl` |
| **Vector & Lexical Indexes** | Maintain FAISS IVFFlat (primary), HNSW (fallback), and BM25 sparse indexes. Persist artifacts for reuse. | `clockify_rag/indexing.py`, files under `config.FILES` |
| **Retriever & Reranker** | Execute BM25 + dense dual retrieval, reciprocal-rank fusion, intent-aware weighting, optional LLM reranking, MMR diversification, and snippet packing. | `clockify_rag/retrieval.py`, `clockify_rag/intent_classification.py` |
| **Answer Orchestration** | Drive the end-to-end `answer_once` flow: validation, caching, retrieval, reranking, prompt construction, LLM call, citation validation, and response shaping. | `clockify_rag/answer.py`, `clockify_rag/caching.py`, `clockify_rag/error_handlers.py` |
| **LLM Client Abstraction** | Unified Ollama client with retries/timeouts plus a deterministic mock used for tests/CI (`RAG_LLM_CLIENT=mock`). | `clockify_rag/api_client.py` |
| **APIs & CLIs** | Expose FastAPI endpoints, Typer-powered CLI (`ragctl`), and legacy `clockify_support_cli_final.py` wrappers for build/chat/ask flows. | `clockify_rag/api.py`, `clockify_rag/cli_modern.py`, `clockify_support_cli_final.py`, `Makefile` |
| **Observability** | Structured logging plus in-process metrics for counters, gauges, and histograms. Exporters feed CI tests and can be scraped by external collectors. | `clockify_rag/logging_config.py`, `clockify_rag/metrics.py`, `export_metrics.py`, `logs/` |
| **Evaluation** | Offline retrieval evaluation via `eval.py`, RAGAS integration hooks, and datasets under `eval_datasets/`. Supports mocked LLM mode for CI. | `eval.py`, `docs/EVALUATION.md` (to be updated) |

## Data Flow

```
           ┌───────────────────────────────────────────┐
           │  Source Docs (Markdown, HTML, PDF, etc.)  │
           └───────────────────────────────────────────┘
                                 │
                           ingest_document /
                           ingest_directory
                                 │
                                 ▼
                   Normalized Markdown corpus
                                 │
                          build_chunks()
                                 │
                           Chunk metadata
                  (written to chunks.jsonl/meta.jsonl)
                                 │
                                 ▼
       ┌─────────────── Embedding Layer ────────────────┐
       │  • Local SentenceTransformer (default)         │
       │  • Ollama `/api/embeddings` fallback           │
       └──────────────────────┬─────────────────────────┘
                              │
                       vecs_n.npy / emb_cache
                              │
                              ▼
        ┌─────────────── Index Builders ────────────────┐
        │  • FAISS IVFFlat (primary ANN)                │
        │  • HNSW (fallback ANN)                        │
        │  • BM25 sparse index                          │
        └───────────────┬───────────┬──────────────────┘
                        │           │
                        ▼           ▼
             faiss.index / hnsw_cosine.bin / bm25.json
                        │
                        ▼
             Hybrid Retriever (dense + BM25)
                        │
                Intent-aware scoring
                 + MMR diversification
                 + optional LLM rerank
                        │
                        ▼
               Context packer (token-aware)
                        │
                        ▼
          Answer orchestration + LLM prompt builder
                        │
                 Ollama `/api/chat` call
                        │
                        ▼
        JSON answer + citations + confidence routing
```

## External Services & Dependencies

- **Ollama-compatible LLM host** (default `RAG_OLLAMA_URL=http://10.127.0.192:11434`):
  - Chat/generation model: `RAG_CHAT_MODEL=qwen2.5:32b`
  - Embedding model: `RAG_EMBED_MODEL=nomic-embed-text:latest`
  - Accessible only from the company Mac (VPN required). All network clients must handle timeouts, retries, and be mockable for offline testing.
- **Local storage** for vector artifacts (FAISS/HNSW/BM25), chunk metadata, logs (`logs/`), and caches (`emb_cache.jsonl`, `rag_queries.jsonl`).
- **Python runtime** (3.11+) with optional Apple Silicon acceleration (PyTorch MPS) and FAISS wheels. Dockerfile and `docker-compose.yml` support linux/amd64 and linux/arm64 (documented in `docs/DEPLOYMENT.md`).

## Environment Assumptions

- **Development**: macOS M1 Pro laptops with VPN access to the remote Ollama host. Local runs default to mock LLM clients; setting `RAG_OLLAMA_URL` flips to the real host.
- **Production**: Linux containers (amd64) managed by the platform team. Containers mount persistent storage for indexes and expose FastAPI on port `8000`.
- **Offline/CI**: Must succeed without network access. All tests and evaluation scripts default to the mock LLM client and deterministic embeddings.

## Component Interactions

1. **Ingestion** (`ragctl ingest` or `clockify_support_cli_final.py build`) acquires a build lock, normalizes documents via `clockify_rag.ingestion`, parses them with `clockify_rag.chunking`, embeds text through `clockify_rag.embedding`, and persists indexes via `clockify_rag.indexing`.
2. **Query handling** (CLI, API, or scripts):
   - `clockify_rag.answer.answer_once` validates input, consults `clockify_rag.caching.QueryCache`, and triggers `clockify_rag.retrieval.retrieve`.
   - Retrieval loads chunk/embedding artifacts (if not already in memory), executes hybrid search, optional LLM rerank, and packs snippets.
   - `clockify_rag.retrieval.ask_llm` builds the JSON-mode instructions and calls the Ollama chat endpoint via the shared LLM client.
   - Responses flow through `clockify_rag.error_handlers` for standardized error envelopes and `clockify_rag.logging_config` for structured logs.
3. **API layer** (`clockify_rag.api`) exposes:
   - `GET /health`, `GET /v1/config`, `GET /v1/metrics`
   - `POST /v1/query` for synchronous QA
   - `POST /v1/ingest` to rebuild indexes (delegates to the same ingest pipeline)
4. **CLI** (`ragctl`) wraps the same flows with Typer commands for doctor, ingest, query, chat, and eval. Legacy scripts remain for backwards compatibility but share the config + retrieval stack.
5. **Evaluation** uses `eval.py` (MRR/P@5/NDCG) and optional RAGAS modules to benchmark retrieval quality. Datasets live under `eval_datasets/` and can be extended.

## Artifacts & Storage Layout

| Artifact | Purpose | Generated by |
|----------|---------|--------------|
| `chunks.jsonl` / `meta.jsonl` | Chunk metadata and helper fields | `clockify_rag.chunking.build_chunks` |
| `vecs_n.npy` (`float32`) | Normalized dense embeddings for chunks | `clockify_rag.embedding.embed_texts` |
| `bm25.json` | Sparse keyword index | `clockify_rag.indexing.build_bm25` |
| `faiss.index` / `hnsw_cosine.bin` | ANN indexes for dense retrieval | `clockify_rag.indexing.build_faiss_index` / HNSW helpers |
| `index.meta.json` | Versioning and checksum info | `clockify_rag.indexing.save_index_meta` |
| `rag_queries.jsonl` | Structured query logs (redaction-aware) | `clockify_rag.caching.log_query` helpers |
| `logs/` | General application logs (JSON/text) | `clockify_rag.logging_config` |

## Evaluation & Testing Surfaces

- `eval.py --dataset eval_datasets/<file>.jsonl` runs offline retrieval evaluation (defaults to lexical fallback if dense assets missing).
- `tests/` contains unit tests for chunking, embedding, retrieval, caching, metrics, CLI threading, etc. New tests must default to the mock LLM client so CI needs no network.
- `scripts/smoke.sh` (legacy) and the new smoke test (to be added) ensure end-to-end health from a developer laptop or CI runner.

## Deployment & Operations Touchpoints

- `docker-compose.yml` launches the FastAPI server plus optional local Ollama profile.
- `Dockerfile` builds a production image (multi-stage) that installs the Python package, copies artifacts, and exposes uvicorn.
- Runbooks (`docs/RUNBOOK.md`) cover health checks, log paths, rebuild steps, and how to verify connectivity to the remote Ollama host (`$RAG_OLLAMA_URL/api/tags`).
- `docs/DEPLOYMENT.md` captures platform-specific notes (Apple Silicon vs linux/amd64), environment variables, and how to swap between mocked vs real LLM clients.

Keep this document up to date when the architecture evolves (new ingestion sources, retrievers, or evaluation tooling). Changes that add new dependencies or external touchpoints must be reflected here before merging to `main`.
