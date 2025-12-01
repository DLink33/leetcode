from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    ([2,3,2], 3),
    ([1,2,3,1], 4),
    ([0], 0),
    ([1,2,3], 3),
    ([1,3,1,3,100], 103),
    ([200,3,140,20,10], 340),
    ([1,1,1,1,1,1,1,1,1], 4),
    ([100,1,1,100], 101),
    ([1,2], 2),
    ([2,1], 2),
    ([1], 1),
    ([5,1,1,5], 6),
]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.rob(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.rob(*case_input) == expected
    else:
        assert sol.rob(case_input) == expected # pyright: ignore[reportArgumentType]
