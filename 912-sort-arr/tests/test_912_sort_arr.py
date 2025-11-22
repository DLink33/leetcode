from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    ([5, 2, 3, 1], [1, 2, 3, 5]),
    ([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]),
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([3, 2, 1], [1, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([4, 3, 2, 1], [1, 2, 3, 4]),
    ([10, -1, 2, 0, 5], [-1, 0, 2, 5, 10]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([1, 3, 2, 3, 1], [1, 1, 2, 3, 3]),
    ([100, 50, 75, 25, 0], [0, 25, 50, 75, 100]),
    ([9, 7, 5, 3, 1, 2, 4, 6, 8, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 2, 2, 1, 1, 2], [1, 1, 1, 2, 2, 2]),
    ([3, 5, 2, 4, 1], [1, 2, 3, 4, 5]),
    ([8, 6, 7, 5, 3, 0, 9], [0, 3, 5, 6, 7, 8, 9]),
    ([2, 3, 2, 1, 4, 3, 5], [1, 2, 2, 3, 3, 4, 5]),
    ([1, -1, 0], [-1, 0, 1]),
    ([4, 2, 5, 3, 1, 0], [0, 1, 2, 3, 4, 5]),
    ([6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6]),
]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.sortArray(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.sortArray(*case_input) == expected
    else:
        assert sol.sortArray(case_input) == expected
