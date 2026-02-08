// Delete Nth Node in Linked List //

/*
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Notes:
This should be a matter of traversing the linked list node by node and tracking our index. When we reach the n-1th node, we can perform our removal:
1. save ref to removal node's next
2. change current node's next to removal node's next

Special case for removing the head (index 0)
we will just simply set the head's next to null and save the new head as the second to next node in the list.

*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

ListNode.prototype.printList = function () {
  let node = this;
  while (node !== null) {
    console.log(node.val);
    node = node.next;
  }
};

/*
same as using class syntax:
class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
  printList() {
    let node = this;
    while (node !== null) {
      console.log(node.val);
      node = node.next;
    }
  }
}

*/

/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  const dummy = new ListNode(0, head);
  let slow = dummy;
  let fast = dummy;
  // progress left pointer to n + 1
  for (let i = 0; i < n + 1; ++i) {
    fast = fast.next;
  }
  // progress left and right pointers until the right reaches the end of the linked list
  while (fast !== null) {
    fast = fast.next;
    slow = slow.next;
  }
  //delete
  const temp = slow.next;
  slow.next = slow.next.next;
  temp.next = null;

  return dummy.next;
};

function main() {
  let head = new ListNode(1, new ListNode(2, new ListNode(3, null)));
  head.printList();
  head = removeNthFromEnd(head, 3);
  head.printList();
}

main();
