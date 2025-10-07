#! .venv/bin/python


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Helper recursive method
        def rev(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            check = i < len(s) and (p[j] == s[i] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                return rev(i, j + 2) or (check and rev(i + 1, j))
            else:
                return check and rev(i + 1, j + 1)

        return rev(0, 0)


def main():
    sol = Solution()
    rslt = sol.isMatch("aab", "c*a*b")
    print(rslt)
    pass


if __name__ == "__main__":
    main()
