import pytest
from src.Solution import Solution

TEST_CASES = [
    # Add your test cases here. Common patterns:
    # (input_value, expected_value)
    # ((arg1, arg2, ...), expected_value)
    # ({"args": (a1, ...), "kwargs": {"k": v}}, expected_value)
]

@pytest.mark.parametrize("input, expected", TEST_CASES)
def test_solution(input, expected):
    sol: Solution = Solution()
    if isinstance(input, dict) and ("args" in input or "kwargs" in input):
        args = input.get("args", ())
        kwargs = input.get("kwargs", {})
        assert sol.findCircleNum(*args, **kwargs) == expected
    elif isinstance(input, tuple):
        assert sol.findCircleNum(*input) == expected
    else:
        assert sol.findCircleNum(input) == expected
