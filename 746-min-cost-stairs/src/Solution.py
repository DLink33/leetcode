class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if not cost:
            return 0
        n: int = len(cost)
        dp: list[int] = [0]*(n)
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])
        dp[0] = cost[0]
        dp[1] = cost[1]
        total: int = 0
        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])
    
    def minCostClimbingStairsIter(self, cost: list[int]) -> int:
        if not cost:
            return 0
        n: int = len(cost)
        if n == 1:
            return cost[0]
        prev1:int = cost[0]
        prev2:int = cost[1]
        curr: int = 0
        for i in range(2,n):
            better = min(prev1, prev2)
            curr = cost[i] + better
            prev1 = prev2
            prev2 = curr
        return min(prev1, prev2)


def main():
    sol: Solution = Solution()
    cost:list[int] = [1, 100, 1, 1 ,1, 100, 1, 1, 100, 1]
    ans:int = 6
    print(sol.minCostClimbingStairs(cost))
    print(sol.minCostClimbingStairsIter(cost))
    assert sol.minCostClimbingStairs(cost) == ans

if __name__ == '__main__':
    main()
  
