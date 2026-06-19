"""
Tests for the @retry decorator.
Do not modify this file.
"""
import pytest
from retry import retry


def test_succeeds_on_third_attempt():
    """Function that fails twice and succeeds on the third attempt."""
    call_count = 0

    @retry(times=3, exceptions=(ValueError,))
    def flaky():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise ValueError("temporary failure")
        return "ok"

    result = flaky()
    assert result == "ok"
    assert call_count == 3


def test_raises_after_max_retries():
    """If all attempts are exhausted, the last exception must propagate."""
    @retry(times=3, exceptions=(ValueError,))
    def always_fails():
        raise ValueError("permanent error")

    with pytest.raises(ValueError, match="permanent error"):
        always_fails()


def test_does_not_retry_unlisted_exception():
    """If the exception type is not listed, it must propagate immediately."""
    call_count = 0

    @retry(times=3, exceptions=(ValueError,))
    def wrong_exception():
        nonlocal call_count
        call_count += 1
        raise TypeError("wrong type")

    with pytest.raises(TypeError):
        wrong_exception()

    assert call_count == 1


def test_times_one_does_not_retry():
    """With times=1, the function raises on the first failure without retrying."""
    call_count = 0

    @retry(times=1, exceptions=(Exception,))
    def fails_once():
        nonlocal call_count
        call_count += 1
        raise RuntimeError("failure")

    with pytest.raises(RuntimeError):
        fails_once()

    assert call_count == 1


def test_preserves_function_metadata():
    """The decorator must preserve __name__ and __doc__ of the original function."""
    @retry(times=2, exceptions=(Exception,))
    def my_function():
        """Docstring of my_function."""
        pass

    assert my_function.__name__ == "my_function"
    assert "Docstring" in my_function.__doc__


def test_passes_args_and_kwargs():
    """The decorator must correctly forward *args and **kwargs."""
    @retry(times=2, exceptions=(Exception,))
    def add(a, b, *, factor=1):
        return (a + b) * factor

    assert add(2, 3, factor=4) == 20


def test_retry_count_is_exact():
    """The number of calls must not exceed `times`."""
    call_count = 0

    @retry(times=4, exceptions=(RuntimeError,))
    def always_fails():
        nonlocal call_count
        call_count += 1
        raise RuntimeError("x")

    with pytest.raises(RuntimeError):
        always_fails()

    assert call_count == 4
