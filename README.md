# Clockify RAG – Internal Support Assistant

RAG service that answers Clockify/CAKE support questions with citations. Defaults are zero-config for an internal corporate setup on Mac (VPN): Ollama at `http://10.127.0.192:11434`, chat model `qwen2.5:32b`, embeddings via Ollama `nomic-embed-text` (768-dim), corpus `clockify_help_corpus.en.md` (fallback `knowledge_full.md`).

## TL;DR – Run on a Mac (VPN on, no env vars)
- Copy/paste commands: `RUN_ON_WORK_MAC.md` (CLI + API flows, zero env vars).
- Defaults already point to the corporate Ollama + models; env vars still override if needed.

## Launch the CLI (VPN, zero env vars)
1) Clone and enter the repo  
   ```bash
   git clone https://github.com/apet97/1rag.git
   cd 1rag
   ```
2) Create/activate env (conda shown; venv also works)  
   ```bash
   conda create -n clockify-rag python=3.12 -y
   conda activate clockify-rag
   # optional ANN on macOS arm64
   conda install -c conda-forge faiss-cpu=1.8.0 -y
   ```
3) Install deps  
   ```bash
   pip install --upgrade pip
   pip install -e ".[dev]"
   ```
4) Build the index (uses `clockify_help_corpus.en.md`, falls back to `knowledge_full.md`)  
   ```bash
   python -m clockify_rag.cli_modern ingest --force
   ```
5) Ask a question  
   ```bash
   python -m clockify_rag.cli_modern query "How do I add time for others?"
   ```
6) Optional chat REPL  
   ```bash
   python -m clockify_rag.cli_modern chat
   ```
If you skip FAISS, the system falls back to BM25 + flat dense search automatically.

## Run the API (localhost)
```bash
uvicorn clockify_rag.api:app --host 0.0.0.0 --port 8000
curl -X POST http://127.0.0.1:8000/v1/query \
  -H "Content-Type: application/json" \
  -d '{"question": "How do I add time for others?", "top_k": 8}'
```

## Architecture at a glance
```mermaid
flowchart TD
    A[clockify_help_corpus.en.md] --> B[Chunker]
    A2[knowledge_full.md fallback] --> B
    B --> C[Embeddings nomic-embed-text 768d]
    C --> D[Indexes BM25 + FAISS IVFFlat / FlatIP]
    D --> E[Retriever hybrid + MMR]
    E --> F[LLM qwen2.5:32b via Ollama]
    F --> G[Answer composer + citations]
```

**What this means (plain English)**
- Start with the help docs (primary file; backup file if needed).
- Split docs into small sections so they’re easy to search.
- Turn each section into numeric “fingerprints” (embeddings) and also keep a keyword index.
- When you ask a question, search both indexes, blend the best matches, and pick the top snippets.
- Send those snippets to the AI (Qwen 2.5 on our Ollama server) to draft the answer.
- Return the answer with citations showing exactly which snippets were used.

## Commands you’ll use
- Build index: `python -m clockify_rag.cli_modern ingest --input clockify_help_corpus.en.md --force`
- CLI query: `python -m clockify_rag.cli_modern query "How do I add time for others?"`
- Chat REPL: `python -m clockify_rag.cli_modern chat`
- Doctor: `python -m clockify_rag.cli_modern doctor --json`
- API: `uvicorn clockify_rag.api:app --host 0.0.0.0 --port 8000`

Legacy CLIs (`clockify_rag/cli.py`, `clockify_support_cli_final.py`) remain for backward compatibility only; use `clockify_rag.cli_modern` for all new usage.

## Defaults (zero env required on VPN)
- `RAG_OLLAMA_URL`: `http://10.127.0.192:11434` (override for local with `http://127.0.0.1:11434`)
- `RAG_CHAT_MODEL`: `qwen2.5:32b`
- `RAG_EMBED_MODEL`: `nomic-embed-text` (768-dim)
- `EMB_BACKEND`: `ollama` (set `local` for offline dev; conftest pins local for tests)
- Corpus resolution: prefers `clockify_help_corpus.en.md`, falls back to `knowledge_full.md`
- Timeouts/retries: connect 3s, read 120s, retries 2 (VPN-friendly)
- Env vars and `.env` still override; `validate_and_set_config()` refreshes derived dims/models.

## Knowledge base & artifacts
- Ingest reads `clockify_help_corpus.en.md` front matter; resolves via `resolve_corpus_path`.
- Artifacts live beside the corpus unless `--output` is set: `chunks.jsonl`, `vecs_n.npy`, `bm25.json`, `faiss.index` (when FAISS present), `index.meta.json`.

## Testing
- Full suite: `pytest` (tests pin local embeddings; Ollama not required). Last run: all passed on Python 3.12; FAISS tests skipped unless installed.
- Smoke on VPN: `python -m clockify_rag.cli_modern ingest --force` then `python -m clockify_rag.cli_modern query "Lock timesheets"`.

## Troubleshooting
- Ollama unreachable: check VPN and `curl $RAG_OLLAMA_URL/api/tags`; override to `http://127.0.0.1:11434` if running local.
- FAISS missing on macOS arm64: install via conda (`conda install -c conda-forge faiss-cpu`); otherwise auto-falls back to flat search.
- Corpus missing: ensure `clockify_help_corpus.en.md` is in repo root or pass `--input`; `knowledge_full.md` is auto fallback.

## Docs map
- `RUN_ON_WORK_MAC.md` – copy/paste commands for Mac + VPN (zero env vars)
- `docs/CONFIGURATION.md` – env matrix and defaults
- `docs/ARCHITECTURE.md` – deeper design notes
- `docs/OPERATIONS.md` – runbook and smoke tests
- `docs/HELP_CORPUS.md` – corpus refresh/indexing details
