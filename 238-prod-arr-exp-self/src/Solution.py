class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        left,right,rslt = [1]*n,[1]*n,[1]*n

        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]

        for i in range(n-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]

        for i in range(n):
            rslt[i] = left[i]*right[i]
        return rslt

    
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
    print(sol.productExceptSelf(nums))
if __name__ == '__main__':
    main()
  
