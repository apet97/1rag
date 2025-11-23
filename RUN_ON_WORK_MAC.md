# Run on Aleksandar's Work Mac (VPN on)

Defaults are set for the corporate Ollama on VPN: base URL `http://10.127.0.192:11434`, chat model `qwen2.5:32b`, embeddings `nomic-embed-text` (768-dim), corpus `clockify_help_corpus.en.md` (falls back to `knowledge_full.md`). No environment variables are required.

Use `python3.12` if available; otherwise replace it with `python3`.

## CLI-Only Flow (zero-config)
```bash
python3.12 -m venv .venv          # fallback: python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e ".[dev]"
python -m clockify_rag.cli_modern ingest --force
python -m clockify_rag.cli_modern query "How do I add time for others?"
```

FAISS (optional ANN speedup on macOS arm64): install via conda, not pip:
```bash
conda install -c conda-forge faiss-cpu
```

## API Server Flow (localhost)
```bash
source .venv/bin/activate                       # reuse the same venv
python -m clockify_rag.cli_modern ingest --force  # ensure index is present
uvicorn clockify_rag.api:app --host 0.0.0.0 --port 8000
curl -X POST http://127.0.0.1:8000/v1/query \
  -H "Content-Type: application/json" \
  -d '{"question": "How do I add time for others?", "top_k": 8}'
```
