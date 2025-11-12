from linear.PriorityQueue import PriorityQueue
from typing import Callable
import logging as log
from copy import deepcopy

log.basicConfig(level=log.INFO)

class Solution:
    def findKthLargest_maxPQ(self, nums: list[int], k: int) -> int:
        pq:PriorityQueue[int] = PriorityQueue(nums, lambda x,y:x>y)
        log.info(f"Initial pq: {pq}")
        for _ in range(k-1):
            pq.pop()
            log.info(f"pq after pop: {pq}")
        return pq.peek()
    
    def findKthLargest_sort(self, nums: list[int], k: int) -> int:
        nums = deepcopy(nums)
        nums.sort(reverse=True)
        log.info(f"Sorted nums: {nums}")
        return nums[k-1]
    
    def findKthLargest_minPQ(self, nums: list[int], k: int) -> int:
        min_pq:PriorityQueue[int] = PriorityQueue([], lambda x,y:x<y)
        for num in nums:
            min_pq.push(num)
            log.info(f"min_pq after pushing {num}: {min_pq}")
            if len(min_pq) > k:
                removed = min_pq.pop()
                log.info(f"min_pq after popping {removed}: {min_pq}")
        return min_pq.peek()
        
SMOKE_TEST_PARAMS: list[tuple[list[int], int, int]] = [
    ([3,2,1,5,6,4], 2, 5),
    ([3,2,3,1,2,4,5,5,6], 4, 4),
]

def run_smoke_tests(test_func: Callable[[list[int], int], int], testParams: list[tuple[list[int], int, int]] = SMOKE_TEST_PARAMS) -> None:

    for params in testParams:
        rslt:int = test_func(params[0], params[1])
        log.info(f"nums: {params[0]}")
        log.info(f"k: {params[1]}")
        log.info(f"rslt: {rslt}; expected: {params[2]}")
        assert rslt == params[2]

def main():
    sol = Solution()
    run_smoke_tests(sol.findKthLargest_maxPQ)
    run_smoke_tests(sol.findKthLargest_minPQ)
    run_smoke_tests(sol.findKthLargest_sort)
    print("All smoke tests passed!")
    

if __name__ == '__main__':
    main()