class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp:list[int] = [0] * (target+1)
        dp[0] = 1
        for x in range(1,target+1):
            for n in nums:
                if n <= x:
                    dp[x] += dp[x-n]
        return dp[target]
    
    def combinationSumIV(self, nums:list[int], target:int) -> int :
        memo:dict[int,int] = {}
        def helper(t:int) -> int:
            if t == 0:
                return 1
            rslt = 0
            for num in nums:
                if (t-num) in memo: # check to see if we have it memoized already 
                    rslt += memo[t-num]
                elif num <= t:
                    rslt += helper(t-num)
            memo[t] = rslt # memo our rslt
            return rslt

        return helper(target)

def main():
    sol: Solution = Solution()
    nums:list[int] = [1,2,3]
    target:int = 4
    print(sol.combinationSumIV(nums, target))
    print(sol.combinationSum4(nums, target))

if __name__ == '__main__':
    main()

