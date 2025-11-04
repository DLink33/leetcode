"""
739. Daily Tempurature

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


class Solution:
    # O(n) using a monotonic stack
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        rslt: list[int] = [0] * len(temperatures)
        staq: list[int] = []

        for i, temp in enumerate(temperatures):
            while staq and temp > temperatures[staq[-1]]:
                idx: int = staq.pop()
                rslt[idx] = i - idx
            staq.append(i)
        return rslt

    # brute force O(n^2)
    def dailyTemperatures_brutish(self, temperatures: list[int]) -> list[int]:
        rslt = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    rslt[i] = j - i
                    break
        return rslt


def main():
    temperatures: list[int] = [73, 74, 75, 71, 69, 72, 76, 73]
    temperatures: list[int] = [1, 100, 2, 4, 3, 5, 101]
    sol: Solution = Solution()
    rslt: list[int] = sol.dailyTemperatures_brutish(temperatures)
    print(rslt)
    rslt = sol.dailyTemperatures(temperatures)
    print(rslt)


if __name__ == "__main__":
    main()
