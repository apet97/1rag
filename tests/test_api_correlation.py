"""Integration tests for correlation ID middleware."""

from fastapi.testclient import TestClient


def test_correlation_id_on_success_response():
    """Correlation ID header present on successful responses."""
    from clockify_rag.api import create_app

    app = create_app()
    client = TestClient(app)
    resp = client.get("/health")
    assert "x-correlation-id" in resp.headers
    assert len(resp.headers["x-correlation-id"]) == 32  # UUID hex


def test_correlation_id_on_404_error():
    """Correlation ID header present on 404 errors."""
    from clockify_rag.api import create_app

    app = create_app()
    client = TestClient(app)
    resp = client.get("/nonexistent-endpoint-xyz")
    assert resp.status_code == 404
    assert "x-correlation-id" in resp.headers


def test_correlation_id_passthrough():
    """Client-provided correlation ID is echoed back."""
    from clockify_rag.api import create_app

    app = create_app()
    client = TestClient(app)
    resp = client.get("/health", headers={"x-correlation-id": "test-abc-123"})
    assert resp.headers["x-correlation-id"] == "test-abc-123"


def test_invalid_correlation_id_rejected():
    """Invalid correlation IDs are replaced with generated ones."""
    from clockify_rag.api import create_app

    app = create_app()
    client = TestClient(app)
    resp = client.get("/health", headers={"x-correlation-id": "test<script>bad"})
    # Should NOT echo back the malicious ID
    assert resp.headers["x-correlation-id"] != "test<script>bad"
    assert len(resp.headers["x-correlation-id"]) == 32


def test_oversized_correlation_id_rejected():
    """Correlation IDs exceeding max length are replaced."""
    from clockify_rag.api import create_app

    app = create_app()
    client = TestClient(app)
    oversized_id = "a" * 100  # 100 chars, exceeds 64 char limit
    resp = client.get("/health", headers={"x-correlation-id": oversized_id})
    # Should NOT echo back the oversized ID
    assert resp.headers["x-correlation-id"] != oversized_id
    assert len(resp.headers["x-correlation-id"]) == 32


def test_x_request_id_also_accepted():
    """X-Request-ID header is accepted as correlation ID."""
    from clockify_rag.api import create_app

    app = create_app()
    client = TestClient(app)
    resp = client.get("/health", headers={"x-request-id": "req-12345"})
    assert resp.headers["x-correlation-id"] == "req-12345"
