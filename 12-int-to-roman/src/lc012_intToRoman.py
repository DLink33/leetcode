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
        roman = self.roman
        rslt = ""
        digits = self.numDigits(num)

        for i in range(digits):
            for div in roman[digits-(i+1)]:
                if not ((num // div[0]) == 4 or (num// div[0] == 9)):
                    numChars = num // div[0]
                    rslt = rslt + div[1]*numChars
                    if numChars:
                        num -= div[0]*numChars
                elif((num // div[0]) == 4):
                    rslt += (roman[i][0][1] + roman[i][1][1])
                    num -= (div[0]*4)
                    continue
                else:
                    rslt += (roman[i][1][1] + roman[i+1][0][1])
                    num -= (div[0]*9)
                    continue

                    
        
        return rslt


def main():
    sol = Solution()
    r = sol.numDigits(3749)
    s = sol.intToRoman(3749)
    print(s)
    pass


if __name__ == "__main__":
    main()
