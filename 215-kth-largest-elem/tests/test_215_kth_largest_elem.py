# tests/test_lc215_kth_largest.py
import pytest
from Solution import Solution  # adjust import to your module

TEST_CASES = [
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ([1], 1, 1),
    ([2, 1], 1, 2),
    ([2, 1], 2, 1),
    ([5, 3, 1, 6, 4, 2], 3, 4),
    ([7, 10, 4, 3, 20, 15], 3, 10),
    ([1, 2, 3, 4, 5, 6], 6, 1),
    ([6, 5, 4, 3, 2, 1], 1, 6),
]

@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize("nums,k,expected", TEST_CASES)
def test_find_kth_largest_maxpq(sol, timeit, nums, k, expected):
    # copy to avoid in-place mutation across tests
    got = timeit("maxPQ", sol.findKthLargest_maxPQ, list(nums), k)
    assert got == expected

@pytest.mark.parametrize("nums,k,expected", TEST_CASES)
def test_find_kth_largest_minpq(sol, timeit, nums, k, expected):
    got = timeit("minPQ", sol.findKthLargest_minPQ, list(nums), k)
    assert got == expected

@pytest.mark.parametrize("nums,k,expected", TEST_CASES)
def test_find_kth_largest_sort(sol, timeit, nums, k, expected):
    got = timeit("sort", sol.findKthLargest_sort, list(nums), k)
    assert got == expected
