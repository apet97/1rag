# Python / Dependency / Platform Hygiene Plan

**Date**: 2025-11-19
**Objective**: Clean up Python version support, dependency management, and M1 compatibility

## Phase 0: Audit Summary

### Current Warnings (Python 3.14 on M1 Pro)
1. **Pydantic v1 / LangChain**: "Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater"
2. **FAISS**: "FAISS wheels are not published for macOS arm64; install via conda"
3. **Optional deps**: "Optional dependencies not installed: torch"

### Current State
- **pyproject.toml**:
  - `requires-python = ">=3.11,<3.12"` ← TOO RESTRICTIVE (excludes 3.12)
  - `torch>=2.3.0,<2.6.0` listed as REQUIRED dependency ← Should be optional
  - FAISS correctly excluded from dependencies
  - Classifiers list 3.11 and 3.12 (but constraint excludes 3.12)

- **CI**: Python 3.11 only (should add 3.12)

- **Documentation**: Good foundation but needs "Known Warnings" section

## Planned Changes

### Phase 1: Python Version Range
- [ ] Change `requires-python` to `">=3.11,<3.14"` (allow 3.11-3.12, block 3.14)
- [ ] Add note in classifiers: "Not compatible with Python 3.14 (Pydantic v1 limitation)"
- [ ] Update tool configs (black, ruff, mypy) target versions

### Phase 2: Dependency Layout
- [ ] Move `torch` from required to optional extra `[embeddings]`
- [ ] Verify all other deps are correctly categorized:
  - Core: langchain-ollama, numpy, httpx, etc.
  - Dev: pytest, mypy, ruff, black
  - Optional: torch, sentence-transformers (for local embeddings)
  - FAISS: Document as conda-only for M1

### Phase 3: macOS M1 Compatibility
- [ ] Update verify_env.py to treat FAISS/torch as optional with friendly messages
- [ ] Add pytest.importorskip for optional deps in tests
- [ ] Update M1_COMPATIBILITY.md with "Expected Warnings" section

### Phase 4: Test Behavior
- [ ] Add conftest.py with markers for optional dependencies
- [ ] Mark tests requiring torch/FAISS with `@pytest.mark.optional_embeddings`
- [ ] Use `pytest.importorskip("torch")` where needed

### Phase 5: CI Updates
- [ ] Add Python 3.12 to test matrix
- [ ] Keep 3.11 as minimum supported
- [ ] Ensure FAISS is NOT required in CI (optional)

### Phase 6: Documentation
- [ ] Add "Supported Python Versions" section to PRODUCTION_GUIDE.md
- [ ] Add "Known Warnings (Mac M1)" section to M1_COMPATIBILITY.md
- [ ] Update SMOKE_TEST_RUNBOOK.md with optional dep guidance

## Target Support Matrix

| Environment | Python | FAISS | torch | Status |
|-------------|--------|-------|-------|--------|
| Server/CI (Linux x86_64) | 3.11-3.12 | Optional | Optional | Primary |
| Local Dev (macOS M1) | 3.11-3.12 | Optional (conda) | Optional | Supported |
| Python 3.14 | 3.14 | - | - | Not supported (Pydantic v1) |

## Acceptable Warnings (M1 only)
- FAISS missing: Core RAG works without FAISS (fallback to linear search)
- torch missing: Core RAG works with remote Ollama embeddings only
- Pydantic 3.14: Only if user forces unsupported Python version

## Success Criteria
- [ ] No warnings on Python 3.11 or 3.12 (supported versions)
- [ ] Clear error message on Python 3.14 explaining incompatibility
- [ ] Tests pass on Linux 3.11 and 3.12
- [ ] Tests pass on macOS M1 with documented warnings
- [ ] Documentation explains all acceptable warnings
