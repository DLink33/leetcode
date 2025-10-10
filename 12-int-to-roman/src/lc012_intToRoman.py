#! .venv/bin/python


class Solution:
    def __init__(self):
        self.roman = (
            [(5, "V"), (1, "I")],
            [(50, "L"), (10, "X")],
            [(500, "D"), (100, "C")],
            [(1000, "M")],
        )

    def numDigits(self, num: int) -> int:
        rslt = 0
        while num > 0:
            num //= 10
            rslt += 1
        return rslt

    def intToRoman(self, num: int) -> str:
        roman = self.roman
        rslt = ""
        digits = self.numDigits(num)
        i = 0
        while i < digits:
            p = digits - i - 1  # place power (3=thousands, 2=hundreds, 1=tens, 0=ones)
            d = (num // (10**p)) % 10  # current digit at this place

            if p == 3:  # thousands
                rslt += "M" * d
            else:
                one = roman[p][1][1]  # I, X, C
                five = roman[p][0][1]  # V, L, D
                # next place's "ten" symbol: use its 'one' if present, else the only symbol (thousands)
                nxt = roman[p + 1]
                ten = nxt[1][1] if len(nxt) > 1 else nxt[0][1]  # X, C, M

                if d <= 3:
                    rslt += one * d
                elif d == 4:
                    rslt += one + five
                elif d <= 8:
                    rslt += five + one * (d - 5)
                else:  # d == 9
                    rslt += one + ten

            i += 1

        return rslt


def main():
    sol = Solution()
    # r = sol.numDigits(3749)
    s = sol.intToRoman(3749)
    print(s)
    pass


if __name__ == "__main__":
    main()
