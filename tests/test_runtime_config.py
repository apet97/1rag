import numpy as np
import pytest

import clockify_rag.config as config
from clockify_rag import retrieval, embedding
from clockify_rag.utils import validate_and_set_config


@pytest.fixture(autouse=True)
def restore_config():
    original = {
        "OLLAMA_URL": config.OLLAMA_URL,
        "GEN_MODEL": config.GEN_MODEL,
        "EMB_MODEL": config.EMB_MODEL,
        "CTX_TOKEN_BUDGET": config.CTX_TOKEN_BUDGET,
        "EMB_BACKEND": config.EMB_BACKEND,
        "REFUSAL_STR": getattr(config, "REFUSAL_STR", None),
    }
    yield
    for key, value in original.items():
        if value is None:
            # Some configs (like REFUSAL_STR) may not exist in older setups
            if hasattr(config, key):
                delattr(config, key)
        else:
            setattr(config, key, value)


def test_pack_snippets_respects_runtime_budget():
    validate_and_set_config(ctx_budget="300")

    chunks = [
        {
            "id": "id_1",
            "title": "Title",
            "section": "Section",
            "text": "word " * 200,
        }
    ]

    block, ids, used = retrieval.pack_snippets(chunks, order=[0])

    assert ids == ["id_1"]
    assert used <= config.CTX_TOKEN_BUDGET
    assert len(block) > 0


def test_ask_llm_uses_runtime_config(monkeypatch):
    new_url = "http://localhost:2345"
    new_model = "my-gen-model"
    validate_and_set_config(ollama_url=new_url, gen_model=new_model)

    captured = {}

    class DummyResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"message": {"content": "ok"}}

    class DummySession:
        def post(self, url, json, timeout, allow_redirects):
            captured["url"] = url
            captured["json"] = json
            captured["timeout"] = timeout
            captured["allow_redirects"] = allow_redirects
            return DummyResponse()

    monkeypatch.setattr(retrieval, "get_session", lambda retries=None: DummySession())

    result = retrieval.ask_llm("question", "context")

    assert result == "ok"
    assert captured["url"] == f"{new_url}/api/chat"
    assert captured["json"]["model"] == new_model


def test_embed_query_uses_runtime_config(monkeypatch):
    new_url = "http://localhost:3456"
    new_emb_model = "my-emb-model"
    monkeypatch.setattr(config, "EMB_BACKEND", "ollama")
    validate_and_set_config(ollama_url=new_url, emb_model=new_emb_model)

    calls = {}

    class DummyEmbResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"embedding": [1.0, 0.0]}

    class DummySession:
        def post(self, url, json, timeout, allow_redirects):
            calls.setdefault("urls", []).append(url)
            calls.setdefault("models", []).append(json["model"])
            return DummyEmbResponse()

    monkeypatch.setattr(embedding, "get_session", lambda retries=None: DummySession())

    vec = embedding.embed_query("hello")

    assert pytest.approx(np.linalg.norm(vec), rel=1e-6) == 1.0
    assert calls["urls"] == [f"{new_url}/api/embeddings"]
    assert calls["models"] == [new_emb_model]


def test_system_prompt_reflects_runtime_refusal():
    original_refusal = getattr(config, "REFUSAL_STR", "")
    new_refusal = "PLEASE CONTACT SUPPORT"

    config.REFUSAL_STR = new_refusal

    prompt_from_function = retrieval.get_system_prompt()
    prompt_from_attr = retrieval.SYSTEM_PROMPT

    assert new_refusal in prompt_from_function
    assert new_refusal in prompt_from_attr

    # USER_WRAPPER should also embed the runtime refusal when formatted
    formatted_user = retrieval.USER_WRAPPER.format(
        snips="Snippet", q="Question?", refusal=config.REFUSAL_STR
    )
    assert new_refusal in formatted_user

    config.REFUSAL_STR = original_refusal
