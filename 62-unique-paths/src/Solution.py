from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp:list[list[int]] = [[0]*(n) for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(1, n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]
    
    def uniquePaths_choose(self, m: int, n: int) -> int:
        D:int = m-1
        R:int = n-1
        T:int = D + R
        return comb(T, D)

def main():
    sol: Solution = Solution()
    m = 3
    n = 5
    print(sol.uniquePaths_choose(m,n))
    print(sol.uniquePaths(m, n))

if __name__ == '__main__':
    main()

