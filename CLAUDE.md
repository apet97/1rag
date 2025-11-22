# Claude Code Guide

This repo hosts **Clockify RAG** (FastAPI + Typer CLI) for Clockify/CAKE internal support. Use this as the contract for any Claude Code (Sonnet 4.5) sessions.

## Project snapshot (work laptop constraints)
- This laptop can edit the repo but cannot validate remote services directly; you’ll need to rely on local commands and push to GitHub for CI.
- Language: Python 3.11–3.13 (3.14+ blocked).
- Default stack: FastAPI API (`clockify_rag/api.py`), Typer CLI (`clockify_rag/cli_modern.py`), hybrid retrieval (`clockify_rag/retrieval.py`), ingestion/indexing (`clockify_rag/indexing.py`), embeddings/LLM via Ollama.
- Default endpoints/models: `RAG_OLLAMA_URL=http://10.127.0.192:11434`, chat model `qwen2.5:32b`, embed model `nomic-embed-text:latest`, `EMB_BACKEND=ollama` (tests pin to local embeddings).
- Tests: pytest under `tests/` (many skips if FAISS/torch absent on arm64).

## How to run locally
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -q            # full suite (fast; skips FAISS/rate limiter tests as needed)
black clockify_rag   # formatting
ruff check clockify_rag tests
```
For ingestion/query (requires corpus file and Ollama):
```bash
python -m clockify_rag.cli_modern ingest --input clockify_help_corpus.en.md
python -m clockify_rag.cli_modern query "How do I lock timesheets?"
```

## Session rules for Claude Code
1) **Role**: senior reviewer/implementer. Prefer small, safe diffs; propose a short plan before edits. Keep changes PR-sized.
2) **Scope discipline**: Work in tight loops (inspect -> suggest -> edit -> test). Do not refactor unrelated modules.
3) **Testing**: Run `pytest -q` after behavior changes. Use `ruff`/`black` if formatting/lint is touched. If a command cannot be run locally due to host limits, note it and rely on GH CI.
4) **Risk controls**: Avoid infra/CI changes unless asked. Do not touch auth/CI/secrets. Keep defaults intact unless explicitly requested.
5) **Output expectations**: Summaries first, then findings with file:line refs, then concrete actions. Include “how to verify” for risky changes.

### If asked to do a repo-wide issue/improvement sweep
- First, read the docs (README, docs/ARCHITECTURE.md, docs/CONFIGURATION.md, AGENTS/CLAUDE if present) and map the code layout (core modules, tests, workflows).
- Build an architectural summary: components, data flow, hotspots.
- Identify findings with severity (High/Med/Low) and concrete suggestions (file + line). Focus on correctness, perf (especially retrieval/indexing), and DX.
- Validate locally where possible (`pytest -q`, `ruff`, `black`); if something can’t run locally, flag it for GH CI.

## Hotspots / priorities
- Retrieval pipeline: BM25/dense/MMR, pack_snippets budgeting, rerank fallbacks (`clockify_rag/retrieval.py`).
|- Answer orchestration and citation validation (`clockify_rag/answer.py`).
|- Embedding backends and FAISS fallback on M1 (`clockify_rag/embedding.py`, `clockify_rag/indexing.py`, `embeddings_client.py`).
|- API/CLI consistency and thread safety (`clockify_rag/api.py`, `clockify_rag/cli_modern.py`, `clockify_rag/cli.py`).
|- Logging/metrics toggles (`caching.py`, `logging_utils.py`, `metrics.py`).

## Quick repo map
- Core: `clockify_rag/` (config, api, cli_modern, retrieval, answer, indexing, embedding, embeddings_client, llm_client, caching, utils, prompts, intent_classification, confidence_routing).
- Tests: `tests/` (broad coverage; conftest forces local embeddings to avoid network).
- Docs: `docs/` (architecture, operations, configuration, etc.).
- CI: `.github/workflows/` (black/ruff/pytest).

## Commands Claude may run
- `pytest -q`
- `ruff check clockify_rag tests`
- `black clockify_rag tests`
- `python -m clockify_rag.cli_modern doctor --json` (info only)

## When editing
- Keep env defaults stable: corporate Ollama URL + `EMB_BACKEND=ollama`. Tests already override to local; do not change test overrides.
- For formatting issues, run `black` on touched files only.
- If adding tests, prefer small, deterministic pytest cases alongside existing patterns.
