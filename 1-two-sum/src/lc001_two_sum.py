#! .venv/bin/python
from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap: Dict[int, int] = {}

        for i, n in enumerate(nums):
            c = target - n
            if c < 0:
                continue
            if c in numsMap:
                return [numsMap[c], i]
            numsMap[n] = i
        return []


def main():
    pass


if __name__ == "__main__":
    main()
