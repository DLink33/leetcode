from Stack import Stack


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 1:
            return False
        valid_chars: dict[str, str] = {")": "(", "}": "{", "]": "["}
        myStack: Stack = Stack()

        pop = myStack.pop
        push = myStack.push
        peek = myStack.peek
        is_empty = myStack.is_empty

        for char in s:
            if char in valid_chars:
                if is_empty():
                    return False
                if peek() != valid_chars[char]:
                    return False
                pop()
            else:
                push(char)
        return is_empty()


def main():
    # smoke tests
    seq: str = "([])"
    sol: Solution = Solution()
    rslt: bool = sol.isValid(seq)
    print(seq)
    print(rslt)


if __name__ == "__main__":
    main()
