#! .venv/bin/python

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        currArea = 0
        length = len(height)
        i = 0
        j = 0
        while i < length - 1:
            j = i + 1
            while j <= length - 1:
                currArea = (j - i) * min(height[i], height[j])
                maxArea = max(maxArea, currArea)
                j += 1
            i += 1
        return maxArea


def main():
    h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    smoke = Solution()
    rslt = smoke.maxArea(h)
    print(rslt)


if __name__ == "__main__":
    main()
