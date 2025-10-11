from typing import List, Tuple

import pytest

from lc001_two_sum import Solution

CASES: List[Tuple[List[int], int, List[int]]] = [
    ([2, 7, 11, 15], 9, [0, 1]),  # sample
    ([3, 2, 4], 6, [1, 2]),  # small check
    ([3, 3], 6, [0, 1]),  # two same elements
    ([0, 4, 3, 0], 0, [0, 3]),  # two zeros
    ([-1, -2, -3, -4, -5], -8, [2, 4]),  # negative numbers
    ([1, 2, 3, 4, 5], 10, []),  # no solution
    ([1, 2], 3, [0, 1]),  # minimum input size
    ([1, 2, 3], 5, [1, 2]),  # odd length list
    ([1, 2, 3, 4], 7, [2, 3]),  # even length list
    ([0, 0, 3, 4], 0, [0, 1]),  # multiple zeros
    ([1] * 10000 + [2], 3, [9999, 10000]),  # large input size
]


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize("nums, target, expected", CASES)
def test_two_sum(sol: Solution, nums: List[int], target: int, expected: List[int]):
    result = sol.twoSum(nums, target)
    print(f"\nInput array: {nums}")
    print(f"Target sum: {target}")
    print(f"Expected result: {expected}")
    print(f"Actual result: {result}")
    assert result == expected
