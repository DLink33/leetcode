// Linked List Cycle Detection //

/*
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
*/

class ListNode {
  constructor(val, next) {
    this.val = val ?? 0;
    this.next = next ?? null;
  }
  static fromArr(list) {
    let curr = new ListNode(-1);
    let head = curr;
    for (const value of list) {
      curr.next = new ListNode(value);
      curr = curr.next;
    }
    return head.next;
  }
  printList() {
    let curr = this;
    while (curr !== null) {
      console.log(curr.val);
      curr = curr.next;
    }
  }
}

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
  if (head?.next == null) return false; //guard for null head or a single value (head.next === null)
  let fast = head;
  let slow = head;

  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
    if (fast === slow) return true;
  }
  return false;
};

function main() {
  const list = ListNode.fromArr([1, 2, 3]);
  let node = list;
  while (node.next !== null) node = node.next;
  node.next = list;
  console.log(hasCycle(list));
}

main();
