"""Tests for the prompts module."""

import pytest
from clockify_rag.prompts import QWEN_SYSTEM_PROMPT, build_rag_user_prompt


def test_system_prompt_contains_key_phrases():
    """Test that the system prompt contains essential instructions."""
    # Check for key phrases that define the role and behavior
    assert "Clockify" in QWEN_SYSTEM_PROMPT
    assert "CAKE.com" in QWEN_SYSTEM_PROMPT
    assert "CONTEXT" in QWEN_SYSTEM_PROMPT
    assert "internal support" in QWEN_SYSTEM_PROMPT.lower()
    assert "source of truth" in QWEN_SYSTEM_PROMPT.lower()


def test_build_rag_user_prompt_with_basic_chunks():
    """Test basic user prompt building with minimal chunk data."""
    chunks = [
        {"id": "chunk_1", "text": "This is the first chunk content."},
        {"id": "chunk_2", "text": "This is the second chunk content."},
    ]
    question = "How do I track time?"

    prompt = build_rag_user_prompt(question, chunks)

    # Check that prompt includes context blocks
    assert "[CONTEXT_BLOCK id=1]" in prompt
    assert "[CONTEXT_BLOCK id=2]" in prompt

    # Check that chunk content is included
    assert "This is the first chunk content." in prompt
    assert "This is the second chunk content." in prompt

    # Check that question is included
    assert "How do I track time?" in prompt
    assert "USER QUESTION" in prompt


def test_build_rag_user_prompt_with_metadata():
    """Test user prompt building with full chunk metadata."""
    chunks = [
        {
            "id": "chunk_1",
            "text": "Track time using the timer.",
            "title": "Time Tracking Guide",
            "url": "https://support.clockify.me/articles/123",
            "section": "Getting Started",
        },
        {
            "id": "chunk_2",
            "text": "Enter time manually in the time tracker.",
            "title": "Manual Time Entry",
            "url": "https://support.clockify.me/articles/456",
            "section": "Advanced Features",
        },
    ]
    question = "What are the ways to track time?"

    prompt = build_rag_user_prompt(question, chunks)

    # Check context blocks
    assert "[CONTEXT_BLOCK id=1]" in prompt
    assert "[CONTEXT_BLOCK id=2]" in prompt

    # Check metadata is included
    assert "source: https://support.clockify.me/articles/123" in prompt
    assert "title: Time Tracking Guide" in prompt
    assert "section: Getting Started" in prompt
    assert "source: https://support.clockify.me/articles/456" in prompt
    assert "title: Manual Time Entry" in prompt
    assert "section: Advanced Features" in prompt

    # Check content
    assert "Track time using the timer." in prompt
    assert "Enter time manually in the time tracker." in prompt

    # Check instructions
    assert "INSTRUCTIONS:" in prompt
    assert "primary source of truth" in prompt.lower()
    assert "TASK:" in prompt


def test_build_rag_user_prompt_with_partial_metadata():
    """Test prompt building when chunks have only some metadata fields."""
    chunks = [
        {
            "id": "chunk_1",
            "text": "Content here.",
            "title": "Article Title",
            # No URL or section
        },
        {
            "id": "chunk_2",
            "text": "More content.",
            "url": "https://example.com",
            # No title or section
        },
    ]
    question = "Test question?"

    prompt = build_rag_user_prompt(question, chunks)

    # Should include available metadata
    assert "title: Article Title" in prompt
    assert "source: https://example.com" in prompt

    # Should not crash on missing metadata
    assert "[CONTEXT_BLOCK id=1]" in prompt
    assert "[CONTEXT_BLOCK id=2]" in prompt


def test_build_rag_user_prompt_with_empty_chunks():
    """Test prompt building with empty chunk list."""
    chunks = []
    question = "What happens with no context?"

    prompt = build_rag_user_prompt(question, chunks)

    # Should still include question and structure
    assert "What happens with no context?" in prompt
    assert "USER QUESTION" in prompt
    assert "CONTEXT_BLOCKS" in prompt


def test_build_rag_user_prompt_includes_citations_instruction():
    """Test that the prompt instructs the model to include citations."""
    chunks = [
        {"id": "test_chunk", "text": "Test content."},
    ]
    question = "Test?"

    prompt = build_rag_user_prompt(question, chunks)

    # Check citation instructions
    assert "citations" in prompt.lower() or "id=" in prompt
    assert "[id=" in prompt  # Example citation format


def test_system_prompt_structure():
    """Test that the system prompt has the expected structure."""
    # Should have main sections
    assert "PRIMARY ROLE" in QWEN_SYSTEM_PROMPT
    assert "KNOWLEDGE & SCOPE" in QWEN_SYSTEM_PROMPT
    assert "RAG BEHAVIOR" in QWEN_SYSTEM_PROMPT
    assert "STYLE & FORMAT" in QWEN_SYSTEM_PROMPT
    assert "OUTPUT RULES" in QWEN_SYSTEM_PROMPT

    # Should emphasize importance of context
    assert "VERY IMPORTANT" in QWEN_SYSTEM_PROMPT
