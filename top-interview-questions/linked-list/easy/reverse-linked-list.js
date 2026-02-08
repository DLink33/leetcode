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
var reverseList = function (head) {
  if (head === null || head.next === null) return head;
  let curr = head;
  let next = head.next;
  let prev = null;
  while (next !== null) {
    curr.next = prev; // reverse the next pointer at curr
    // iterate all pointers to their next value starting with prev, then curr, then next
    prev = curr;
    curr = next;
    next = next.next;
  }
  // since our next is null one step before we reverse the last curr.next.  Peform this last step manually.
  curr.next = prev;
  // return curr as new head
  return curr;
};

function main() {
  let head = new ListNode(
    1,
    new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, null)))),
  );

  head = reverseList(head);
  head.printList();
}

main();
