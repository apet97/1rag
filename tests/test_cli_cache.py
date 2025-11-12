"""Tests for CLI cache plumbing."""

from argparse import Namespace

import clockify_rag.cli as cli_module
from clockify_rag.caching import serialize_result_for_cache


class CacheStub:
    """Minimal cache stub that mimics QueryCache API for tests."""

    def __init__(self, hit=None):
        self.cache = {}
        self.hit = hit
        self.loaded_paths = []
        self.saved_paths = []
        self.put_calls = []

    def load(self, path=None):
        self.loaded_paths.append(path)
        return len(self.cache)

    def save(self, path=None):
        self.saved_paths.append(path)
        return len(self.cache)

    def get(self, *_args, **_kwargs):
        return self.hit

    def put(self, *args, **kwargs):
        self.put_calls.append((args, kwargs))
        return None


def _cached_payload():
    """Helper to build a serialized cache payload."""

    snapshot = {
        "metadata": {"used_tokens": 5},
        "selected_chunks": [42],
        "packed_chunks": [42],
        "context_block": "",
        "confidence": 0.91,
        "routing": {"intent": "faq"},
        "timing": {"total_ms": 12},
        "refused": False,
    }
    return serialize_result_for_cache(snapshot)


def test_chat_repl_cache_hit_skips_answer_once(monkeypatch, capsys):
    """Repeated questions should short-circuit the expensive answer pipeline."""

    monkeypatch.setattr(cli_module, "_log_config_summary", lambda **_: None)
    monkeypatch.setattr(cli_module, "warmup_on_startup", lambda: None)
    monkeypatch.setattr(cli_module, "ensure_index_ready", lambda **_: ([], [], {}, None))
    monkeypatch.setattr(cli_module, "get_precomputed_cache", lambda *_args, **_kwargs: None)

    cache = CacheStub(hit=("Cached answer", _cached_payload()))
    monkeypatch.setattr(cli_module, "get_query_cache", lambda: cache)

    def fail_answer(*_args, **_kwargs):
        raise AssertionError("answer_once should not run on cache hit")

    monkeypatch.setattr(cli_module, "answer_once", fail_answer)

    inputs = iter(["Cached question", ":exit"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(inputs))

    cli_module.chat_repl(debug=True)

    output = capsys.readouterr().out
    assert "Cached answer" in output
    assert "cache_status': 'hit'" in output  # Debug metadata should surface cache hit
    assert cache.put_calls == []


def test_handle_ask_command_cache_hit(monkeypatch, capsys):
    """The ask command should reuse cached answers and skip retrieval."""

    monkeypatch.setattr(cli_module, "_log_config_summary", lambda **_: None)

    cache = CacheStub(hit=("Cached answer", _cached_payload()))
    monkeypatch.setattr(cli_module, "get_query_cache", lambda: cache)
    def fail_index(*_args, **_kwargs):
        raise AssertionError("should not load index")

    def fail_answer(*_args, **_kwargs):
        raise AssertionError("answer_once should not run")

    monkeypatch.setattr(cli_module, "ensure_index_ready", fail_index)
    monkeypatch.setattr(cli_module, "answer_once", fail_answer)

    args = Namespace(
        question="Cached question",
        topk=3,
        pack=2,
        threshold=0.1,
        rerank=False,
        seed=42,
        num_ctx=1024,
        num_predict=128,
        retries=0,
        json=False,
        debug=True,
        query_cache_path="/tmp/test-cache.json",
    )

    cli_module.handle_ask_command(args)

    output = capsys.readouterr().out
    assert "Cached answer" in output
    assert cache.put_calls == []
    assert cache.saved_paths == []  # Nothing new persisted on hit
    assert cache.loaded_paths == [args.query_cache_path]
