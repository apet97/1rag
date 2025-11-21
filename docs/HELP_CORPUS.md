# Help Corpus & Ingestion

How the Clockify/CAKE help-center corpus is refreshed and turned into searchable artifacts.

## Source of truth
- The corpus is delivered as a single Markdown file: `clockify_help_corpus.en.md` (UpdateHelpGPT export). Legacy `knowledge_full.md` remains supported as a fallback.
- Each article uses YAML front matter with: `id`, `source_url`, `domain`, `product`, `title`, `short_title`, `category`, `last_fetched`, `detected_lang`, `tags`, `is_hub`, and optional `suppress_from_rag`.
- Sections: **Summary**, **Canonical answer**, **Body**, **Key points**, **Limits & gotchas**, **FAQ**, **Search hints**, **Internal notes**.
- Any article with `suppress_from_rag: true` is skipped during ingestion.
- Hub/category pages (`is_hub: true`) are indexed but down-weighted during retrieval so they do not outrank specific answers.

## 🚧 Roadmap: UpdateHelpGPT Integration

**Status:** Planned enhancement (not yet implemented)

**Goal:** Automate help article scraping and corpus generation within this repository.

**Current workflow:**
1. External team runs UpdateHelpGPT tooling (not in this repo)
2. Team generates `clockify_help_corpus.en.md` export
3. File is manually dropped into repo root
4. Developer runs `ingest` command to rebuild index

**Planned workflow:**
1. Add `UpdateHelpGPT/` directory to repo with scraper scripts
2. Implement `UpdateHelpGPT/refresh_help_corpus.py`:
   - Scrape Clockify/CAKE help centers
   - Generate `clockify_help_corpus.en.md` (current filename, `knowledge_full.md` stays as fallback)
   - Output metadata files: `url_manifest.txt`, `scrape_report.json`
3. Add CLI command: `python -m clockify_rag.cli_modern refresh-corpus --delay-seconds 0.75 --max-pages 1500`
4. Integrate with CI for periodic corpus updates

**Benefits:**
- 🔄 **Automated updates**: Schedule corpus refresh via CI/cron
- 📊 **Traceability**: Track which URLs were scraped and when
- 🛠️ **Self-contained**: No dependency on external team for corpus generation
- 🔍 **Transparency**: Scrape logic and metadata visible in repo

**Implementation notes:**
- Keep existing `knowledge_full.md` workflow for backward compatibility
- Scraper should respect rate limits and robots.txt
- Consider incremental updates (only scrape changed pages)
- Validate output format matches current chunking expectations

For now, **continue using the external UpdateHelpGPT export workflow** described below.

## Refreshing the corpus
1. Generate/export the latest help-center Markdown (internal UpdateHelpGPT tooling).
2. Place the file at `clockify_help_corpus.en.md` in the repo root (or `knowledge_full.md` if you receive a legacy export).
3. (Optional) Record the hash for drift detection:
   ```bash
   shasum clockify_help_corpus.en.md
   ```

## Building the index
```bash
# Local/offline friendly (default embeddings are local)
python -m clockify_rag.cli_modern ingest --input clockify_help_corpus.en.md --force

# Internal deployment (remote embeddings via Ollama)
EMB_BACKEND=ollama \
python -m clockify_rag.cli_modern ingest --input clockify_help_corpus.en.md --force
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
- Keep `clockify_help_corpus.en.md` (or `knowledge_full.md`) under version control only if you intend to pin a specific snapshot; otherwise treat it as data.
- FAISS on Apple Silicon may require `conda install -c conda-forge faiss-cpu=1.8.0`; until installed, retrieval falls back to linear search + BM25.
- If the corpus changes, always rebuild the artifacts and restart any long-running API/CLI processes so they reload the new indexes.
