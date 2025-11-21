"""Tests for Qwen JSON output contract validation.

This module tests the JSON schema validation for Qwen's structured output.
These tests are critical for CI - any breaking change to the prompt contract
will be caught here.
"""

import json
import pytest

from clockify_rag.answer import parse_qwen_json


class TestQwenJSONContract:
    """Test Qwen JSON output schema validation."""

    def test_parse_valid_qwen_json_happy_path(self):
        """Test parsing a valid, well-formed Qwen JSON response."""
        valid_json = json.dumps(
            {
                "answer": "To track time in Clockify, click the timer button.",
                "confidence": 95,
                "reasoning": "This answer is based on context blocks 1 and 3 which explicitly describe the timer functionality.",
                "sources_used": ["1", "3"],
            }
        )

        result = parse_qwen_json(valid_json)

        assert result["answer"] == "To track time in Clockify, click the timer button."
        assert result["confidence"] == 95
        assert (
            result["reasoning"]
            == "This answer is based on context blocks 1 and 3 which explicitly describe the timer functionality."
        )
        assert result["sources_used"] == ["1", "3"]

    def test_parse_json_with_markdown_code_blocks(self):
        """Test parsing JSON wrapped in markdown code blocks."""
        wrapped_json = """```json
{
  "answer": "Test answer",
  "confidence": 80,
  "reasoning": "Test reasoning",
  "sources_used": ["1", "2"]
}
```"""

        result = parse_qwen_json(wrapped_json)

        assert result["answer"] == "Test answer"
        assert result["confidence"] == 80

    def test_parse_json_with_incomplete_code_blocks(self):
        """Test parsing JSON with incomplete markdown markers."""
        wrapped_json = """```json
{
  "answer": "Test answer",
  "confidence": 75,
  "reasoning": "Test reasoning",
  "sources_used": []
}"""

        result = parse_qwen_json(wrapped_json)

        assert result["answer"] == "Test answer"
        assert result["confidence"] == 75
        assert result["sources_used"] == []

    def test_parse_json_with_markdown_in_answer(self):
        """Test that answer field can contain Markdown formatting."""
        valid_json = json.dumps(
            {
                "answer": "## How to Track Time\n\n1. Click the timer\n2. Enter task name\n3. Press start\n\n**Note:** Use tags for better organization.",
                "confidence": 90,
                "reasoning": "Based on comprehensive documentation in context 1.",
                "sources_used": ["1"],
            }
        )

        result = parse_qwen_json(valid_json)

        assert "## How to Track Time" in result["answer"]
        assert "**Note:**" in result["answer"]

    def test_parse_json_with_empty_sources(self):
        """Test parsing when sources_used is an empty list."""
        valid_json = json.dumps(
            {
                "answer": "I don't have enough information to answer this question. Please check the Clockify help documentation or contact support.",
                "confidence": 15,
                "reasoning": "None of the context blocks contained relevant information about this specific feature.",
                "sources_used": [],
            }
        )

        result = parse_qwen_json(valid_json)

        assert result["confidence"] == 15
        assert result["sources_used"] == []

    def test_parse_invalid_json_raises_error(self):
        """Test that malformed JSON raises JSONDecodeError."""
        invalid_json = "{answer: 'missing quotes', confidence: 50}"

        with pytest.raises(json.JSONDecodeError):
            parse_qwen_json(invalid_json)

    def test_parse_non_dict_json_raises_error(self):
        """Test that JSON array or primitive raises ValueError."""
        json_array = json.dumps(["answer", "confidence", "reasoning", "sources"])

        with pytest.raises(ValueError, match="Expected JSON object"):
            parse_qwen_json(json_array)

    def test_parse_missing_required_field_answer(self):
        """Test that missing 'answer' field raises ValueError."""
        incomplete_json = json.dumps(
            {
                "confidence": 80,
                "reasoning": "Test reasoning",
                "sources_used": ["1"],
            }
        )

        with pytest.raises(ValueError, match="Missing required fields.*answer"):
            parse_qwen_json(incomplete_json)

    def test_parse_missing_required_field_confidence(self):
        """Test that missing 'confidence' field raises ValueError."""
        incomplete_json = json.dumps(
            {
                "answer": "Test answer",
                "reasoning": "Test reasoning",
                "sources_used": ["1"],
            }
        )

        with pytest.raises(ValueError, match="Missing required fields.*confidence"):
            parse_qwen_json(incomplete_json)

    def test_parse_missing_required_field_reasoning(self):
        """Test that missing 'reasoning' field raises ValueError."""
        incomplete_json = json.dumps(
            {
                "answer": "Test answer",
                "confidence": 80,
                "sources_used": ["1"],
            }
        )

        with pytest.raises(ValueError, match="Missing required fields.*reasoning"):
            parse_qwen_json(incomplete_json)

    def test_parse_missing_required_field_sources_used(self):
        """Test that missing 'sources_used' field raises ValueError."""
        incomplete_json = json.dumps(
            {
                "answer": "Test answer",
                "confidence": 80,
                "reasoning": "Test reasoning",
            }
        )

        with pytest.raises(ValueError, match="Missing required fields.*sources_used"):
            parse_qwen_json(incomplete_json)

    def test_parse_invalid_answer_type(self):
        """Test that non-string 'answer' field raises ValueError."""
        invalid_json = json.dumps(
            {
                "answer": 12345,  # Should be string
                "confidence": 80,
                "reasoning": "Test reasoning",
                "sources_used": ["1"],
            }
        )

        with pytest.raises(ValueError, match="Field 'answer' must be string"):
            parse_qwen_json(invalid_json)

    def test_parse_invalid_confidence_type(self):
        """Test that non-integer 'confidence' field raises ValueError."""
        invalid_json = json.dumps(
            {
                "answer": "Test answer",
                "confidence": "high",  # Should be integer
                "reasoning": "Test reasoning",
                "sources_used": ["1"],
            }
        )

        with pytest.raises(ValueError, match="Field 'confidence' must be integer"):
            parse_qwen_json(invalid_json)

    def test_parse_confidence_out_of_range_too_low(self):
        """Test that confidence < 0 raises ValueError."""
        invalid_json = json.dumps(
            {
                "answer": "Test answer",
                "confidence": -10,
                "reasoning": "Test reasoning",
                "sources_used": ["1"],
            }
        )

        with pytest.raises(ValueError, match="Field 'confidence' must be in range 0-100"):
            parse_qwen_json(invalid_json)

    def test_parse_confidence_out_of_range_too_high(self):
        """Test that confidence > 100 raises ValueError."""
        invalid_json = json.dumps(
            {
                "answer": "Test answer",
                "confidence": 150,
                "reasoning": "Test reasoning",
                "sources_used": ["1"],
            }
        )

        with pytest.raises(ValueError, match="Field 'confidence' must be in range 0-100"):
            parse_qwen_json(invalid_json)

    def test_parse_confidence_boundary_values(self):
        """Test that confidence at boundaries (0, 100) is valid."""
        # Test confidence = 0
        json_low = json.dumps(
            {
                "answer": "No answer",
                "confidence": 0,
                "reasoning": "No context",
                "sources_used": [],
            }
        )
        result_low = parse_qwen_json(json_low)
        assert result_low["confidence"] == 0

        # Test confidence = 100
        json_high = json.dumps(
            {
                "answer": "Perfect answer",
                "confidence": 100,
                "reasoning": "All context present",
                "sources_used": ["1", "2", "3"],
            }
        )
        result_high = parse_qwen_json(json_high)
        assert result_high["confidence"] == 100

    def test_parse_confidence_float_converted_to_int(self):
        """Test that float confidence is converted to int."""
        json_with_float = json.dumps(
            {
                "answer": "Test answer",
                "confidence": 85.5,
                "reasoning": "Test reasoning",
                "sources_used": ["1"],
            }
        )

        result = parse_qwen_json(json_with_float)
        assert result["confidence"] == 85
        assert isinstance(result["confidence"], int)

    def test_parse_invalid_reasoning_type(self):
        """Test that non-string 'reasoning' field raises ValueError."""
        invalid_json = json.dumps(
            {
                "answer": "Test answer",
                "confidence": 80,
                "reasoning": ["Based on context 1"],  # Should be string
                "sources_used": ["1"],
            }
        )

        with pytest.raises(ValueError, match="Field 'reasoning' must be string"):
            parse_qwen_json(invalid_json)

    def test_parse_invalid_sources_used_type(self):
        """Test that non-list 'sources_used' field raises ValueError."""
        invalid_json = json.dumps(
            {
                "answer": "Test answer",
                "confidence": 80,
                "reasoning": "Test reasoning",
                "sources_used": "1, 2, 3",  # Should be list
            }
        )

        with pytest.raises(ValueError, match="Field 'sources_used' must be list"):
            parse_qwen_json(invalid_json)

    def test_parse_invalid_sources_used_element_type(self):
        """Test that non-string elements in 'sources_used' raise ValueError."""
        invalid_json = json.dumps(
            {
                "answer": "Test answer",
                "confidence": 80,
                "reasoning": "Test reasoning",
                "sources_used": [1, 2, 3],  # Should be strings
            }
        )

        with pytest.raises(ValueError, match="Field 'sources_used\\[0\\]' must be string"):
            parse_qwen_json(invalid_json)

    def test_parse_sources_used_with_empty_string_raises_error(self):
        """Test that empty or whitespace-only sources are rejected."""
        invalid_json = json.dumps(
            {
                "answer": "Test answer",
                "confidence": 80,
                "reasoning": "Test reasoning",
                "sources_used": [" "],  # Empty after stripping
            }
        )

        with pytest.raises(ValueError, match="sources_used\\[0\\].*empty"):
            parse_qwen_json(invalid_json)

    def test_parse_sources_used_with_mixed_types(self):
        """Test that mixed types in sources_used raise ValueError."""
        invalid_json = json.dumps(
            {
                "answer": "Test answer",
                "confidence": 80,
                "reasoning": "Test reasoning",
                "sources_used": ["1", 2, "3"],  # Mixed types
            }
        )

        with pytest.raises(ValueError, match="Field 'sources_used\\[1\\]' must be string"):
            parse_qwen_json(invalid_json)

    def test_parse_json_with_extra_fields_ignored(self):
        """Test that extra fields in JSON are ignored (forward compatibility)."""
        json_with_extra = json.dumps(
            {
                "answer": "Test answer",
                "confidence": 85,
                "reasoning": "Test reasoning",
                "sources_used": ["1"],
                "extra_field": "This should be ignored",
                "another_extra": 12345,
            }
        )

        result = parse_qwen_json(json_with_extra)

        # Should parse successfully and return only expected fields
        assert result["answer"] == "Test answer"
        assert result["confidence"] == 85
        assert "extra_field" not in result
        assert "another_extra" not in result

    def test_parse_json_with_unicode_content(self):
        """Test that Unicode characters in content are preserved."""
        unicode_json = json.dumps(
            {
                "answer": "Pour suivre le temps: cliquez sur le chronomètre. 时间跟踪。",
                "confidence": 90,
                "reasoning": "Basé sur le contexte français et chinois.",
                "sources_used": ["français-1", "中文-2"],
            },
            ensure_ascii=False,
        )

        result = parse_qwen_json(unicode_json)

        assert "chronomètre" in result["answer"]
        assert "时间跟踪" in result["answer"]
        assert "français-1" in result["sources_used"]
        assert "中文-2" in result["sources_used"]

    def test_parse_json_with_very_long_answer(self):
        """Test that very long answers are parsed correctly."""
        long_answer = "Test answer. " * 1000  # ~13KB answer
        long_json = json.dumps(
            {
                "answer": long_answer,
                "confidence": 70,
                "reasoning": "Based on extensive documentation.",
                "sources_used": ["1", "2", "3", "4", "5"],
            }
        )

        result = parse_qwen_json(long_json)

        assert len(result["answer"]) > 10000
        assert result["confidence"] == 70

    def test_parse_json_preserves_whitespace_in_answer(self):
        """Test that whitespace and formatting in answer is preserved."""
        formatted_answer = """
        ## Section 1

        - Item 1
        - Item 2

        Code example:
        ```
        const x = 1;
        ```
        """

        formatted_json = json.dumps(
            {
                "answer": formatted_answer,
                "confidence": 85,
                "reasoning": "Code example from context 1.",
                "sources_used": ["1"],
            }
        )

        result = parse_qwen_json(formatted_json)

        assert "## Section 1" in result["answer"]
        assert "- Item 1" in result["answer"]
        assert "const x = 1;" in result["answer"]
