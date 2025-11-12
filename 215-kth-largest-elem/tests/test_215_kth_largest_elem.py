# tests/test_lc006_zigzag.py
import pytest
from Solution import Solution
from time import time


@pytest.fixture
def sol():
    return Solution()

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

AVG_RUN_TIMES: dict[str, float] = {
    "maxPQ": 0,
    "minPQ": 0,
    "sort": 0,
}

@pytest.mark.parametrize(
    "nums,k,expected",
    TEST_CASES
)

def test_find_kth_largest(sol: Solution, nums: list[int], k: int, expected: int):
    start_time = time()
    assert sol.findKthLargest_maxPQ(nums=nums, k=k) == expected
    end_time = time()
    AVG_RUN_TIMES["maxPQ"] += (end_time - start_time)

@pytest.mark.parametrize(
    "nums,k,expected",
    TEST_CASES
)
def test_find_kth_largest_minPQ(sol: Solution, nums: list[int], k: int, expected: int):
    start_time = time()
    assert sol.findKthLargest_minPQ(nums=nums, k=k) == expected
    end_time = time()
    AVG_RUN_TIMES["minPQ"] += (end_time - start_time)

@pytest.mark.parametrize(
    "nums,k,expected",
    TEST_CASES
)
def test_find_kth_largest_sort(sol: Solution, nums: list[int], k: int, expected: int):
    start_time = time()
    assert sol.findKthLargest_sort(nums=nums, k=k) == expected
    end_time = time()
    AVG_RUN_TIMES["sort"] += (end_time - start_time)

def test_avg_run_times():
    num_tests = len(TEST_CASES)
    print()
    for method, total_time in AVG_RUN_TIMES.items():
        avg_time = total_time / num_tests
        print(f"\nAverage run time for {method}:\t{avg_time:.10f} seconds")
    print()