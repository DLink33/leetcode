#! .venv/bin/python


class Solution:
    def __init__(self):
        self.roman = (
            [ (5,'V'), (1, 'I') ],
            [ (50, 'L'), (10, 'X') ],
            [ (500, 'D'), (100, 'C') ],
            [ (1000, 'M') ]
        )
    def numDigits(self, num:int) -> int:
        rslt = 0
        while (num > 0):
            num //= 10
            rslt+=1
        return rslt
    def intToRoman(self, num:int) -> str:
        digits = self.numDigits(num)

        for i in range(digits-1)    


def main():
    sol = Solution()
    r = sol.numDigits(3749)
    print(r)
    pass


if __name__ == "__main__":
    main()
