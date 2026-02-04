// Reverse Linked List //

/*
Given the head of a singly linked list, reverse the list, and return the reversed list.
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

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {};

function main() {}

main();
