from typing import Any

from SinglyLinkedList import SinglyLinkedList


class Queue:
    def __init__(self):
        self.list: SinglyLinkedList = SinglyLinkedList()

    def __len__(self):
        return self.list.len

    def __str__(self) -> str:
        rslt: list[int] = []
        curr: SinglyLinkedList.Node | None = self.list.head
        while curr:
            rslt.append(curr.val)
            curr = curr.nxt
        return str(rslt)

    def enqueue(self, val):
        self.list.append(val)

    def dequeue(self):
        old_head = self.list.head
        if old_head is None:
            return None
        rslt = old_head.val

        # Set new head to the next value of the old head
        self.list.head = old_head.nxt
        self.list.len -= 1

        # in the event we dequeue the last element, we need
        # to ensure that the tail pointer also points to None
        if self.list.head is None:
            self.list.tail = None

        # detach old head completely
        old_head.nxt = None

        return rslt

    def peek(self):
        if self.list.head:
            return self.list.head.val
        return None

    def is_empty(self):
        if self.list.head:
            return False
        return True


def main():
    # Smoke tests
    my_queue = Queue()
    print(f"queue: {my_queue}")
    print(f"queue head: {my_queue.list.head}")
    print(f"queue tail: {my_queue.list.tail}")

    my_queue.enqueue(111)
    print(f"queue: {my_queue}")
    print(f"queue head: {my_queue.list.head}")
    print(f"queue tail: {my_queue.list.tail}")

    my_queue.enqueue(222)
    print(f"queue: {my_queue}")
    print(f"queue head: {my_queue.list.head}")
    print(f"queue tail: {my_queue.list.tail}")

    my_queue.enqueue(333)
    print(f"queue: {my_queue}")
    print(f"queue head: {my_queue.list.head}")
    print(f"queue tail: {my_queue.list.tail}")

    x: Any = my_queue.peek()
    print(f"peek: {x}")

    x: Any = my_queue.dequeue()
    print(f"queue: {my_queue}")
    print(f"queue head: {my_queue.list.head}")
    print(f"queue tail: {my_queue.list.tail}")
    print(f"dequed value: {x}")

    x: Any = my_queue.dequeue()
    print(f"queue: {my_queue}")
    print(f"queue head: {my_queue.list.head}")
    print(f"queue tail: {my_queue.list.tail}")
    x: Any = my_queue.dequeue()
    print(f"queue: {my_queue}")
    print(f"queue head: {my_queue.list.head}")
    print(f"queue tail: {my_queue.list.tail}")

    print(f"len: {len(my_queue)}")


if __name__ == "__main__":
    main()
