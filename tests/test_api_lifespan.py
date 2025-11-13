from fastapi.testclient import TestClient

import clockify_rag.api as api_module
from clockify_rag.exceptions import IndexLoadError


def test_create_app_lifespan_runs(monkeypatch):
    """create_app should initialize without raising during FastAPI lifespan."""

    monkeypatch.setattr(api_module, "ensure_index_ready", lambda retries=2: None)

    app = api_module.create_app()

    # entering the TestClient context runs the app lifespan (startup/shutdown)
    with TestClient(app):
        pass


def test_startup_handles_index_load_error(monkeypatch):
    """API startup should degrade gracefully when index artifacts are missing."""

    error_message = "artifacts missing"

    def failing_ensure(retries=2):
        raise IndexLoadError(error_message)

    monkeypatch.setattr(api_module, "ensure_index_ready", failing_ensure)

    app = api_module.create_app()

    with TestClient(app) as client:
        assert app.state.index_ready is False
        assert app.state.index_error == error_message

        health = client.get("/health")
        assert health.status_code == 200
        payload = health.json()
        assert payload["status"] == "unavailable"
        assert payload["index_ready"] is False

        query = client.post("/v1/query", json={"question": "ping"})
        assert query.status_code == 503
        assert error_message in query.json()["detail"]
