from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    # Add your test cases here. Common patterns:
    # (input_value, expected_value)
    # ((arg1, arg2, ...), expected_value)
    # ({"args": (a1, ...), "kwargs": {"k": v}}, expected_value)
]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.coinChange(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.coinChange(*case_input) == expected
    else:
        assert sol.coinChange(case_input) == expected
