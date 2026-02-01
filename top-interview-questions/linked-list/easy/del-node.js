// Delete Node in a Linked List //

/*
There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.
Custom testing:

For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
We will build the linked list and pass the node to your function.
The output will be the entire list after calling your function.

NOTES:

*/
class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}
class LinkedList {
  constructor() {
    this.head = null;
  }
  printList() {
    let current = this.head;
    const values = [];
    while (current) {
      values.push(current.val);
      current = current.next;
    }
    console.log(values.join(" -> "));
  }
}

LinkedList.prototype.fromArray = function (arr) {
  this.head = null;
  let current = null;

  for (const v of arr) {
    const node = new ListNode(v);
    if (!this.head) this.head = node;
    else current.next = node;
    current = node;
  }

  return this; // return the LinkedList instance
};

/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */
var deleteNode = function (node) {
  if (node === null || node.next === null) {
    return;
  }
  node.val = node.next.val;
  node.next = node.next.next;
};

function main() {
  const node1 = new ListNode(4);
  const node2 = new ListNode(5);
  const node3 = new ListNode(1);
  const node4 = new ListNode(9);

  node1.next = node2;
  node2.next = node3;
  node3.next = node4;

  deleteNode(node2);
}

main();
