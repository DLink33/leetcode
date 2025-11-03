from typing import Any

from SinglyLinkedList import SinglyLinkedList


class Stack:
    def __init__(self):
        self.list: SinglyLinkedList = SinglyLinkedList()

    def __len__(self):
        return self.list.len

    def __str__(self) -> str:
        rslt: list[int] = []
        curr = self.list.head
        while curr:
            rslt.append(curr.val)
            curr = curr.nxt
        return str(rslt)

    def push(self, val: Any) -> None:
        new_head = self.list.Node(val, self.list.head)
        self.list.head = new_head

        # the case where we are pushing a value to an empty stack
        if self.list.tail is None:
            self.list.tail = new_head
        self.list.len += 1

    def pop(self) -> Any:
        old_head = self.list.head

        # in the case of trying to pop from an empty stack
        if old_head is None:
            return None

        # set return value to be the old head's value
        rslt = old_head.val

        # set our new head to the next value of the old head
        self.list.head = old_head.nxt

        # in the case we only have one element remaining we have
        # to make sure the tail and the head are pointing the only
        # remaining value
        if self.list.tail is old_head:
            self.list.tail = None

        # Detach old head
        old_head.nxt = None
        self.list.len -= 1

        return rslt

    def peek(self) -> Any:
        return self.list.head.val if self.list.head else None

    def is_empty(self) -> bool:
        return self.list.len == 0


def main():
    my_stack: Stack = Stack()
    print(f"queue: {my_stack}")
    print(f"queue head: {my_stack.list.head}")
    print(f"queue tail: {my_stack.list.tail}")
    my_stack.push(111)
    my_stack.push(222)
    my_stack.push(333)
    print(f"queue: {my_stack}")
    print(f"queue head: {my_stack.list.head}")
    print(f"queue tail: {my_stack.list.tail}")
    x: int = my_stack.pop()
    print(f"popped val: {x}")
    print(f"queue: {my_stack}")
    print(f"queue head: {my_stack.list.head}")
    print(f"queue tail: {my_stack.list.tail}")
    print(f"peek: {my_stack.peek()}")
    my_stack.pop()
    print(f"queue: {my_stack}")
    print(f"queue head: {my_stack.list.head}")
    print(f"queue tail: {my_stack.list.tail}")
    my_stack.pop()
    print(f"queue: {my_stack}")
    print(f"queue head: {my_stack.list.head}")
    print(f"queue tail: {my_stack.list.tail}")


if __name__ == "__main__":
    main()
