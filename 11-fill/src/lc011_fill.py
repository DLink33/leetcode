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
            while j < length:
                currArea = (j - i) * min(height[i], height[j])
                maxArea = max(maxArea, currArea)
                j += 1
            i += 1
        return maxArea

    def maxArea2(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            currArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currArea)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return maxArea


def main():
    h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    smoke = Solution()
    rslt = smoke.maxArea(h)
    rslt2 = smoke.maxArea2(h)
    print("expected value: 49\n")
    print(f"maxArea1: {rslt}")
    print(f"maxArea2: {rslt2}")


if __name__ == "__main__":
    main()
