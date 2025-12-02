from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    (([1, 2, 3], 4), 7),
    (([9], 3), 0),
    (([2, 1, 3], 35), 1132436852),
    (([10], 10), 1),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 512),
    (([4, 2, 1], 32), 39882198),
    (([3, 33, 333], 10000), 0),
    (([1], 0), 1),
    (([1, 2], 10), 89),
    (([5, 3, 2], 8), 6),
]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.combinationSum4(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.combinationSum4(*case_input) == expected
    else:
        assert sol.combinationSum4(case_input) == expected # pyright: ignore[reportCallIssue]
