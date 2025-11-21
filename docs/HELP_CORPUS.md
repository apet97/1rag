# Help Corpus & Ingestion

How the Clockify/CAKE help-center corpus is refreshed and turned into searchable artifacts.

## Source of truth
- The corpus is delivered as a single Markdown file: `knowledge_full.md`.
- It is generated internally (UpdateHelpGPT export) outside this repo. Drop the latest export at the repo root before rebuilding.
- English-only content is assumed; the RAG pipeline is not multi-lingual.

## Refreshing the corpus
1. Generate/export the latest help-center Markdown (internal UpdateHelpGPT tooling).
2. Place the file at `knowledge_full.md` in the repo root.
3. (Optional) Record the hash for drift detection:
   ```bash
   shasum knowledge_full.md
   ```

## Building the index
```bash
# Local/offline friendly (default embeddings are local)
python -m clockify_rag.cli_modern ingest --input knowledge_full.md --force

# Internal deployment (remote embeddings via Ollama)
EMB_BACKEND=ollama \
python -m clockify_rag.cli_modern ingest --input knowledge_full.md --force
```
Outputs (beside the repo): `chunks.jsonl`, `vecs_n.npy`, `bm25.json`, `faiss.index` (when FAISS is installed), `index.meta.json`, `.build.lock` (temporary).

## Validating a build
- `python -m clockify_rag.cli_modern doctor --json` – check artifact presence/sizes.
- `python -m clockify_rag.sanity_check` – verifies config, Ollama connectivity, embeddings, and a minimal LLM round-trip.
- `python scripts/smoke_rag.py --client ollama --question "How do I lock timesheets?"` – quick end-to-end smoke (set `--client mock` for offline).

## Helpful utilities
- `scripts/generate_chunk_title_map.py` – map titles → chunk IDs for QA/labeling.
- `scripts/build_faq_cache.py` – optional precomputed FAQ cache (`FAQ_CACHE_ENABLED=1`).
- `scripts/create_dummy_index.py` – build tiny artifacts for CI/offline demo.

## Ingestion pipeline (code)
- `clockify_rag/chunking.py` – heading-aware splits with overlap (`CHUNK_CHARS`, `CHUNK_OVERLAP`).
- `clockify_rag/embedding.py` and `clockify_rag/embeddings_client.py` – local vs Ollama embeddings.
- `clockify_rag/indexing.py` – FAISS/BM25 build, locking, metadata, and validation.

## Operational notes
- Keep `knowledge_full.md` under version control only if you intend to pin a specific snapshot; otherwise treat it as data.
- FAISS on Apple Silicon may require `conda install -c conda-forge faiss-cpu=1.8.0`; until installed, retrieval falls back to linear search + BM25.
- If the corpus changes, always rebuild the artifacts and restart any long-running API/CLI processes so they reload the new indexes.
