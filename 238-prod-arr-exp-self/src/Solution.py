class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        raise NotImplementedError
    
    def productExceptSelf_naive(self, nums: list[int]) -> list[int]:
        prod:int = 1
        rslt = [0] * len(nums)
        for i in range(len(nums)):
            prod:int = prod * nums[i]
        for idx, num in enumerate(nums):
            rslt[idx] = prod//num
        return rslt

def main():
    sol: Solution = Solution()
    nums: list[int] = [1,2,3,4]
    print(nums)
    print(sol.productExceptSelf_naive([1,2,3,4]))
if __name__ == '__main__':
    main()
  
