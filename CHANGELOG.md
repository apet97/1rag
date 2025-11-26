# Changelog

All notable changes to Clockify RAG will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Security
- **Prompt injection prevention**: Added `_escape_chunk_text()` function to sanitize chunk content before embedding in prompts. Neutralizes:
  - Triple quote escapes that could break content delimiters
  - Fake `[ARTICLE id=...]` markers that could confuse the LLM
  - `[SYSTEM]` and `[CONTEXT]` markers that could enable injection attacks
  - File: `clockify_rag/prompts.py`

- **Query expansion DoS prevention**: Added `MAX_QUERY_EXPANSION_ENTRIES` config (default 10,000) to limit in-memory size of query expansion dictionary
  - File: `clockify_rag/retrieval.py`, `clockify_rag/config.py`

### Fixed
- **Z-score normalization bug**: When all scores are identical (std=0), now returns zeros instead of original values. This preserves the invariant that normalized scores center around 0 and prevents unpredictable hybrid scoring behavior.
  - File: `clockify_rag/retrieval.py` line 458-479

- **FAISS index race condition**: Moved `reset_faiss_index()` call to happen BEFORE `save_faiss_index()` instead of after. This prevents a race condition where concurrent readers could get stale cached indexes between save and reset.
  - File: `clockify_rag/indexing.py` lines 444-450

### Changed
- **HTTP client caching**: `get_llm_client()` now reuses a cached `httpx.Client` instance instead of creating a new one on every call. This improves performance through connection pool reuse and reduces socket exhaustion.
  - File: `clockify_rag/llm_client.py`
  - Added: `_get_http_client()` helper with thread-safe lazy initialization

### Added
- **Circuit breaker pattern**: New `clockify_rag/circuit_breaker.py` module for resilient remote service calls
  - Prevents cascading failures by temporarily blocking requests to unhealthy services
  - Thread-safe with configurable failure threshold and reset timeout
  - Includes `@circuit_breaker` decorator for easy function wrapping
  - File: `clockify_rag/circuit_breaker.py`

- **Security test suite**: New `tests/test_security_payloads.py` with 33 tests covering:
  - Query validation edge cases
  - Prompt injection prevention
  - Binary and malformed data handling
  - Unicode edge cases (RTL, emoji, zero-width chars)
  - Score normalization robustness

- **API contract tests**: New `tests/test_api_contract.py` with 35 tests covering:
  - Request/response schema validation
  - HTTP status codes for various scenarios
  - Error message formats and sanitization
  - Rate limiting behavior
  - Content-type handling

- **Load tests**: New `tests/test_load.py` with stress tests for:
  - Sustained retrieval load
  - Concurrent retrieval requests
  - BM25 memory stability
  - Normalization performance
  - Query expansion load
  - Resource cleanup verification

- **Answer parsing tests**: New `tests/test_answer_parsing.py` with 33 tests for:
  - Confidence parsing robustness (int, float, string, edge cases)
  - Intent parsing and validation
  - Sources parsing and coercion
  - Citation extraction and validation

- **Embedding dimension validation**: Per-call dimension validation in embedding functions
  - Validates returned embedding dimensions match configured `EMB_DIM`
  - Provides clear error messages when model output doesn't match config
  - File: `clockify_rag/embeddings_client.py`

### Fixed
- **API exception handling**: HTTPException (like 429 rate limit) is now properly re-raised instead of being caught and converted to 500
  - File: `clockify_rag/api.py`

- **Type coercion in answer parsing**: Improved robustness of `parse_qwen_json()` confidence parsing
  - Now handles string-encoded numbers, floats, and edge cases gracefully
  - Properly rounds float values and clamps to valid range (0-100)
  - File: `clockify_rag/answer.py`

## [5.9.1] - Previous Release

### Notes
- Production-ready release with hybrid retrieval (BM25 + FAISS)
- Zero-config VPN defaults for corporate environment
- M1/M2/M3 Apple Silicon optimization
- Comprehensive test coverage (365+ tests)

---

## Migration Notes

### Upgrading from 5.9.1

**Breaking Changes**: None - all changes are backward compatible.

**Behavioral Changes**:
1. `normalize_scores_zscore()` now returns zeros when all input scores are identical (previously returned original values). This is the mathematically correct behavior.

2. The FAISS index cache is now reset before saving new indexes, not after. This may result in slightly different behavior during concurrent build/query operations, but prevents stale data issues.

**New Configuration Options**:
- `MAX_QUERY_EXPANSION_ENTRIES`: Maximum entries in query expansion dictionary (default: 10,000)
- `CIRCUIT_BREAKER_THRESHOLD`: Number of failures before circuit opens (default: 5)
- `CIRCUIT_BREAKER_RESET_TIMEOUT`: Seconds before testing recovery (default: 60.0)
