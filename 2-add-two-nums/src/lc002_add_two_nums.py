#! .venv/bin/python

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        rsltStr = "\n"
        currNode = self
        while currNode:
            rsltStr += " " + str(currNode.val) + " ->"
            currNode = currNode.next
        return rsltStr + " None\n"

    def toInt(self) -> int:
        n = 0
        m = 1
        currNode = self
        while currNode:
            n += currNode.val * m
            m *= 10
            currNode = currNode.next
        return n


class LinkedIntList:
    def __init__(self, n: int):
        self.head = self.intLinkedList(n)

    def intLinkedList(self, n: int) -> "ListNode | None":
        rslt = ListNode()
        if n == 0:
            return rslt
        currNode = rslt
        while n > 0:
            currVal = n % 10
            n //= 10
            currNode.next = ListNode(currVal, None)
            currNode = currNode.next
        return rslt.next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        rslt = ListNode()
        currNode1 = l1
        currNode2 = l2
        currRsltNode = rslt
        while currNode1 or currNode2:
            val = 0
            if currNode1:
                val += currNode1.val
                currNode1 = currNode1.next
            if currNode2:
                val += currNode2.val
                currNode2 = currNode2.next
            val += carry
            carry = val // 10
            val %= 10
            currRsltNode.next = ListNode(val, None)
            currRsltNode = currRsltNode.next
        return rslt.next


def main():
    # num1 = 342
    # num2 = 465
    num1 = 0
    num2 = 0

    s = Solution()
    l1 = LinkedIntList(num1).head
    l2 = LinkedIntList(num2).head
    rslt = s.addTwoNumbers(l1, l2)
    if rslt is not None:
        print(f"Linked List Result:\n{rslt}")
        print(f"Linked List to Int: {rslt.toInt()}")
    else:
        print("Result is None")


if __name__ == "__main__":
    main()
