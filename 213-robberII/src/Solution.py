class Solution:
    def rob_linear(self, nums: list[int]) -> int:
        n:int = len(nums)
        if n == 1:
            return nums[0]
        
        prev2 = nums[0]                 # take the current val and the i-2
        prev1 = max(nums[0], nums[1])   # take the val at i-1

        for i in range(2,n):
            curr = max(prev1, prev2+nums[i])
            prev1, prev2, = curr, prev1
        return prev1
    
    def rob(self, nums:list[int]):
        if len(nums) == 1:
            return nums[0]
        first:list[int] = nums[:-1]
        last:list[int]  = nums[1:]
        return max(self.rob_linear(first), self.rob_linear(last))

def main():
    sol: Solution = Solution()
    houses:list[int] = [1,2,3,1]
    print(sol.rob(houses))

if __name__ == '__main__':
    main()
  
