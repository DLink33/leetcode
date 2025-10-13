class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rslt: int = 0
        cand: str = ""
        for i in range(0, len(s), 1):
            cand = s[i]
            rslt = max(rslt, len(cand))
            for j in range(i + 1, len(s), 1):
                if s[j] in cand:
                    break
                cand += s[j]
                rslt = max(rslt, len(cand))
        return rslt

    def lengthOfLongestSubstring2(self, s: str) -> int:
        left: int = 0
        last: dict[str, int] = {}
        rslt: int = 0
        for right, char in enumerate(s):
            if char in last and last[char] >= left:
                left = last[char] + 1
            last[char] = right
            rslt = max(rslt, right - left + 1)
        return rslt


def main():
    s = "abcabcbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))


if __name__ == "__main__":
    main()
