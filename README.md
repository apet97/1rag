# Clockify RAG – Internal Support Assistant

RAG service that answers Clockify/CAKE support questions from the internal help corpus. Uses **Qwen 2.5 (32B) via internal Ollama** plus hybrid BM25 + FAISS retrieval and answer validation with citations.

## What it does
- Clockify/CAKE help-center assistant with citations and refusal on missing context.
- Hybrid retrieval (BM25 + FAISS + MMR) with intent-aware blending and token-budgeted context packing.
- Remote-first Ollama (Qwen + nomic-embed-text); local dev works on M1 Pro without external APIs.
- FastAPI API + Typer CLI (`clockify_rag.cli_modern`) for ingest/query/chat/demo.
- Deterministic ingestion and build locks to keep artifacts consistent across environments.

## MacBook Pro (Apple Silicon, M1 Pro) Quickstart

Two options, both tested on arm64:

### A) Conda-first (easiest, includes FAISS)
1) Install Miniconda (arm64):  
   ```bash
   curl -fsSL https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o miniconda.sh
   bash miniconda.sh
   conda init zsh  # then restart shell
   ```
2) Create env with Python 3.12 and core deps (FAISS included):  
   ```bash
   conda create -n clockify-rag python=3.12 -y
   conda activate clockify-rag
   conda install -c conda-forge faiss-cpu=1.8.0 numpy pandas pytest ruff black -y
   ```
3) Clone and install the project (pip inside the conda env):  
   ```bash
   git clone git@github.com:apet97/1rag.git
   cd 1rag
   pip install --upgrade pip
   pip install -e ".[dev]"
   ```
4) Put the corpus in place:  
   ```bash
   cp /path/to/clockify_help_corpus.en.md .
   # falls back to knowledge_full.md if missing
   ```
5) Build index (uses FAISS if present, BM25 otherwise):  
   ```bash
   python -m clockify_rag.cli_modern ingest --input clockify_help_corpus.en.md
   ```
6) Smoke test offline (mock LLM):  
   ```bash
   RAG_LLM_CLIENT=mock python -m pytest tests/test_api_query.py tests/test_qwen_contract.py -q
   ```
7) Run the API:  
   ```bash
   uvicorn clockify_rag.api:app --reload
   curl -X POST http://127.0.0.1:8000/v1/query \
     -H "Content-Type: application/json" \
     -d '{"question": "How do I lock timesheets?", "top_k": 8}'
   ```

### B) Pure venv (BM25-only unless you add FAISS)
1) Python 3.12 (3.11–3.13 supported). On macOS: `pyenv install 3.12.12`
2) Create venv and install deps:  
   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -e ".[dev]"
   ```
3) Place corpus, ingest, smoke-test, run API (same as steps 4–7 above).

Offline defaults: set `RAG_LLM_CLIENT=mock` and keep `EMB_BACKEND=local` (default) to avoid VPN/Ollama. FAISS is optional; without it, BM25-only retrieval still works. 

Rerank and CORS knobs:
- `RERANK_MODEL` to use a lighter model for reranking (falls back to `RAG_CHAT_MODEL`).
- `RERANK_READ_TIMEOUT` to cap rerank latency (default 180s).
- `ALLOWED_ORIGINS` (comma-separated) to enable CORS; omit to keep CORS off by default.

**Notes:**
- Default Ollama endpoint: `http://10.127.0.192:11434` (override via `RAG_OLLAMA_URL` or use `http://127.0.0.1:11434` for local dev).
- Embeddings default to Ollama; set `EMB_BACKEND=local` only if you need an offline fallback.
- See [docs/INSTALL_macOS_ARM64.md](docs/INSTALL_macOS_ARM64.md) for deeper M1 tuning and troubleshooting.

## Quickstart — internal deployment (VPN + internal Ollama/Qwen)
```bash
export RAG_OLLAMA_URL=http://<internal-ollama-host>:11434   # on VPN
export RAG_CHAT_MODEL=qwen2.5:32b
export RAG_EMBED_MODEL=nomic-embed-text:latest
export EMB_BACKEND=ollama                                  # remote embeddings

# Build or refresh the index from the help corpus
python -m clockify_rag.cli_modern ingest --input clockify_help_corpus.en.md --force

# Run API
uvicorn clockify_rag.api:app --host 0.0.0.0 --port 8000
# or chat via CLI
python -m clockify_rag.cli_modern chat
```
Artifacts: `chunks.jsonl`, `vecs_n.npy`, `bm25.json`, `faiss.index` (when FAISS is available), and `index.meta.json` sit beside the repo.

## Architecture
- Clients (CLI/API) sanitize inputs, enforce query limits, and route to retrieval.
- Retrieval blends BM25 + dense (FAISS/linear) with MMR diversification and section-aware packing.
- Context (12K tokens) is sent to Ollama Qwen 2.5 with the JSON-only prompt contract.
- Answer composer validates citations, confidence, and contract, then returns JSON to clients.

## Pipeline summary
- **Ingestion**: `clockify_help_corpus.en.md` (falls back to `knowledge_full.md`) → `clockify_rag.chunking.build_chunks` → `clockify_rag.embedding` (local or Ollama) → `clockify_rag.indexing.build` writes BM25 + FAISS + metadata.
- **Online query**: question → sanitize/length guard → embed → hybrid BM25+dense → MMR diversification → pack to 12K-token budget → `clockify_rag.llm_client` (ChatOllama/Qwen) → citations + confidence routing in `clockify_rag.answer`.

## Key components
- `clockify_rag/config.py` – configuration defaults, env parsing, model selection.
- `clockify_rag/retrieval.py` – hybrid retrieval, MMR, packing, rerank hooks.
- `clockify_rag/answer.py` – orchestration, refusal, citation validation.
- `clockify_rag/embedding.py` & `clockify_rag/embeddings_client.py` – local vs Ollama embeddings.
- `clockify_rag/indexing.py` – chunking, embedding, BM25/FAISS build + lock handling.
- `clockify_rag/cli_modern.py` – Typer CLI (`ingest`, `query`, `chat`, `doctor`).
- `clockify_rag/api.py` – FastAPI service surface.
- `clockify_rag/sanity_check.py` – connectivity and end-to-end probe.
- Helpers: `scripts/generate_chunk_title_map.py` (chunk lookup), `scripts/build_faq_cache.py` (optional cache).

## Configuration (high level)
- **Ollama host/model**: `RAG_OLLAMA_URL`, `RAG_CHAT_MODEL`, `RAG_EMBED_MODEL`.
- **Embedding backend**: `EMB_BACKEND=ollama` (production) or `local` (offline dev, default).
- **Retrieval**: `DEFAULT_TOP_K` (15), `DEFAULT_PACK_TOP` (8), `DEFAULT_THRESHOLD` (0.25), `ALPHA` (0.5), `MMR_LAMBDA` (0.75).
- **Budgets**: `CTX_BUDGET=12000`, `DEFAULT_NUM_CTX=32768`, `DEFAULT_NUM_PREDICT=512`.
- **Timeouts**: `CHAT_CONNECT_TIMEOUT`, `CHAT_READ_TIMEOUT`, `EMB_CONNECT_TIMEOUT`, `EMB_READ_TIMEOUT`, `DEFAULT_RETRIES`.
- See `docs/CONFIGURATION.md` for the full matrix and sample `.env` snippets for VPN vs local.

## Testing & CI
- Fast checks: `python -m clockify_rag.sanity_check`
- Unit/integration: `pytest -q`
- Smoke (mock LLM by default): `make smoke` or `python scripts/smoke_rag.py`
- CI runs lint/format/tests; keep docs updated when behavior changes.

## 5-minute demo script
1) Ensure `clockify_help_corpus.en.md` is present (or `knowledge_full.md` for legacy exports).
2) Build artifacts: `python -m clockify_rag.cli_modern ingest --input clockify_help_corpus.en.md --force`.
3) Start chat: `python -m clockify_rag.cli_modern chat` (or run `uvicorn clockify_rag.api:app` and POST to `/v1/query`).
4) Ask a few live questions:
   - “Add time for others”
   - “Lock timesheets”
   - “Manage overtime limits”
5) Show observability:
   - Tail `rag_queries.jsonl` if logging enabled.
   - `GET /v1/metrics` when API is running.
   - Point out citations in responses.

## Troubleshooting (common)
- **Ollama unreachable**: verify VPN and `curl $RAG_OLLAMA_URL/api/tags`; fall back to local with `RAG_OLLAMA_URL=http://127.0.0.1:11434` and `EMB_BACKEND=local`.
- **Missing corpus**: ensure `clockify_help_corpus.en.md` is in repo root or pass `--input` to `ingest`; CI uses the sample corpus to stay offline.
- **Offline/mock mode**: set `RAG_LLM_CLIENT=mock` (and optionally `EMB_BACKEND=local`) to run pytest, CLI, or API without VPN.
- **FAISS missing on M1**: `conda install -c conda-forge faiss-cpu=1.8.0`; system falls back to linear search if absent.
- **Python 3.14**: blocked at import time; use 3.11–3.13.
- **Index drift**: delete artifacts and rebuild: `rm -f chunks.jsonl vecs_n.npy bm25.json faiss.index index.meta.json && python -m clockify_rag.cli_modern ingest --input clockify_help_corpus.en.md`.
- **Switching from legacy `knowledge_full.md`**: remove old artifacts before rebuilding with the new `clockify_help_corpus.en.md` to avoid mixing data (`rm -f chunks.jsonl vecs_n.npy bm25.json faiss.index index.meta.json` then ingest).

## Docs to read next
- `docs/ARCHITECTURE.md` – deeper dive + diagrams.
- `docs/CONFIGURATION.md` – env knobs for VPN vs local.
- `docs/HELP_CORPUS.md` – how the help corpus is refreshed and indexed.
- `docs/OPERATIONS.md` – runbook for smoke tests and deployments.
