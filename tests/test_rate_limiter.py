"""Tests for rate limiting functionality."""
import math
import os
import sys

import pytest

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from clockify_rag.caching import RateLimiter


class ManualClock:
    """Deterministic monotonic clock for rate limiter tests."""

    def __init__(self):
        self._now = 0.0

    def __call__(self) -> float:  # pragma: no cover - simple getter
        return self._now

    def advance(self, seconds: float) -> None:
        self._now += seconds


class TestRateLimiter:
    """Test rate limiter logic."""

    def test_rate_limiter_allows_within_limit(self):
        clock = ManualClock()
        limiter = RateLimiter(max_requests=3, window_seconds=10, time_func=clock)

        assert limiter.allow_request() is True
        assert limiter.allow_request() is True
        assert limiter.allow_request() is True

    def test_rate_limiter_blocks_after_limit(self):
        clock = ManualClock()
        limiter = RateLimiter(max_requests=3, window_seconds=10, time_func=clock)

        assert limiter.allow_request() is True
        assert limiter.allow_request() is True
        assert limiter.allow_request() is True
        assert limiter.allow_request() is False

    def test_rate_limiter_resets_after_window(self):
        clock = ManualClock()
        limiter = RateLimiter(max_requests=2, window_seconds=1, time_func=clock)

        assert limiter.allow_request() is True
        assert limiter.allow_request() is True
        assert limiter.allow_request() is False

        clock.advance(1.1)

        assert limiter.allow_request() is True

    def test_rate_limiter_wait_time_zero_when_allowed(self):
        clock = ManualClock()
        limiter = RateLimiter(max_requests=3, window_seconds=10, time_func=clock)

        assert limiter.wait_time() == 0.0
        limiter.allow_request()
        assert limiter.wait_time() == 0.0

    def test_rate_limiter_wait_time_nonzero_when_blocked(self):
        clock = ManualClock()
        limiter = RateLimiter(max_requests=2, window_seconds=10, time_func=clock)

        limiter.allow_request()
        limiter.allow_request()

        assert limiter.allow_request() is False

        wait_time = limiter.wait_time()
        assert wait_time > 0
        assert math.isfinite(wait_time)
        assert wait_time <= 10

        clock.advance(wait_time)
        assert limiter.allow_request() is True

    def test_rate_limiter_sliding_window(self):
        clock = ManualClock()
        limiter = RateLimiter(max_requests=2, window_seconds=2, time_func=clock)

        assert limiter.allow_request() is True
        clock.advance(1.0)
        assert limiter.allow_request() is True
        assert limiter.allow_request() is False
        clock.advance(1.0)
        assert limiter.allow_request() is True

    def test_rate_limiter_custom_limits(self):
        clock = ManualClock()
        limiter = RateLimiter(max_requests=1, window_seconds=5, time_func=clock)
        assert limiter.allow_request() is True
        assert limiter.allow_request() is False

        clock = ManualClock()
        limiter = RateLimiter(max_requests=100, window_seconds=1, time_func=clock)
        for _ in range(100):
            assert limiter.allow_request() is True
        assert limiter.allow_request() is False

    def test_rate_limiter_concurrent_safety(self):
        clock = ManualClock()
        limiter = RateLimiter(max_requests=5, window_seconds=10, time_func=clock)

        allowed_count = 0
        for _ in range(10):
            if limiter.allow_request():
                allowed_count += 1

        assert allowed_count == 5


if __name__ == "__main__":  # pragma: no cover - manual invocation helper
    pytest.main([__file__, "-v"])
