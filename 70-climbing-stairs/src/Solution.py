class Solution:
    def __init__(self):
        self._ways:dict[int,int] = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if n in self._ways:
            return self._ways[n]
        rslt: int = self.climbStairs(n-1) + self.climbStairs(n-2)
        if n not in self._ways:
            self._ways[n] = rslt
        return rslt
    
    def climbStairsIterative(self, n: int):
        if n == 1 or n == 2:
            return n
        j:int = 1
        k:int = 2
        i:int = 3   # Start iat 3 since the first 2 iterations 
                    # are encapsulated in our early return base cases

        while(i <= n):
            i+=1
            nxt:int = j+k  # get the next valute before we start setting j and k
            j = k # j becomes the current k 
            k = nxt # k becomes the previous k plus the previous j
        return k # finally return k when we are done iterating

def main():
    sol: Solution = Solution()
    n:int = 5
    ans:int = sol.climbStairs(n)
    print(ans)
    ans:int = sol.climbStairsIterative(n)
    print(ans)

if __name__ == '__main__':
    main()
