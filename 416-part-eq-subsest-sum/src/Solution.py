class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total:int = sum(nums)

        if total % 2 != 0:
            return False
        
        target:int = total // 2

        dp:list[bool] = [False] * (target+1)
        dp[0] = True #base case a sum of 0 is possible by selecting the empty set

        for n in nums:
            for s in range(target, n-1, -1):
                dp[s] |= dp[s-n]

        return dp[target]

def main():
    sol: Solution = Solution()
    nums = [1,5,11,5]
    print(sol.canPartition(nums))

if __name__ == '__main__':
    main()

