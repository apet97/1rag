import pytest
from fastapi.testclient import TestClient

import clockify_rag.api as api_module
from clockify_rag.exceptions import ValidationError


def test_api_query_returns_metadata(monkeypatch):
    """API should expose metadata from the new answer_once result schema."""

    fake_chunks = [
        {"id": "chunk-001", "title": "Track Time", "section": "Overview"},
        {"id": "chunk-002", "title": "Track Time", "section": "Steps"},
    ]

    monkeypatch.setattr(api_module, "ensure_index_ready", lambda retries=2: (fake_chunks, [], {}, None))

    result_payload = {
        "answer": "Mocked answer",
        "confidence": 0.91,
        "selected_chunks": [
            {"id": "chunk-001", "title": "Track Time", "section": "Overview"},
            {"index": 1},
            {"chunk_id": "chunk-legacy"},
        ],
        "metadata": {"used_tokens": 128, "retrieval_count": 3},
        "routing": {"action": "self-serve"},
    }

    monkeypatch.setattr(api_module, "answer_once", lambda *_, **__: result_payload)

    app = api_module.create_app()

    with TestClient(app) as client:
        response = client.post(
            "/v1/query",
            json={"question": "How do I track time?"},
        )

        assert response.status_code == 200
        payload = response.json()

        assert payload["answer"] == result_payload["answer"]
        assert payload["metadata"]["used_tokens"] == result_payload["metadata"]["used_tokens"]
        assert payload["routing"] == result_payload["routing"]

        assert payload["sources"] == [
            {"id": "chunk-001", "title": "Track Time", "section": "Overview"},
            {"id": "chunk-002", "title": "Track Time", "section": "Steps"},
            {"id": "chunk-legacy", "title": None, "section": None},
        ]


def test_api_query_respects_privacy_mode(monkeypatch):
    """When privacy mode is enabled, redact source metadata."""

    fake_chunks = [
        {"id": "chunk-101", "title": "Hidden Title", "section": "Hidden Section"},
    ]

    monkeypatch.setattr(api_module.config, "API_PRIVACY_MODE", True, raising=False)
    monkeypatch.setattr(api_module, "ensure_index_ready", lambda retries=2: (fake_chunks, [], {}, None))

    result_payload = {
        "answer": "Confidential",
        "selected_chunks": [0, {"id": "chunk-202", "title": "Leak"}],
        "metadata": {},
    }

    monkeypatch.setattr(api_module, "answer_once", lambda *_, **__: result_payload)

    app = api_module.create_app()

    with TestClient(app) as client:
        response = client.post(
            "/v1/query",
            json={"question": "Is privacy respected?"},
        )

        assert response.status_code == 200
        payload = response.json()

    assert payload["sources"] == [
        {"id": "chunk-101", "title": None, "section": None},
        {"id": "chunk-202", "title": None, "section": None},
    ]


@pytest.mark.parametrize(
    "question,message",
    [
        ("bad-empty", "Query cannot be empty"),
        (
            "bad-long",
            "Query too long (12001 chars). Maximum allowed: 12000 chars. Set MAX_QUERY_LENGTH env var to override.",
        ),
    ],
)
def test_api_query_validation_errors(monkeypatch, question, message):
    """API should convert validation errors into 400 responses."""

    monkeypatch.setattr(api_module, "ensure_index_ready", lambda retries=2: ([], [], {}, None))

    def fake_answer(q, *_args, **_kwargs):
        assert q == question
        raise ValidationError(message)

    monkeypatch.setattr(api_module, "answer_once", fake_answer)

    app = api_module.create_app()

    with TestClient(app) as client:
        response = client.post("/v1/query", json={"question": question})

    assert response.status_code == 400
    assert response.json()["detail"] == message
