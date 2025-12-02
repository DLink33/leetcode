class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        LARGEST = amount + 1
        dp = [LARGEST] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] != LARGEST else -1

    def coinChange_recursive(self, coins: list[int], amount: int) -> int:
        INF: int = amount + 1

        def change(target: int) -> int:
            if target == 0:
                return 0
            if target < 0:
                return INF
            best: int = INF
            for coin in coins:
                new_target: int = target - coin
                best = min(best, 1 + change(new_target))
            return best

        ans = change(amount)
        return ans if ans != INF else -1

    def coinChange_memo(self, coins: list[int], amount: int) -> int:
        INF: int = amount + 1
        memo: dict[int, int] = {}

        def change(target: int) -> int:
            if target in memo:
                return memo[target]
            if target == 0:
                return 0
            if target < 0:
                return INF

            best: int = INF
            for coin in coins:
                new_target: int = target - coin
                best = min(best, 1 + change(new_target))

            memo[target] = best
            return best

        ans = change(amount)
        return ans if ans != INF else -1



def main():
    sol: Solution = Solution()
    amount:int = 2
    coins:list[int] = [3]
    rslt:int = sol.coinChange(coins, amount)
    print(rslt)
    rslt = sol.coinChange_recursive(coins, amount)
    print(rslt)

if __name__ == '__main__':
    main()
  
