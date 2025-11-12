"""Tests for the Prometheus metrics endpoint."""

from fastapi.testclient import TestClient

import clockify_rag.api as api_module
from clockify_rag.metrics import get_metrics, MetricNames


def test_metrics_endpoint_emits_prometheus_text():
    """/v1/metrics should expose Prometheus formatted metrics with KPIs."""

    collector = get_metrics()
    collector.reset()
    collector.increment_counter(MetricNames.QUERIES_TOTAL, 2)
    collector.observe_histogram(MetricNames.QUERY_LATENCY, 123.0)

    app = api_module.create_app()

    with TestClient(app) as client:
        response = client.get("/v1/metrics")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/plain; version=0.0.4; charset=utf-8"

    body = response.text
    assert "# TYPE queries_total counter" in body
    assert ("queries_total 2" in body) or ("queries_total 2.0" in body)
    assert f"{MetricNames.QUERY_LATENCY}_count" in body
    assert f"{MetricNames.QUERY_LATENCY}_sum" in body
    assert "quantile=\"0.5\"" in body
