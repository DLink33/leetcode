from typing import Any

import pytest

from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    # Example test cases
    ([1, 5, 11, 5], True),
    ([1, 2, 3, 5], False),
    # Additional test cases
    ([2, 2, 3, 5], False),
    ([3, 3, 3, 4, 5], True),
    ([1, 2, 5], False),
    ([1, 1, 1, 1], True),
    ([100, 100, 100, 100, 100, 100], True),
    ([1], False),
    ([0, 0, 0, 0], True),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False)
]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.canPartition(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.canPartition(*case_input) == expected
    else:
        assert sol.canPartition(case_input) == expected
