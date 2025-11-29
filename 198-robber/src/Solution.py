class Solution:
    def rob(self, nums: list[int]) -> int:
        n:int = len(nums)
        if n == 1:
            return nums[0]
        prev1= nums[0]
        prev2= max(nums[1],nums[0])

        for i in range(2,n,1):
            curr = max(prev2, nums[i] + prev1)
            prev1, prev2 = prev2, curr  
        return prev2
        

def main():
    sol: Solution = Solution()
    nums: list[int] = [2,7,9,3,1]
    print(sol.rob(nums=nums))
    nums = [2,1,1,2]
    print(sol.rob(nums=nums))
    nums = [10, 2, 9, 3, 1, 5, 6]
    print(sol.rob(nums=nums))

if __name__ == '__main__':
    main()
  
