# Architecture Vision

## Modularization Roadmap
1. **Core package split**  
   - Create `clockify_rag/core/` with submodules `retrieval`, `context`, `evaluation`, `io`.  
   - Move shared logic from `clockify_support_cli_final.py` into core modules.  
   - Provide stable typed interfaces (dataclasses for chunks, retrieval scores).
2. **Thin CLI layer**  
   - Replace monolithic CLI with lightweight wrapper importing from `clockify_rag`.  
   - Implement Click/Typer-based CLI for better UX while preserving current argparse flags.  
   - Ensure CLI only handles argument parsing, environment config, and output formatting.
3. **Service-ready API**  
   - Expose `clockify_rag.api` with `build_index`, `load_index`, `answer_query`, supporting synchronous and streaming responses.  
   - Add FastAPI reference implementation using same core modules.

## Plugin & Extension Architecture
- **Plugin discovery:** Use `importlib.metadata.entry_points(group="clockify_rag.plugins")` to auto-load retrievers/rerankers.  
- **Validation hooks:** Each plugin exposes `validate()` returning diagnostics aggregated in startup logs.  
- **Configuration:** Allow YAML/JSON config mapping plugin names to pipeline stages.  
- **Fallback ordering:** Provide default hybrid retrieval, but allow overriding dense retriever, rerank model, or citation formatter individually.

## API Design
- **Data models:**
  ```python
  @dataclass
  class Chunk:
      id: str
      title: str
      section: str
      url: str
      text: str
  
  @dataclass
  class RetrievalResult:
      chunk: Chunk
      scores: dict[str, float]
  
  @dataclass
  class Answer:
      text: str
      citations: list[str]
      confidence: int
      diagnostics: dict[str, Any]
  ```
- **Primary functions:**
  - `build_index(source: Path, *, cache: bool = True) -> IndexArtifacts`
  - `retrieve(question: str, artifacts: IndexArtifacts, *, top_k: int) -> list[RetrievalResult]`
  - `generate_answer(question: str, context: list[Chunk], *, model_cfg: ModelConfig) -> Answer`

## Scaling Strategy
1. **Distributed indexing**  
   - Partition knowledge base by namespace, build FAISS indexes per shard, store metadata in SQLite.  
   - Use multiprocessing to parallelize BM25 tokenization.
2. **Query caching & serving**  
   - Introduce Redis-backed cache for `answer_once` results and embedding vectors.  
   - Implement TTL eviction aligned with RateLimiter to prevent hammering.
3. **Streaming responses**  
   - Support event-stream output from LLMs; propagate partial answers via generator interface.
4. **Observability**  
   - Emit OpenTelemetry spans for build/retrieve/ask.  
   - Aggregate KPI metrics and retrieval profile stats in Prometheus.

## Long-Term Enhancements
- **Cross-encoder reranking:** Add optional ColBERT / bge-reranker integration with batching and caching.  
- **Multilingual support:** Normalize Unicode, add language detection, route to language-specific embeddings.  
- **Metadata enrichment:** Attach creation timestamps, provenance, and snippet confidence to each chunk.  
- **Evaluation suite:** Automate nightly run producing leaderboard of metrics stored in JSON for regression detection.  
- **Knowledge lifecycle:** Track `kb_sha` and diff knowledge base snapshots, triggering incremental rebuilds.
