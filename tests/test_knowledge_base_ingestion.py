from clockify_rag.chunking import build_chunks
from clockify_rag.retrieval import _article_key


def test_build_chunks_from_knowledge_base_dir(tmp_path):
    kb_dir = tmp_path / "knowledge_base" / "track-time-and-expenses"
    kb_dir.mkdir(parents=True)
    article_path = kb_dir / "timesheet-view.md"
    article_path.write_text(
        """---
title: "Timesheet view"
url: "https://clockify.me/help/track-time-and-expenses/timesheet-view"
category: "track-time-and-expenses"
slug: "timesheet-view"
---

## Timesheet view

Managers can review their team's time in Timesheet view.
""",
        encoding="utf-8",
    )

    chunks = build_chunks(str(tmp_path / "knowledge_base"))

    assert chunks, "Knowledge base directory should produce chunks"
    first = chunks[0]
    assert first["title"] == "Timesheet view"
    assert first["url"] == "https://clockify.me/help/track-time-and-expenses/timesheet-view"
    assert first["metadata"].get("category") == "track-time-and-expenses"
    assert first["metadata"].get("slug") == "timesheet-view"
    assert first["doc_path"] == str(article_path)
    assert first["text"].startswith("Context: Timesheet view")
    assert _article_key(first) == first["url"]
