class Solution:
    def jump(self, nums: list[int]) -> int:
        raise NotImplementedError
    
    def jump_greedy(self, nums: list[int]) -> int:
        n = len(nums)
        jumps = 0 # tracks the number of jumps we have taken
        end = 0   # tracks the end of the current range of values we could jump to
        farthest = 0 # tracks the largest jump value between the current index  and end

        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == end: # we have finished looking at all of the possible indecies to jump to
                jumps += 1 # now we must jump since we have found the farthest we can get
                end = farthest # we now have a new end point
                if end >= n-1: # if we reach the end already we can break and return our jumps
                    break
        return jumps


def main():
    sol: Solution = Solution()
    inpt:list[int] = [2,3,1,12,4]   
    #inpt:list[int] = [1,2,3]
    rslt = sol.jump_greedy(inpt)
    print(rslt)

if __name__ == '__main__':
    main()

