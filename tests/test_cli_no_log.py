"""Regression tests for the --no-log flag."""

import argparse

import clockify_rag.cli as cli_module
import clockify_rag.config as config_module
import clockify_rag.query_logging as telemetry


def test_handle_ask_command_respects_no_log(monkeypatch):
    """Ensure query logging is skipped when --no-log is supplied."""

    # Start from a clean logging state
    monkeypatch.setattr(config_module, "QUERY_LOG_DISABLED", False, raising=False)

    args = argparse.Namespace(
        cmd="ask",
        log="INFO",
        query_expansions=None,
        emb_backend=config_module.EMB_BACKEND,
        ann=config_module.USE_ANN,
        alpha=config_module.ALPHA_HYBRID,
        faiss_multiplier=config_module.FAISS_CANDIDATE_MULTIPLIER,
        ollama_url=None,
        gen_model=None,
        emb_model=None,
        ctx_budget=None,
        no_log=True,
        question="How do I export time entries?",
        rerank=False,
        pack=4,
        seed=42,
        threshold=0.25,
        topk=6,
        num_ctx=1024,
        num_predict=128,
        retries=0,
        json=False,
        debug=False,
    )

    # Avoid disk/network operations during configure step
    monkeypatch.setattr(cli_module, "set_query_expansion_path", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(cli_module, "load_query_expansion_dict", lambda **_kwargs: None)
    monkeypatch.setattr(cli_module, "validate_and_set_config", lambda **_kwargs: None)
    monkeypatch.setattr(cli_module, "validate_chunk_config", lambda: None)
    monkeypatch.setattr(cli_module, "check_pytorch_mps", lambda: None)

    disabled = cli_module.configure_logging_and_config(args)
    assert disabled is True
    assert config_module.QUERY_LOG_DISABLED is True

    # Stub heavy dependencies inside the handler
    monkeypatch.setattr(cli_module, "ensure_index_ready", lambda **_kwargs: ([], None, None, None))
    sample_result = {
        "answer": "Use the export button on the detailed report.",
        "selected_chunks": [
            {"id": "chunk-1", "chunk": "Sensitive KB text", "dense": 0.9, "bm25": 0.8, "hybrid": 0.85}
        ],
        "metadata": {"retrieval_count": 1, "packed_count": 1},
        "timing": {"total_ms": 42.0},
        "refused": False,
        "confidence": 0.67,
        "routing": {"action": "self_service", "level": "green"},
    }
    monkeypatch.setattr(cli_module, "answer_once", lambda *args, **kwargs: sample_result)

    log_calls = []
    metric_calls = []
    monkeypatch.setattr(telemetry, "log_query", lambda *a, **k: log_calls.append((a, k)))
    monkeypatch.setattr(telemetry, "log_query_metrics", lambda *a, **k: metric_calls.append((a, k)))

    cli_module.handle_ask_command(args)

    assert not log_calls, "log_query should not run when logging is disabled"
    assert not metric_calls, "log_query_metrics should not run when logging is disabled"
