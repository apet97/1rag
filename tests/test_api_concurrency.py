import asyncio
import time

import pytest
import httpx
from asgi_lifespan import LifespanManager

import clockify_rag.api as api_module


@pytest.mark.asyncio
async def test_concurrent_query_and_health(monkeypatch):
    """Ensure slow blocking helpers do not block the event loop."""

    def ready_index(retries=0, **_):
        return ([{"id": 1, "text": "chunk"}], None, {"idf": {}}, None)

    monkeypatch.setattr(api_module, "ensure_index_ready", ready_index)

    def slow_answer(*args, **kwargs):
        time.sleep(0.2)
        return {"answer": "ok", "selected_chunks": [], "metadata": {}}

    monkeypatch.setattr(api_module, "answer_once", slow_answer)

    def slow_connectivity(url, timeout):
        time.sleep(0.2)
        return url

    monkeypatch.setattr(api_module, "check_ollama_connectivity", slow_connectivity)

    app = api_module.create_app()

    elapsed = None

    async with LifespanManager(app):
        async with httpx.ASGITransport(app=app) as transport:
            async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
                start = time.perf_counter()

                async def do_query(i: int):
                    response = await client.post(
                        "/v1/query", json={"question": f"question {i}"}
                    )
                    assert response.status_code == 200
                    return response

                async def do_health():
                    response = await client.get("/health")
                    assert response.status_code == 200
                    return response

                await asyncio.gather(
                    do_query(1),
                    do_query(2),
                    do_health(),
                    do_health(),
                )

                elapsed = time.perf_counter() - start

    assert elapsed is not None and elapsed < 0.6, f"Requests executed too slowly: {elapsed:.2f}s"
