class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        n:int = len(stones)
        total:int = sum(stones)
        target = total//2
        dp:list[bool] = [False] * (target+1)
        dp[0] = True

        for weight in stones:
            for i in range(target, weight - 1, -1):
                dp[i] = dp[i] or dp[i-weight] # if it is already possible to create a value i, then we don't need to check if i - weight of current stone is also possible
        
        for i in range(target, -1, -1):
            if dp[i]:
                return total - (2*i) # return the total
        return 0
        

def main():
    sol: Solution = Solution()
    stones:list[int] = [2,7,4,1,8,1]
    print(sol.lastStoneWeightII(stones))

    stones = [31,26,33,21,40]
    print(sol.lastStoneWeightII(stones))

if __name__ == '__main__':
    main()

