from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    ([2, 7, 9, 3, 1], 12),
    ([2, 1, 1, 2], 4),
    ([1, 3, 1, 3, 100], 103),
    ([1], 1),
    ([0], 0),
    ([1, 2], 2),
    ([2, 3, 2], 4),
    ([1, 2, 3, 1], 4),
    ([4, 1, 2, 7, 5, 3, 1], 14),
    ([10, 2, 9, 3, 1, 5, 6], 26),
    ([100, 1, 1, 100], 200),
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
        assert sol.rob(case_input) == expected
