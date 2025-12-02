from typing import Any
import time

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

# Master list of test cases
TEST_CASES: list[TestCase] = [
    (([1, 2, 5], 11), 3),
    (([2], 3), -1),
    (([1], 0), 0),
    (([1], 1), 1),
    (([1], 2), 2),
    (([1, 3, 4], 6), 2),
    (([2, 5, 10, 1], 27), 4),
    (([186, 419, 83, 408], 6249), 20),
    (([1, 5, 10, 25], 63), 6),
    (([3, 7, 405, 436], 883), 8),
    (([2, 5, 10, 1], 100), 10),
    (([1, 2147483647], 2), 2),
    (([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 999), -1),
]

# Only the smaller ones for the exponential recursive solution
SMALL_TEST_CASES: list[TestCase] = TEST_CASES[:7]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_coin_change_bottom_up(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.coinChange(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.coinChange(*case_input) == expected
    else:
        assert sol.coinChange(case_input) == expected  # pyright: ignore[reportCallIssue]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_coin_change_memo(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.coinChange_memo(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.coinChange_memo(*case_input) == expected
    else:
        assert sol.coinChange_memo(case_input) == expected  # pyright: ignore[reportCallIssue]


@pytest.mark.parametrize(("case_input", "expected"), SMALL_TEST_CASES)
def test_coin_change_recursive(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.coinChange_recursive(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.coinChange_recursive(*case_input) == expected
    else:
        assert sol.coinChange_recursive(case_input) == expected  # pyright: ignore[reportCallIssue]


def test_timing_coin_change_methods(coin_repeats: int) -> None:
    """
    Simple timing comparison between bottom-up DP and memoized recursion.

    Run with:
        pytest -s tests/test_322_coin_change.py::test_timing_coin_change_methods --coin-repeats 50
    to see printed timings.
    """
    sol = Solution()

    # Pick the heavier cases to make the timing difference more visible
    benchmark_cases: list[TestCase] = [
        (([2, 5, 10, 1], 27), 4),
        (([186, 419, 83, 408], 6249), 20),
        (([1, 5, 10, 25], 63), 6),
        (([3, 7, 405, 436], 883), 8),
        (([2, 5, 10, 1], 100), 10),
        (([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 999), -1),
    ]

    methods = [
        ("bottom_up", sol.coinChange),
        ("memo", sol.coinChange_memo),
    ]

    repeats = coin_repeats  # increase if you want smoother averages

    for name, func in methods:
        start = time.perf_counter()
        for _ in range(repeats):
            for (coins, amount), expected in benchmark_cases:
                result = func(coins, amount)
                # sanity-check correctness while benchmarking
                assert result == expected
        elapsed = time.perf_counter() - start
        calls = repeats * len(benchmark_cases)
        print(
            f"\n{name:10s}: total={elapsed:.4f}s  avg_per_call={elapsed / calls:.6f}s "
            f"over {calls} calls (6 test cases)"
        )
