"""Tests for query expansion functionality."""
import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from clockify_support_cli_final import expand_query


class TestQueryExpansion:
    """Test query expansion with synonyms and acronyms."""

    def test_expand_query_with_track(self):
        """Test that 'track' expands with synonyms."""
        query = "How to track time?"
        expanded = expand_query(query)

        # Should contain original query
        assert "How to track time?" in expanded
        # Should contain synonyms for 'track'
        assert any(syn in expanded for syn in ["log", "record", "enter", "add"])
        # Should contain synonyms for 'time'
        assert any(syn in expanded for syn in ["hours", "duration"])

    def test_expand_query_with_acronym(self):
        """Test that acronyms like 'SSO' are expanded."""
        query = "How to configure SSO?"
        expanded = expand_query(query)

        # Should contain original
        assert "How to configure SSO?" in expanded
        # Should contain expansion
        assert "single sign-on" in expanded or "single sign on" in expanded

    def test_expand_query_no_match(self):
        """Test that queries without matching terms are unchanged."""
        query = "What is the meaning of life?"
        expanded = expand_query(query)

        # Should return original query unchanged
        assert expanded == query

    def test_expand_query_empty(self):
        """Test that empty query returns empty."""
        assert expand_query("") == ""

    def test_expand_query_multiple_terms(self):
        """Test query with multiple matching terms."""
        query = "How to track billable time?"
        expanded = expand_query(query)

        # Should expand both 'track' and 'billable' and 'time'
        assert "How to track billable time?" in expanded
        assert any(syn in expanded for syn in ["log", "record"])
        assert any(syn in expanded for syn in ["chargeable", "invoiceable"])
        assert any(syn in expanded for syn in ["hours", "duration"])

    def test_expand_query_whole_word_only(self):
        """Test that partial word matches are not expanded."""
        # 'track' should not match 'attraction'
        query = "tourist attraction"
        expanded = expand_query(query)

        # Should not expand because 'track' is not a whole word
        assert expanded == query

    def test_expand_query_case_insensitive(self):
        """Test that expansion works regardless of case."""
        query = "How to TRACK TIME?"
        expanded = expand_query(query)

        # Should still expand despite uppercase
        assert any(syn in expanded for syn in ["log", "record", "enter"])

    def test_expand_query_with_reports(self):
        """Test expansion of 'report' term."""
        query = "Generate report"
        expanded = expand_query(query)

        assert "Generate report" in expanded
        assert any(syn in expanded for syn in ["summary", "analytics", "export"])

    def test_expand_query_mobile_terms(self):
        """Test expansion of mobile-related terms."""
        query = "Can I use mobile app offline?"
        expanded = expand_query(query)

        # Should expand 'mobile' and 'offline'
        assert any(syn in expanded for syn in ["phone", "smartphone", "app"])
        assert any(syn in expanded for syn in ["no internet", "no connection"])

    def test_expand_query_preserves_original(self):
        """Test that original query is always preserved."""
        query = "How to track time?"
        expanded = expand_query(query)

        # Original should be the first part
        assert expanded.startswith(query)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
