from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def getSize(self, head: Optional[ListNode]) -> int:
        curr: Optional[ListNode] = head
        rslt: int = 0
        while curr:
            rslt += 1
            curr = curr.next
        return rslt

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = self.getSize(head)

        curr: Optional[ListNode] = head
        prev: ListNode = None
        counter = 0

        while size - counter > n:
            prev = curr
            curr = curr.next
            counter += 1
        if curr == head:
            head = curr.next
            return head
        prev.next = curr.next
        return head
