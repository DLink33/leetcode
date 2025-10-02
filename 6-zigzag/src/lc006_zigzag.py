#! .venv/bin/python
"""

6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Handle edge cases
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ["" for _ in range(numRows)]
        cur_row = 0
        going_down = False

        for ch in s:
            rows[cur_row] += ch
            # change direction when we hit the top or bottom row
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1

        return "".join(rows)


def main():
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
    print(sol.convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
    print(sol.convert("ABCD", 2))  # ACBD
    print(sol.convert("A", 1))  # A
    print(sol.convert("ABCDE", 4))  # ABCED


if __name__ == "__main__":
    main()
