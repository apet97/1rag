# Configuration Reference

`clockify_rag/config.py` is the source of truth. Values resolve in this order: environment variables → `.env` → hard-coded defaults. Legacy aliases (`OLLAMA_URL`, `GEN_MODEL`, `EMB_MODEL`) still work but prefer the `RAG_*` namespace.

## ⚡ Default Values — No Configuration Required

**For internal VPN use on macOS M1/M2/M3 Pro, no environment variables are required.** The system ships with production-ready defaults tuned for the internal corporate environment:

| Setting | Default Value | Purpose |
|---------|---------------|---------|
| `RAG_OLLAMA_URL` | `http://10.127.0.192:11434` | Corporate/local Ollama host |
| `RAG_CHAT_MODEL` | `qwen2.5:32b` | Generation model for answers |
| `RAG_EMBED_MODEL` | `nomic-embed-text` | Embedding model (when `EMB_BACKEND=ollama`) |
| `EMB_BACKEND` | `ollama` | Remote embeddings via corporate Ollama (768-dim) |
| `DEFAULT_RETRIES` | `2` | Network retry attempts for VPN resilience |
| `CHAT_READ_TIMEOUT` | `120s` | LLM response timeout |
| `EMB_READ_TIMEOUT` | `120s` | Embedding timeout |

**Key features:**
- ✅ **No mandatory env vars**: Just clone, install, and run.
- ✅ **VPN-safe defaults**: Internal Ollama URL hard-coded; lazy model selection avoids startup failures.
- ✅ **Remote-first**: Corporate Ollama embeddings by default; set `EMB_BACKEND=local` for offline/dev.
- ✅ **Override when needed**: Set `RAG_OLLAMA_URL=http://127.0.0.1:11434` for local Ollama; default uses the corporate host.
- ✅ **macOS arm64**: Install FAISS via conda (`conda install -c conda-forge faiss-cpu`) if you want ANN speedups; otherwise BM25/flat search is used.

See [README.md](../README.md) for the zero-config quickstart.

## Environment Profiles
- **Internal (default):** Remote Ollama endpoint on corporate network, chat model `qwen2.5:32b`, embedding model `nomic-embed-text` (768-dim), `EMB_BACKEND=ollama`. No env vars required for normal use.
- **Local dev:** Override via env vars if you run a local Ollama or want local embeddings: e.g., `RAG_OLLAMA_URL=http://127.0.0.1:11434`, `EMB_BACKEND=local`, `RAG_LLM_CLIENT=mock` for offline smoke tests.
- **Mock/offline:** Set `RAG_LLM_CLIENT=mock` (and optionally `EMB_BACKEND=local`) for CI/offline scenarios.

## Ollama & models
| Variable | Default | Purpose |
|----------|---------|---------|
| `RAG_OLLAMA_URL` | `http://10.127.0.192:11434` | Base URL for Qwen + embeddings. |
| `RAG_CHAT_MODEL` | `qwen2.5:32b` | Generation model. |
| `RAG_EMBED_MODEL` | `nomic-embed-text` | Embedding model when `EMB_BACKEND=ollama`. |
| `EMB_BACKEND` | `ollama` | `ollama` (production, remote embeddings) or `local` (SentenceTransformer). |
| `RAG_LLM_CLIENT` | `""` | `mock`/`test` for offline CI; empty uses real Ollama. |

## Retrieval & prompting
| Variable | Default | Purpose |
|----------|---------|---------|
| `DEFAULT_TOP_K` | `15` | Candidates fetched per retriever before filtering. |
| `DEFAULT_PACK_TOP` | `8` | Snippets packed into the prompt. |
| `DEFAULT_THRESHOLD` | `0.25` | Minimum hybrid score to include a chunk. |
| `DEFAULT_NUM_CTX` | `32768` | Context window passed to the LLM. |
| `DEFAULT_NUM_PREDICT` | `512` | Max output tokens. |
| `CTX_BUDGET` | `12000` | Token budget reserved for snippets. |
| `ALPHA` | `0.5` | Hybrid weight (BM25 vs dense). |
| `MMR_LAMBDA` | `0.75` | Relevance vs diversity balance. |
| `USE_INTENT_CLASSIFICATION` | `1` | Adjust `ALPHA` per query intent. |
| `MAX_QUERY_LENGTH` | `1000000` | Hard length cap. |

## Chunking & indexing
| Variable | Default | Purpose |
|----------|---------|---------|
| `CHUNK_CHARS` | `1600` | Target characters per chunk. |
| `CHUNK_OVERLAP` | `200` | Overlap between chunks. |
| `ANN` | `faiss` | ANN backend (`faiss` or `none`). |
| `ANN_NLIST` / `ANN_NPROBE` | `64` / `16` | FAISS IVF params. |
| `FAISS_CANDIDATE_MULTIPLIER` | `3` | Dense candidates = `top_k * multiplier`. |
| `ANN_CANDIDATE_MIN` | `200` | Minimum dense candidates. |
| `FAISS_IVF_MIN_ROWS` | `20000` | Threshold to switch from flat to IVF. |

## Timeouts & retries
| Variable | Default | Notes |
|----------|---------|-------|
| `CHAT_CONNECT_TIMEOUT` | `3.0` | LLM connect timeout (s). |
| `CHAT_READ_TIMEOUT` | `120.0` | LLM read timeout (s). |
| `EMB_CONNECT_TIMEOUT` | `5.0` | Embedding connect timeout (s). |
| `EMB_READ_TIMEOUT` | `60.0` | Embedding read timeout (s). |
| `DEFAULT_RETRIES` | `2` | Retries for Ollama calls. |
| `WARMUP` | `1` | Preload models/index on startup. |

## Logging, metrics, auth
| Variable | Default | Purpose |
|----------|---------|---------|
| `RAG_LOG_FILE` | `rag_queries.jsonl` | Structured query log path. |
| `RAG_LOG_INCLUDE_ANSWER` | `1` | Include answer text in logs (0 redact). |
| `RAG_LOG_INCLUDE_CHUNKS` | `0` | Include chunk text in logs (off by default). |
| `RAG_STRICT_CITATIONS` | `0` | Refuse answers without citations when set to 1. |
| `API_AUTH_MODE` | `none` | `api_key` enables shared-secret auth. |
| `API_ALLOWED_KEYS` | *(empty)* | Comma-separated API keys when auth is on. |
| `API_KEY_HEADER` | `x-api-key` | Header name for API key auth. |

## Caching & expansions
| Variable | Default | Purpose |
|----------|---------|---------|
| `CACHE_MAXSIZE` | `100` | In-memory query cache size. |
| `CACHE_TTL` | `3600` | Query cache TTL (seconds). |
| `CLOCKIFY_QUERY_EXPANSIONS` | *(unset)* | Override for query expansion JSON. |
| `MAX_QUERY_EXPANSION_FILE_SIZE` | `10485760` | Max bytes for expansion file (10 MB). |
| `FAQ_CACHE_ENABLED` | `0` | Enable FAQ cache. |
| `FAQ_CACHE_PATH` | `faq_cache.json` | FAQ cache file. |

## Validation commands
- `python -m clockify_rag.sanity_check` – connectivity, model availability, end-to-end probe.
- `python -m clockify_rag.cli_modern doctor --json` – system/config/index snapshot.
- `python scripts/verify_env.py --strict` – dependency checks.
