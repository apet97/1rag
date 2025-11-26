"""Pydantic BaseSettings for configuration validation.

This module provides type-validated configuration using Pydantic v2 BaseSettings.
It complements the existing config.py module by providing:
- Type validation at startup
- Environment variable documentation
- Better IDE support
- Optional JSON schema generation

Usage:
    from clockify_rag.settings import get_settings

    settings = get_settings()
    print(settings.ollama_url)
    print(settings.chat_model)

The settings are cached after first load for performance.
"""

from functools import lru_cache
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class OllamaSettings(BaseSettings):
    """Ollama LLM and embedding configuration."""

    model_config = SettingsConfigDict(
        env_prefix="RAG_",
        extra="ignore",
    )

    ollama_url: str = Field(
        default="http://10.127.0.192:11434",
        description="Ollama API endpoint URL",
        json_schema_extra={"env": ["RAG_OLLAMA_URL", "OLLAMA_URL"]},
    )
    chat_model: str = Field(
        default="qwen2.5:32b",
        description="LLM model for chat/generation",
        json_schema_extra={"env": ["RAG_CHAT_MODEL", "GEN_MODEL", "CHAT_MODEL"]},
    )
    embed_model: str = Field(
        default="nomic-embed-text",
        description="Model for embeddings",
        json_schema_extra={"env": ["RAG_EMBED_MODEL", "EMB_MODEL", "EMBED_MODEL"]},
    )
    chat_fallback_model: str = Field(
        default="gpt-oss:20b",
        description="Fallback model when primary is unavailable",
    )
    timeout: float = Field(
        default=120.0,
        ge=5.0,
        le=600.0,
        description="Timeout for Ollama operations (seconds)",
    )


class RetrievalSettings(BaseSettings):
    """Retrieval and search configuration."""

    model_config = SettingsConfigDict(
        env_prefix="",
        extra="ignore",
    )

    # Chunking
    chunk_chars: int = Field(
        default=1600,
        ge=100,
        le=8000,
        alias="CHUNK_CHARS",
        description="Characters per chunk",
    )
    chunk_overlap: int = Field(
        default=200,
        ge=0,
        le=4000,
        alias="CHUNK_OVERLAP",
        description="Overlap between chunks",
    )

    # Retrieval parameters
    default_top_k: int = Field(
        default=15,
        ge=1,
        le=100,
        alias="DEFAULT_TOP_K",
        description="Number of chunks to retrieve",
    )
    max_top_k: int = Field(
        default=50,
        ge=1,
        le=200,
        alias="MAX_TOP_K",
        description="Maximum allowed top_k",
    )
    default_pack_top: int = Field(
        default=8,
        ge=1,
        le=50,
        alias="DEFAULT_PACK_TOP",
        description="Number of chunks in LLM context",
    )
    default_threshold: float = Field(
        default=0.25,
        ge=0.0,
        le=1.0,
        alias="DEFAULT_THRESHOLD",
        description="Minimum similarity threshold",
    )

    # BM25 parameters
    bm25_k1: float = Field(
        default=1.2,
        ge=0.1,
        le=10.0,
        alias="BM25_K1",
        description="BM25 term frequency saturation",
    )
    bm25_b: float = Field(
        default=0.65,
        ge=0.0,
        le=1.0,
        alias="BM25_B",
        description="BM25 document length normalization",
    )

    # Hybrid search
    alpha_hybrid: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        alias="ALPHA",
        description="BM25 weight in hybrid search (0=dense only, 1=BM25 only)",
    )
    mmr_lambda: float = Field(
        default=0.75,
        ge=0.0,
        le=1.0,
        alias="MMR_LAMBDA",
        description="MMR relevance vs diversity (higher = more relevance)",
    )


class EmbeddingSettings(BaseSettings):
    """Embedding backend configuration."""

    model_config = SettingsConfigDict(
        env_prefix="EMB_",
        extra="ignore",
    )

    backend: str = Field(
        default="ollama",
        description="Embedding backend: 'local' or 'ollama'",
    )
    max_workers: int = Field(
        default=8,
        ge=1,
        le=64,
        description="Concurrent embedding workers",
    )
    batch_size: int = Field(
        default=32,
        ge=1,
        le=1000,
        description="Texts per embedding batch",
    )
    connect_timeout: float = Field(
        default=5.0,
        ge=1.0,
        le=60.0,
        alias="EMBEDDING_CONNECT_TIMEOUT",
        description="Embedding connection timeout (seconds)",
    )
    read_timeout: float = Field(
        default=60.0,
        ge=5.0,
        le=300.0,
        alias="EMBEDDING_READ_TIMEOUT",
        description="Embedding read timeout (seconds)",
    )

    @field_validator("backend")
    @classmethod
    def validate_backend(cls, v: str) -> str:
        """Validate embedding backend."""
        v = v.lower().strip()
        if v not in ("local", "ollama"):
            raise ValueError(f"Invalid EMB_BACKEND: {v}. Must be 'local' or 'ollama'")
        return v

    @property
    def dim(self) -> int:
        """Return embedding dimension based on backend."""
        return 384 if self.backend == "local" else 768


class ANNSettings(BaseSettings):
    """Approximate nearest neighbor (FAISS) configuration."""

    model_config = SettingsConfigDict(
        env_prefix="ANN_",
        extra="ignore",
    )

    use_ann: str = Field(
        default="faiss",
        alias="ANN",
        description="ANN backend: 'faiss' or 'none'",
    )
    nlist: int = Field(
        default=64,
        ge=8,
        le=1024,
        description="Number of IVF clusters",
    )
    nprobe: int = Field(
        default=16,
        ge=1,
        le=256,
        description="Number of clusters to search",
    )
    ivf_min_rows: int = Field(
        default=20000,
        ge=0,
        le=1_000_000,
        alias="FAISS_IVF_MIN_ROWS",
        description="Minimum rows for IVF vs Flat index",
    )


class CacheSettings(BaseSettings):
    """Caching and rate limiting configuration."""

    model_config = SettingsConfigDict(
        env_prefix="",
        extra="ignore",
    )

    cache_maxsize: int = Field(
        default=100,
        ge=1,
        le=10000,
        alias="CACHE_MAXSIZE",
        description="Maximum cached queries",
    )
    cache_ttl: int = Field(
        default=3600,
        ge=60,
        le=86400,
        alias="CACHE_TTL",
        description="Cache TTL in seconds",
    )
    rate_limit_enabled: bool = Field(
        default=False,
        alias="RATE_LIMIT_ENABLED",
        description="Enable rate limiting",
    )
    rate_limit_requests: int = Field(
        default=10,
        ge=1,
        le=1000,
        alias="RATE_LIMIT_REQUESTS",
        description="Requests per rate limit window",
    )
    rate_limit_window: int = Field(
        default=60,
        ge=1,
        le=3600,
        alias="RATE_LIMIT_WINDOW",
        description="Rate limit window in seconds",
    )


class APISettings(BaseSettings):
    """API server configuration."""

    model_config = SettingsConfigDict(
        env_prefix="API_",
        extra="ignore",
    )

    auth_mode: str = Field(
        default="none",
        description="API auth mode: 'none' or 'api_key'",
    )
    key_header: str = Field(
        default="x-api-key",
        description="Header name for API key",
    )
    allowed_origins: str = Field(
        default="",
        alias="ALLOWED_ORIGINS",
        description="Comma-separated CORS allowed origins",
    )

    @field_validator("auth_mode")
    @classmethod
    def validate_auth_mode(cls, v: str) -> str:
        """Validate auth mode."""
        v = v.lower().strip()
        if v not in ("none", "api_key"):
            raise ValueError(f"Invalid API_AUTH_MODE: {v}. Must be 'none' or 'api_key'")
        return v

    @property
    def origins_list(self) -> list:
        """Return allowed origins as a list."""
        if not self.allowed_origins:
            return []
        return [o.strip() for o in self.allowed_origins.split(",") if o.strip()]


class LLMSettings(BaseSettings):
    """LLM generation configuration."""

    model_config = SettingsConfigDict(
        env_prefix="DEFAULT_",
        extra="ignore",
    )

    num_ctx: int = Field(
        default=32768,
        ge=512,
        le=128000,
        description="LLM context window size",
    )
    num_predict: int = Field(
        default=512,
        ge=32,
        le=4096,
        description="Maximum response tokens",
    )
    retries: int = Field(
        default=2,
        ge=0,
        le=10,
        description="Default retry count",
    )
    connect_timeout: float = Field(
        default=3.0,
        ge=0.1,
        le=60.0,
        alias="CHAT_CONNECT_TIMEOUT",
        description="Chat connection timeout (seconds)",
    )
    read_timeout: float = Field(
        default=120.0,
        ge=1.0,
        le=600.0,
        alias="CHAT_READ_TIMEOUT",
        description="Chat read timeout (seconds)",
    )


class LoggingSettings(BaseSettings):
    """Logging configuration."""

    model_config = SettingsConfigDict(
        env_prefix="RAG_",
        extra="ignore",
    )

    log_enabled: bool = Field(
        default=False,
        alias="RAG_LOG_ENABLED",
        description="Enable query logging",
    )
    log_file: str = Field(
        default="rag_queries.jsonl",
        alias="RAG_LOG_FILE",
        description="Query log file path",
    )
    log_include_answer: bool = Field(
        default=True,
        alias="RAG_LOG_INCLUDE_ANSWER",
        description="Include answers in query log",
    )
    log_include_chunks: bool = Field(
        default=False,
        alias="RAG_LOG_INCLUDE_CHUNKS",
        description="Include chunk text in query log",
    )


class Settings(BaseSettings):
    """Main settings container aggregating all configuration groups.

    This class provides a single entry point for all validated configuration.
    Each nested group can be accessed as a property.
    """

    model_config = SettingsConfigDict(
        extra="ignore",
    )

    # Nested settings groups
    ollama: OllamaSettings = Field(default_factory=OllamaSettings)
    retrieval: RetrievalSettings = Field(default_factory=RetrievalSettings)
    embedding: EmbeddingSettings = Field(default_factory=EmbeddingSettings)
    ann: ANNSettings = Field(default_factory=ANNSettings)
    cache: CacheSettings = Field(default_factory=CacheSettings)
    api: APISettings = Field(default_factory=APISettings)
    llm: LLMSettings = Field(default_factory=LLMSettings)
    logging: LoggingSettings = Field(default_factory=LoggingSettings)

    def validate_all(self) -> list:
        """Validate all settings and return list of warnings.

        Returns:
            List of warning messages (empty if all valid)
        """
        warnings = []

        # Cross-field validations
        if self.retrieval.default_top_k > self.retrieval.max_top_k:
            warnings.append(f"DEFAULT_TOP_K ({self.retrieval.default_top_k}) > MAX_TOP_K ({self.retrieval.max_top_k})")

        if self.retrieval.chunk_overlap >= self.retrieval.chunk_chars:
            warnings.append(
                f"CHUNK_OVERLAP ({self.retrieval.chunk_overlap}) >= CHUNK_CHARS ({self.retrieval.chunk_chars})"
            )

        return warnings


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Get cached settings instance.

    Settings are loaded once and cached for the lifetime of the process.
    Use this function to access validated configuration.

    Returns:
        Validated Settings instance
    """
    return Settings()


def validate_settings() -> tuple:
    """Validate current settings and return status.

    Returns:
        Tuple of (is_valid: bool, warnings: list, errors: list)
    """
    errors = []
    warnings = []

    try:
        settings = get_settings()
        warnings = settings.validate_all()
        return (len(errors) == 0, warnings, errors)
    except Exception as e:
        errors.append(str(e))
        return (False, warnings, errors)


def print_settings_summary() -> None:
    """Print a summary of current settings to stdout."""
    try:
        settings = get_settings()
        print("=" * 60)
        print("CONFIGURATION SUMMARY (Pydantic Validated)")
        print("=" * 60)
        print(f"Ollama URL: {settings.ollama.ollama_url}")
        print(f"Chat Model: {settings.ollama.chat_model}")
        print(f"Embed Model: {settings.ollama.embed_model}")
        print(f"Embedding Backend: {settings.embedding.backend} ({settings.embedding.dim}-dim)")
        print(f"Chunk Size: {settings.retrieval.chunk_chars} chars")
        print(f"Top-K: {settings.retrieval.default_top_k} (max: {settings.retrieval.max_top_k})")
        print(f"Pack-Top: {settings.retrieval.default_pack_top}")
        print(f"Threshold: {settings.retrieval.default_threshold}")
        print(f"ANN: {settings.ann.use_ann}")
        print(f"Cache: {settings.cache.cache_maxsize} entries, {settings.cache.cache_ttl}s TTL")
        print(f"Rate Limit: {'enabled' if settings.cache.rate_limit_enabled else 'disabled'}")
        print("=" * 60)

        is_valid, warnings, errors = validate_settings()
        if warnings:
            print("WARNINGS:")
            for w in warnings:
                print(f"  ⚠ {w}")
        if errors:
            print("ERRORS:")
            for e in errors:
                print(f"  ❌ {e}")
        if is_valid and not warnings:
            print("✅ All settings valid")
    except Exception as e:
        print(f"❌ Failed to load settings: {e}")
