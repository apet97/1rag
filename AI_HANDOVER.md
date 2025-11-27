# AI Handover – Clockify/CAKE Internal RAG

This document summarizes the codebase so another AI can pick up quickly.

## High-Level Purpose
- Answer Clockify/CAKE support tickets using Retrieval-Augmented Generation (RAG).
- Uses local help docs (preferred: `knowledge_base/` directory of per-article Markdown files with YAML frontmatter).
- Hybrid retrieval (BM25 + dense embeddings), best-last packing, strict source URL validation, and a structured JSON answer contract.

## Entry Points
- CLI (preferred): `clockify_rag/cli_modern.py`
  - `ingest`: build/rebuild index from KB.
  - `query`: single question.
  - `chat`: REPL.
  - `doctor`: diagnostics.
- Legacy wrappers: `clockify_support_cli.py`, `clockify_support_cli_final.py` (back-compat).
- API: `clockify_rag/api.py` (FastAPI app; `/v1/query`, `/v1/ingest`, health/metrics).

## Config and Defaults
- Config module: `clockify_rag/config.py`; defaults in `config/defaults.yaml`.
- Corpus resolution (utils.resolve_corpus_path): prefers `knowledge_base/`, then `clockify_help_corpus.en.md`, then `knowledge_full.md`.
- LLM/embeddings: Ollama endpoint (`RAG_OLLAMA_URL`, default internal), chat model `qwen2.5:32b`, embed model `nomic-embed-text` (768d). `EMB_BACKEND` can be `ollama` or `local`.
- Token budgets: `CTX_TOKEN_BUDGET`, `DEFAULT_NUM_CTX`, etc.

## Ingestion and Chunking
- Ingestion helpers: `clockify_rag/ingestion.py` (generic converters), but main path is `build_chunks` in `clockify_rag/chunking.py`.
- `build_chunks`:
  - Accepts file or directory. For directories, iterates all `*.md`.
  - Parses YAML frontmatter: title/url/category/slug (+ optional id/short_title/is_hub/suppress_from_rag).
  - Skips `suppress_from_rag: true`.
  - Splits by H2 sections, extracts H3/H4 subsections.
  - Breadcrumb prefix: `Context: <Title> > <Section> > <Subsection>` prepended to chunk text.
  - Metadata includes breadcrumb, section importance hints, category/slug, etc.
  - Article key derived from canonical URL (`_article_key` in retrieval).
- Index build: `clockify_rag/indexing.py::build` writes `chunks.jsonl`, `vecs_n.npy`, `bm25.json`, optional `faiss.index`, `index.meta.json`. Uses atomic writes and build lock (`utils.build_lock`). FAISS optional; falls back to flat dense + BM25.
- SHA hashing (`utils.compute_sha256`) supports directories for KB drift detection.

## Retrieval Flow
- Entry: `clockify_rag/retrieval.py::retrieve`.
  - Validates and lightly normalizes query (`normalize_query` strips obvious noise).
  - Embeds query (local or Ollama).
  - Hybrid scores: BM25 (`bm25_scores`) + dense; intent classification optional for alpha tuning.
  - Candidate selection includes ANN (FAISS/HNSW) if configured.
  - Dedup by (title, section).
- Packing: `pack_snippets`:
  - Groups chunks by article key (prefer URL).
  - Sorts chunks within article by section/chunk index.
  - Applies token budget; packs articles in reverse retrieval order so the best article ends up last (“best-last” recency bias).
  - Returns packed context text, packed chunk IDs, used tokens, and article_blocks (title/url/text/chunk_ids).
- Role/security hints: `derive_role_security_hints` (very light heuristics).

## Prompting and Answering
- Prompts: `clockify_rag/prompts.py` (QWEN_SYSTEM_PROMPT and user prompt builder).
  - System prompt enforces pipeline: get context → analyze intent → read articles → answer with JSON (intent, user_role_inferred, security_sensitivity, answer_style=ticket_reply, short_intent_summary, answer, sources_used URLs, needs_human_escalation).
  - Role/security hints are hints, not hard constraints.
- Answer generation: `clockify_rag/answer.py::generate_llm_answer`.
  - Builds packed chunks/article blocks, calls `ask_llm` (LLM via `api_client`).
  - Parses structured JSON (defensive) via `parse_qwen_json`.
  - URL verification: normalizes sources_used, filters against URLs present in context (anchors/trailing slashes tolerated), dedupes.
  - Confidence: computed from retrieval scores if not provided.
- Output formatting: CLI prints human-friendly answer + metadata; `--json` returns full JSON.

## Utilities and Guards
- `clockify_rag/utils.py`: corpus resolution, tokenization, noise stripping, logging sanitization, build locks, Ollama URL validation, etc.
- `clockify_rag/metrics.py`: counters/histograms/gauges; API exposes `/v1/metrics`.
- Concurrency: API uses locks to serialize ingests; query during ingest returns consistent state or 503.

## Tests to Know
- `tests/test_article_packing.py`: ensures grouping, ordering, best-last packing, and trimming under tight budgets.
- `tests/test_knowledge_base_ingestion.py`: KB directory ingest uses frontmatter (title/url/category/slug), breadcrumb, article key.
- `tests/test_answer_sources.py`: drops hallucinated URLs from sources_used.
- `tests/test_qwen_contract.py`: JSON contract parsing.
- `tests/test_corpus_resolution.py`: corpus resolution ordering.
- Integration fixtures: `tests/test_integration.py`, etc. (mocked embeddings).

## Operational Commands
- Build index from KB: `python3.12 -m clockify_rag.cli_modern ingest --input ./knowledge_base --force`
- Query: `python3.12 -m clockify_rag.cli_modern query "How do I add time for others?"`
- Chat: `python3.12 -m clockify_rag.cli_modern chat`
- API: `uvicorn clockify_rag.api:app --host 0.0.0.0 --port 8000`
- Doctor: `python3.12 -m clockify_rag.cli_modern doctor`

## Current State / Notes
- Default corpus path now points to `knowledge_base/` (dir-first).
- Tests around packing and URL verification are green locally (see recent runs).
- `clockify_rag/indexing.py` may have local uncommitted edits in this workspace; be cautious not to override user changes.
- `knowledge_base/` should exist at repo root for ingestion; treat its contents as input-only.
