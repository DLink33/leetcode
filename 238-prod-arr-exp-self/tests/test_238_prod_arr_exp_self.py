from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    # Add your test cases here. Common patterns:
    ([1,2,3,4], [24, 12, 8, 6]),
    ([0,0], [0, 0]),
    ([1,0], [0, 1]),
    ([0,1,2,3], [6, 0, 0, 0]),
    ([5], [1]),
    ([1, -1, 1, -1], [1, -1, 1, -1]),
    ([2,3,4,5], [60, 40, 30, 24]),
    ([10, 0, 5], [0, 50, 0]),
    ([1,2], [2,1]),
    ([1000, 2000, 3000], [6000000, 3000000, 2000000]),
]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.productExceptSelf(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.productExceptSelf(*case_input) == expected
    else:
        assert sol.productExceptSelf(case_input) == expected
