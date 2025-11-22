class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(list1, list2) -> list[int]:
            n = len(list1)
            m = len(list2)
            rslt = [0]*(m+n)
            i = 0
            j = 0
            k = 0
            while(i < n and j < m):
                if list1[i] < list2[j]:
                    rslt[k] = list1[i]
                    i+=1
                else:
                    rslt[k] = list2[j]
                    j+=1
                k+=1

            while(i < n):
                rslt[k] = list1[i]
                i+=1
                k+=1
            while(j < m):
                rslt[k] = list2[j]
                j+=1
                k+=1
            return rslt
        #Base Case
        if len(nums) <= 1:
            return nums
        #Recursive Case
        mid:int = len(nums) // 2
        left:list[int] = self.sortArray(nums[:mid])
        right:list[int] = self.sortArray(nums[mid:])
        return merge(left, right)
        

                


def main():
    sol: Solution = Solution()
    nums:list[int] = [7,9,2,5,1,8,0,3,4,6]
    print(f"Before:\t{nums}")
    nums = sol.sortArray(nums)
    print(f"After:\t{nums}")

if __name__ == '__main__':
    main()
  
