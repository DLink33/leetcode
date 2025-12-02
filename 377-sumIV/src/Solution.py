class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp:list[int] = [0] * (target+1)
        dp[0] = 1
        for x in range(1,target+1):
            for n in nums:
                if n <= x:
                    dp[x] += dp[x-n]
        return dp[target]

def main():
    sol: Solution = Solution()
    nums:list[int] = [9]
    target:int = 3
    print(sol.combinationSum4(nums, target))

if __name__ == '__main__':
    main()

