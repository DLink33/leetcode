class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        LARGEST = amount + 1
        dp = [LARGEST] * (amount+1)
        dp[0] = 0
        for i in range (1, amount+1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i-c]+1)

        return dp[amount] if dp[amount] != LARGEST else -1


def main():
    sol: Solution = Solution()
    amount:int = 6
    coins:list[int] = [1,3,4]
    rslt:int = sol.coinChange(coins, amount)
    print(rslt)

if __name__ == '__main__':
    main()
  
