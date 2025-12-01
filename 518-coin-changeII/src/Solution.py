class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # dp[x] = number of ways to make sum x using the coins considered so far
        dp: list[int] = [0] * (amount + 1)
        
        # Base case: one way to make 0 — choose no coins (the empty set {})
        dp[0] = 1

        # Process coins one by one to count combinations (order doesn't matter)
        for c in coins:
            # For this coin, try to build all amounts >= c
            for i in range(c, amount + 1):
                # Ways to make i can be increased by all ways to make (i - c),
                # then adding this coin c.
                dp[i] += dp[i - c]

        return dp[amount]

def main():
    sol: Solution = Solution()
    amount:int = 5
    coins:list[int] = [1,2,5]
    print(sol.change(amount, coins))

if __name__ == '__main__':
    main()

