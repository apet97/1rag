"""Helpers for emitting sanitized query logging and metrics events."""

from __future__ import annotations

import logging
from typing import Any, Dict, Optional

from . import config
from .caching import log_query
from .utils import log_query_metrics, sanitize_for_log

logger = logging.getLogger(__name__)


def record_query_telemetry(
    question: str,
    result: Dict[str, Any],
    *,
    latency_ms: Optional[float] = None,
    source: str = "cli",
) -> None:
    """Emit structured query logs and metrics if logging is enabled.

    Args:
        question: Original question string from the user.
        result: Payload returned from ``answer_once``.
        latency_ms: Optional explicit latency override (milliseconds).
        source: Human-readable source identifier (e.g., ``cli.ask``).
    """

    if getattr(config, "QUERY_LOG_DISABLED", False):
        return

    sanitized_question = sanitize_for_log(question, max_length=2000)
    answer_text = result.get("answer", "") or ""
    sanitized_answer = sanitize_for_log(answer_text, max_length=5000)
    timing = result.get("timing") or {}
    duration = latency_ms if latency_ms is not None else timing.get("total_ms")
    if duration is None:
        duration = 0.0

    metadata = dict(result.get("metadata") or {})
    metadata.setdefault("source", source)
    routing = result.get("routing")
    retrieved_chunks = result.get("selected_chunks") or []

    try:
        log_query(
            query=sanitized_question,
            answer=sanitized_answer,
            retrieved_chunks=retrieved_chunks,
            latency_ms=float(duration),
            refused=result.get("refused", False),
            metadata=metadata,
        )
    except Exception:  # pragma: no cover - defensive
        logger.exception("Failed to write query log entry")

    try:
        log_query_metrics(
            question=sanitized_question,
            answer=sanitized_answer,
            confidence=result.get("confidence"),
            timing=timing,
            metadata=metadata,
            routing=routing,
        )
    except Exception:  # pragma: no cover - defensive
        logger.exception("Failed to emit query metrics entry")
