import pytest
from Solution import Solution

TEST_CASES: list[tuple[list[list[int]], int]] = [
    ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1),
    ([[1]], 1),
    ([[1, 0], [0, 1]], 2),
]


@pytest.mark.parametrize("is_connected, expected", TEST_CASES)
def test_solution(is_connected: list[list[int]], expected: int) -> None:
    sol = Solution()
    assert sol.findCircleNum(is_connected) == expected
