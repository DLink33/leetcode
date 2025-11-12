import pytest
from src.Solution import Solution

TEST_CASES = [
    ([[1,1,0],[1,1,0],[0,0,1]], 2),
    ([[1,0,0],[0,1,0],[0,0,1]], 3),
    ([[1,1,1],[1,1,1],[1,1,1]], 1),
    ([[1]], 1),
    ([[1,0],[0,1]], 2),
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
