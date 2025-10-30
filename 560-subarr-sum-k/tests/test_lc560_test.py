import pytest

from solution import Solution

CASES: list[tuple[list[int], int, int]] = [
    ([1, 1, 1, 1], 2, 3),
    ([6, -2, -1, 3, 8, -4], 4, 3),
]


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize("nums, k, expected", CASES)
def test_subarraySum(sol: Solution, nums: list[int], k: int, expected: int):
    assert sol.subarraySum(nums, k) == expected
