from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    ([2, 7, 4, 1, 8, 1], 1),
    ([31, 26, 33, 21, 40], 5),
    ([1, 2], 1),
    ([1, 3, 4, 2, 2], 0),
    ([5, 3, 1, 4, 2, 6], 1),
    ([10, 10, 10, 10], 0),
    ([1], 1),
    ([2, 2, 2, 2, 2], 2),
    ([7, 3, 2, 5, 8], 1),
    ([9, 8, 7, 6, 5], 1),
]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.lastStoneWeightII(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.lastStoneWeightII(*case_input) == expected
    else:
        assert sol.lastStoneWeightII(case_input) == expected # pyright: ignore[reportArgumentType]
