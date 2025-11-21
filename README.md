# Clockify RAG – Internal Support Assistant

**Version**: 5.9 (Production-Ready)
**Status**: ✅ Deployed for internal use on corporate VPN
**Last Updated**: November 21, 2025

> **Internal tool for Clockify/CAKE support teams.** Provides AI-powered answers from documentation using Qwen 2.5 (32B) via internal Ollama endpoint.

## Overview

A Retrieval-Augmented Generation (RAG) system that answers questions about Clockify documentation using:
- **LLM**: Qwen 2.5 (32B) for answer generation
- **Embeddings**: nomic-embed-text (768-dim) for semantic search
- **Retrieval**: Hybrid BM25 + FAISS with MMR reranking
- **Deployment**: Internal VPN-only, no external API calls

### Key Features

- **Zero configuration** – Works out of the box with hardcoded internal defaults
- **Thread-safe** – Supports multi-threaded production deployments
- **VPN-resilient** – Smart timeouts and fallback handling for network issues
- **Security-hardened** – Error sanitization prevents internal URL/path leaks
- **Production-tested** – 295+ passing tests, comprehensive CI/CD

---

## Quick Start

### Prerequisites

- **Python 3.11-3.13** (3.12 recommended; **3.14+ not supported** due to Pydantic v1 incompatibility)
- **VPN access** to corporate network (for default Ollama endpoint)
- **Optional**: Local Ollama installation for offline development

### Installation

```bash
# Clone repository
git clone <repo-url>
cd 1rag

# Create virtual environment
python3.12 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e '.[dev]'

# Verify environment
python scripts/verify_env.py
```

**Apple Silicon (M1/M2/M3)**: See [docs/M1_COMPATIBILITY.md](docs/M1_COMPATIBILITY.md) for FAISS installation via conda.

### Usage

```bash
# Interactive chat (default: internal Ollama on VPN)
python -m clockify_rag.cli chat

# API server
uvicorn clockify_rag.api:app --host 0.0.0.0 --port 8000

# Health check
python -m clockify_rag.sanity_check
```

**No environment variables required** – System uses safe internal defaults:
- Ollama URL: `http://10.127.0.192:11434` (corporate VPN)
- Model: `qwen2.5:32b`
- Embeddings: `nomic-embed-text:latest`

### Building the Index

```bash
# Build vector index from knowledge base
make build

# Or manually
python -m clockify_rag.ingest knowledge_full.md
```

Generates artifacts: `chunks.jsonl`, `vecs_n.npy`, `meta.jsonl`, `bm25.json`, `index.meta.json`

---

## Configuration

### Environment Variables (All Optional)

Core configuration has hardcoded internal defaults. Override only if needed:

```bash
# Ollama endpoint (default: http://10.127.0.192:11434)
export RAG_OLLAMA_URL=http://127.0.0.1:11434

# Timeout overrides (defaults: connect=5s, read=120s)
export CHAT_CONNECT_TIMEOUT=5
export CHAT_READ_TIMEOUT=180

# Model overrides (defaults: qwen2.5:32b, nomic-embed-text)
export RAG_CHAT_MODEL=qwen2.5:32b
export RAG_EMBED_MODEL=nomic-embed-text:latest
```

See [docs/CONFIGURATION.md](docs/CONFIGURATION.md) for all available settings.

---

## Platform Compatibility

| Platform | Status | Notes |
|----------|--------|-------|
| **Linux** | ✅ Recommended | Production target |
| **macOS Intel** | ✅ Full support | Development tested |
| **macOS Apple Silicon** | ✅ Full support | Requires conda for FAISS |
| **Windows** | ⚠️ WSL2 only | Untested on native Windows |

---

## Development

### Running Tests

```bash
# Full test suite
pytest tests/

# Specific modules
pytest tests/test_config_module.py tests/test_sanitization.py -v

# With coverage
pytest --cov=clockify_rag --cov-report=html
```

### Code Quality

```bash
# Linting
ruff check clockify_rag tests

# Formatting
black clockify_rag tests

# Type checking
mypy clockify_rag
```

### Environment Validation

```bash
# Standard mode (warnings only)
python scripts/verify_env.py

# JSON output
python scripts/verify_env.py --json

# Strict mode (fails on missing optional deps)
python scripts/verify_env.py --strict
```

---

## Architecture

### Data Flow

```
User Query
    ↓
Sanitization & Validation
    ↓
Query Embedding (nomic-embed-text)
    ↓
Hybrid Retrieval (BM25 + FAISS)
    ↓
MMR Reranking (diversity + relevance)
    ↓
Context Packing (top 8 chunks)
    ↓
LLM Generation (qwen2.5:32b)
    ↓
Answer + Citations
```

### Key Components

- **`clockify_rag/config.py`** – Configuration with safe defaults
- **`clockify_rag/llm_client.py`** – LangChain ChatOllama wrapper
- **`clockify_rag/embeddings_client.py`** – Embedding generation
- **`clockify_rag/retrieval.py`** – Hybrid search + MMR reranking
- **`clockify_rag/answer.py`** – Answer generation pipeline
- **`clockify_rag/api.py`** – FastAPI REST interface
- **`clockify_rag/error_handlers.py`** – Security sanitization

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) and [CLAUDE.md](CLAUDE.md) for detailed design.

---

## Requirements

### Core Dependencies

- **Python 3.11-3.13** (3.12 recommended; **3.14+ not supported** due to Pydantic v1 incompatibility)
- **numpy** 2.3.4+ – Vector operations
- **httpx** 0.27.0+ – HTTP client
- **langchain-ollama** 0.1.0+ – LLM integration
- **rank-bm25** 0.2.2+ – Sparse retrieval
- **fastapi** 0.115.0+ – API server
- **typer** 0.15.0+ – CLI interface

### Optional Dependencies

- **faiss-cpu** 1.8.0+ – Fast vector search (graceful fallback to linear search if missing)
- **torch** 2.4.2+ – Local embeddings (not needed for remote Ollama)
- **sentence-transformers** 3.3.1+ – Local embeddings (not needed for remote Ollama)

### External Services

- **Ollama** – LLM inference server
  - Default: `http://10.127.0.192:11434` (corporate VPN)
  - Local override: `http://127.0.0.1:11434`
  - Required models: `qwen2.5:32b`, `nomic-embed-text`

---

## Deployment

### Production Checklist

1. ✅ Verify Python 3.11 or 3.12 (not 3.14+)
2. ✅ Run `python scripts/verify_env.py --strict`
3. ✅ Ensure VPN access to `http://10.127.0.192:11434`
4. ✅ Build index: `make build`
5. ✅ Run smoke tests: `make smoke`
6. ✅ Deploy with process manager (systemd/supervisor)

### Recommended Deployment

```bash
# Using gunicorn with multiple workers
gunicorn clockify_rag.api:app \
  --workers 4 \
  --threads 4 \
  --bind 0.0.0.0:8000 \
  --timeout 180 \
  --log-level info
```

**Thread safety**: v5.9 is fully thread-safe. Use `--threads 4` for optimal performance.

See [docs/PRODUCTION_GUIDE.md](docs/PRODUCTION_GUIDE.md) for detailed deployment instructions.

---

## Documentation

### Quick Links

- **New users**: [START_HERE.md](START_HERE.md)
- **Developers**: [CLAUDE.md](CLAUDE.md) (AI assistant guide)
- **Operations**: [docs/PRODUCTION_GUIDE.md](docs/PRODUCTION_GUIDE.md)
- **Architecture**: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- **Testing**: [TESTING.md](TESTING.md)
- **M1/M2/M3 Setup**: [docs/M1_COMPATIBILITY.md](docs/M1_COMPATIBILITY.md)

### Complete Index

See [docs/INDEX.md](docs/INDEX.md) for full documentation map.

---

## Troubleshooting

### Common Issues

**Ollama connection timeout**
```bash
# Check VPN connection
curl http://10.127.0.192:11434/api/version

# Or use local Ollama
export RAG_OLLAMA_URL=http://127.0.0.1:11434
```

**FAISS not available on M1/M2/M3**
```bash
# Install via conda (recommended)
conda install -c conda-forge faiss-cpu=1.8.0

# System falls back to linear search automatically
```

**Python 3.14 incompatibility**
```bash
# Use Python 3.11 or 3.12
python3.12 -m venv venv
source venv/bin/activate
pip install -e '.[dev]'
```

**Tests failing**
```bash
# Verify environment first
python scripts/verify_env.py --strict

# Run focused tests
pytest tests/test_config_module.py -v
```

---

## Contributing

### Development Setup

```bash
# Install dev dependencies
pip install -e '.[dev]'

# Install pre-commit hooks
pre-commit install

# Run full validation
make deps-check
make smoke
pytest tests/
```

### Code Standards

- **Linting**: `ruff check` must pass
- **Formatting**: `black` formatting enforced
- **Type hints**: Required for new code
- **Tests**: Required for new features
- **Documentation**: Update relevant docs in `docs/`

---

## License

Internal use only – Clockify/CAKE organization.

---

## Support

- **Issues**: File in internal issue tracker
- **Questions**: Ask in #eng-ai Slack channel
- **Documentation**: See [docs/INDEX.md](docs/INDEX.md)

---

## Version History

### v5.9 (Current - November 2025)
- ✅ Thread-safe for multi-threaded deployments
- ✅ Hardcoded safe internal defaults (no env vars required)
- ✅ Enhanced error sanitization
- ✅ Python 3.11-3.13 support (3.14+ blocked)
- ✅ 295+ passing tests

### v5.8 (November 2025)
- Configuration consolidation
- Remote Ollama resilience improvements
- Context budget optimization for Qwen 32B

### v5.7 (November 2025)
- Initial remote-first implementation
- VPN-backed Ollama support

See [CHANGELOG_v5.8.md](CHANGELOG_v5.8.md) and [CHANGELOG_v5.7.md](CHANGELOG_v5.7.md) for detailed history.

---

**Maintained by**: Internal Engineering Team
**Last Updated**: November 21, 2025
**Status**: ✅ Production-Ready
