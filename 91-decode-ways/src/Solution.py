class Solution:
    def numDecodings(self, s: str) -> int:
        n:int = len(s)
        dp:list[int] = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1 if int(s[0]) != 0 else 0

        for i in range(2, n+1):
            if int(s[i-1]) >= 1 and int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
            if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[n]

    def _decode_token(self, token: str) -> str:
        return chr(ord('A') + int(token) - 1)

    def printDecodings(self, s: str) -> tuple[int, list[str]]:
        n = len(s)
        if n == 0:
            return 0, []

        dp = [0] * (n + 1)
        decodings: list[list[str]] = [[] for _ in range(n + 1)]

        dp[0] = 1
        decodings[0] = ['']

        if s[0] != '0':
            dp[1] = 1
            decodings[1] = [self._decode_token(s[0])]
        else:
            dp[1] = 0
            decodings[1] = []

        for i in range(2, n + 1):
            one = s[i - 1]
            two = s[i - 2:i]

            # single-digit
            if '1' <= one <= '9':
                dp[i] += dp[i - 1]
                for decoded in decodings[i - 1]:
                    decodings[i].append(decoded + self._decode_token(one))

            # two-digit
            if '10' <= two <= '26':
                dp[i] += dp[i - 2]
                for decoded in decodings[i - 2]:
                    decodings[i].append(decoded + self._decode_token(two))

        return dp[n], decodings[n]


             
        

def main():
    sol: Solution = Solution()
    s:str = '121'
    print(sol.numDecodings(s))
    print(sol.printDecodings(s))

if __name__ == '__main__':
    main()

