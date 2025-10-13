class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rslt = 0
        cand = ""
        for i in range(0, len(s), 1):
            cand = s[i]
            rslt = max(rslt, len(cand))
            for j in range(i + 1, len(s), 1):
                if s[j] in cand:
                    break
                cand += s[j]
                rslt = max(rslt, len(cand))
        return rslt


def main():
    s = "abcabcbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))


if __name__ == "__main__":
    main()
