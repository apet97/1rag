import os
from pathlib import Path

from clockify_rag.utils import resolve_corpus_path


def test_prefers_primary_corpus_when_present(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    primary = tmp_path / "clockify_help_corpus.en.md"
    primary.write_text("primary")

    path, exists, candidates = resolve_corpus_path()

    assert exists is True
    assert Path(path).name == "clockify_help_corpus.en.md"
    assert "clockify_help_corpus.en.md" in candidates


def test_falls_back_to_legacy_when_primary_missing(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    legacy = tmp_path / "knowledge_full.md"
    legacy.write_text("legacy")

    path, exists, candidates = resolve_corpus_path()

    assert exists is True
    assert Path(path).name == "knowledge_full.md"
    assert "knowledge_full.md" in candidates


def test_returns_first_candidate_when_none_exist(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    path, exists, candidates = resolve_corpus_path()

    assert exists is False
    # Default ordering keeps primary first
    assert Path(path).name == "clockify_help_corpus.en.md"
    assert candidates[0] == "clockify_help_corpus.en.md"
