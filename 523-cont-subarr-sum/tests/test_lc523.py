# tests/test_523.py
import pytest

from solution import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        # Provided / canonical cases
        ([23, 2, 4, 6, 7], 6, True),
        ([23, 2, 6, 4, 7], 6, True),
        ([23, 2, 6, 4, 7], 13, False),
        # k == 0: need two consecutive zeros
        ([0, 0], 0, True),
        ([5, 0, 0], 0, True),
        ([0, 1, 0], 0, False),  # zeros not adjacent → no length-2 zero-sum
        # length guard
        ([5], 5, False),
        # k == 1: any length>=2 subarray works
        ([1, 2], 1, True),
        # negative k normalization
        ([5, 1, 2], -3, True),  # [1,2] = 3
        ([1, 2, 3], -7, False),
        # prefix-based success (sum of first two is multiple of k)
        ([6, 0], 6, True),
        # simple false
        ([1, 0], 2, False),
    ],
)
def test_check_subarray_sum(nums: list[int], k: int, expected: int):
    assert Solution().checkSubarraySum(nums, k) is expected
