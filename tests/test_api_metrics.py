"""Tests for /v1/metrics endpoint outputs."""

from fastapi.testclient import TestClient

import clockify_rag.api as api_module
from clockify_rag.metrics import MetricNames, get_metrics


def _create_test_app(monkeypatch):
    monkeypatch.setattr(api_module, "ensure_index_ready", lambda retries=2: ([], [], {}, None))
    return api_module.create_app()


def test_metrics_endpoint_returns_json_summary(monkeypatch):
    """JSON response should include counters, summary, and app metadata."""

    collector = get_metrics()
    collector.reset()
    collector.increment_counter(MetricNames.QUERIES_TOTAL, labels={"interface": "test"})

    app = _create_test_app(monkeypatch)

    with TestClient(app) as client:
        resp = client.get("/v1/metrics")

    assert resp.status_code == 200
    payload = resp.json()
    assert "counters" in payload
    assert any(key.startswith(MetricNames.QUERIES_TOTAL) for key in payload["counters"].keys())
    assert "summary" in payload
    assert "app" in payload
    assert "index_ready" in payload["app"]


def test_metrics_endpoint_supports_prometheus(monkeypatch):
    """Prometheus format should render text output."""

    collector = get_metrics()
    collector.reset()
    collector.increment_counter(MetricNames.QUERIES_TOTAL)

    app = _create_test_app(monkeypatch)

    with TestClient(app) as client:
        resp = client.get("/v1/metrics", params={"format": "prometheus"})

    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("text/plain")
    assert MetricNames.QUERIES_TOTAL in resp.text
