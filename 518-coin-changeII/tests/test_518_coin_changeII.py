from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    ((5, [1, 2, 5]), 4),
    ((3, [2]), 0),
    ((10, [10]), 1),
    ((0, [1, 2, 3]), 1),
    ((7, [1, 2, 3]), 8),
    ((4, [1, 2, 5]), 3),
    ((100, [1, 5, 10, 25]), 242),
    ((50, [2, 5, 10, 20, 50]), 35),
    ((1, []), 0),
    ((0, []), 1),
    ((500, [1, 2, 5, 10, 20, 50, 100, 200, 500]), 6295435),
]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.change(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.change(*case_input) == expected
    else:
        assert sol.change(case_input) == expected  # pyright: ignore[reportCallIssue]
