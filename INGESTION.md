# Document Ingestion Guide

This project now uses a single help-corpus entry point (`knowledge_full.md`) plus the ingestion pipeline described in `docs/HELP_CORPUS.md`. That document covers:

- How to refresh the corpus (UpdateHelpGPT export).
- How to rebuild artifacts with `clockify_rag.cli_modern ingest`.
- Validation steps and helper scripts.

The code-level ingestion utilities remain in `clockify_rag/ingestion.py` if you need to import custom formats, but the canonical operational flow lives in `docs/HELP_CORPUS.md`.
