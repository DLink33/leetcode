from __future__ import annotations

from typing import Any, Iterator, Optional, Self


class SinglyLinkedList:
    class Node:
        def __init__(self, val: Any, nxt: Self | None = None):
            self.val: Any = val
            self.nxt: Self | None = nxt

        def __str__(self) -> str:
            return str(self.val)

        def __repr__(self) -> str:
            nxt = "Node" if self.nxt is not None else "None"
            return f"Node(val={self.val!r}, next={nxt})"

        def __eq__(self, other: object) -> bool:
            if isinstance(other, self.__class__):
                return other.val == self.val
            return NotImplemented

        def __ne__(self, other: object) -> bool:
            if isinstance(other, self.__class__):
                return other.val != self.val
            return NotImplemented

        def __lt__(self, other: object) -> bool:
            if isinstance(other, self.__class__):
                return self.val < other.val
            return NotImplemented

        def __le__(self, other: object) -> bool:
            if isinstance(other, self.__class__):
                return self.val <= other.val
            return NotImplemented

        def __gt__(self, other: object) -> bool:
            if isinstance(other, self.__class__):
                return self.val > other.val
            return NotImplemented

        def __ge__(self, other: object) -> bool:
            if isinstance(other, self.__class__):
                return self.val >= other.val
            return NotImplemented

        def __copy__(self) -> object:
            return SinglyLinkedList.Node(self.val, self.nxt)

        def __iter__(self) -> Iterator[Any]:
            curr: Optional[Self] = self
            while curr is not None:
                yield curr
                curr: Optional[Self] = curr.nxt

    def __init__(self):
        self.head: Optional[SinglyLinkedList.Node] = None
        self.tail: Optional[SinglyLinkedList.Node] = None
        self.len: int = 0

    def __len__(self) -> int:
        return self.len

    def __str__(self) -> str:
        rslt: list[Any] = []
        curr: SinglyLinkedList.Node | None = self.head
        while curr:
            rslt.append(curr.val)
            curr = curr.nxt
        return str(rslt)

    def append(self, val: Any) -> None:
        node_to_add: Optional[SinglyLinkedList.Node] = self.Node(val)
        if self.tail is None:  # empty list case
            self.head = self.tail = node_to_add
            self.len = 1
            return
        self.tail.nxt = node_to_add
        self.tail = node_to_add
        self.len += 1

    def reverse(self) -> None:
        if self.len <= 1 or self.head is None:
            return
        # Swap head and tail
        temp: SinglyLinkedList.Node = self.tail
        self.tail = self.head
        self.head = temp

        # init prev, curr, and nxt pointers
        curr: SinglyLinkedList.Node = self.tail
        nxt: SinglyLinkedList.Node | None = self.tail.nxt
        prev: SinglyLinkedList.Node | None = None

        # move down the chain of nodes until the next pointer is pointing to None
        #   i.   point the current pointer to the previous node (or None)
        #   ii.  point the previous pointer to the current node
        #   iii. point the current pointer to the next node
        #   iv.  point the next pointer to the current node's next node
        #   v.   set the current node's next node to the previous node
        while nxt:
            curr.nxt = prev
            prev = curr
            curr = nxt
            nxt = curr.nxt
            curr.nxt = prev

    def remove_nth_node_from_end(self, n: int) -> SinglyLinkedList.Node | None:
        if self.head is None or n == 0:
            return self.head
        if self.len == 1 and n == 1:
            self.head = None
            self.tail = None
            self.len = 0
            return None
        dummy: SinglyLinkedList.Node = SinglyLinkedList.Node(None, self.head)
        right: SinglyLinkedList.Node | None = self.head
        left: SinglyLinkedList.Node | None = dummy
        count: int = 0

        # give right pointer an n-spaced head start
        while count < n:
            if right is None:
                return self.head
            count += 1
            right = right.nxt

        # increment left, right until right reaches the end of the Linked List
        while right is not None:
            left = left.nxt
            right = right.nxt

        # left is one behind the target node to delete
        target: SinglyLinkedList.Node | None = left.nxt
        left.nxt = target.nxt  # skip the target node since we are removing it

        # if left is dummy, we didn't move the pointers at all
        # i.e. we are removing the one and only node in the list
        if left is dummy:
            self.head = dummy.nxt

        if target is self.tail:
            self.tail = left

        self.len -= 1
        return self.head

    def has_cycle(self) -> bool:
        hare = self.head
        tortoise = self.head
        while hare and hare.nxt:
            tortoise = tortoise.nxt
            hare = hare.nxt.nxt
            if tortoise is hare:
                return True
        return False


def main():
    my_linked_list: SinglyLinkedList = SinglyLinkedList()
    print(my_linked_list)
    my_linked_list.append(0)
    my_linked_list.append(1)
    my_linked_list.append(2)
    print(my_linked_list)
    my_linked_list.reverse()
    print(my_linked_list)
    my_linked_list.append(3)
    print(my_linked_list)
    print(my_linked_list.head)
    print(my_linked_list.tail)
    print(my_linked_list.has_cycle())

    print(my_linked_list)
    print(my_linked_list.len)

    my_linked_list.remove_nth_node_from_end(2)
    print(my_linked_list)
    print(my_linked_list.len)

    my_linked_list.remove_nth_node_from_end(100)
    print(my_linked_list)
    print(my_linked_list.len)

    my_linked_list.remove_nth_node_from_end(1)
    print(my_linked_list)
    print(my_linked_list.len)

    my_linked_list.remove_nth_node_from_end(1)
    print(my_linked_list)
    print(my_linked_list.len)

    my_linked_list.remove_nth_node_from_end(1)
    print(my_linked_list)
    print(my_linked_list.len)


if __name__ == "__main__":
    main()
