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

    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m: int = len(obstacleGrid)      # height
        n: int = len(obstacleGrid[0])   # width
        dp: list[list[int]] = [[0]*n for _ in range(m)]
        
        # return 0 if we are blocked from the start
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp[0][0] = 1

        # init the first column with appropriate 1s or 0s
        for i in range(1,m):
            if obstacleGrid[i][0] == 0 and dp[i-1][0] == 1:
                dp[i][0] = 1
            else:
                break
                
        # init the first row with appropriate 1s or 0s
        for j in range(1,n):
            if obstacleGrid[0][j] == 0 and dp[0][j-1] == 1:
                dp[0][j] = 1
            else:
                break

        # iterate through dp and if we see an obstacle we know the number
        # of ways to get to that coord in the gird is 0. Otherwise, 
        # we take the sum of the num of paths above and the num of paths 
        # to the left
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
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

    obstacles:list[list[int]] = [
                                    [0,0,1,0,1,0],
                                    [0,0,0,0,1,0],
                                    [0,0,1,0,0,0],
                                    [0,0,0,1,0,0]
                                ]
    
    print(sol.uniquePathsWithObstacles(obstacleGrid=obstacles))

if __name__ == '__main__':
    main()

