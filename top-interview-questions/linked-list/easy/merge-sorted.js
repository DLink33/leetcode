// Merge Sorted Linked Lists //

/*
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

function ListNode(val, nxt) {
  this.val = val === undefined ? 0 : val;
  this.next = nxt === undefined ? null : nxt;
}

ListNode.prototype.printList = function () {
  let node = this;
  while (node !== null) {
    console.log(node.val);
    node = node.next;
  }
};

ListNode.fromArr = (list) => {
  let currNode = new ListNode(-1);
  let head = currNode;
  for (const value of list) {
    currNode.next = new ListNode(value);
    currNode = currNode.next;
  }
  return head.next;
};

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  let rsltList = new ListNode(-1, null);
  let head = rsltList;
  while (!(list1 === null || list2 === null)) {
    if (list1.val < list2.val) {
      rsltList.next = new ListNode(list1.val, null);
      list1 = list1.next;
    } else {
      rsltList.next = new ListNode(list2.val, null);
      list2 = list2.next;
    }
    rsltList = rsltList.next;
  }
  while (list1 != null) {
    rsltList.next = new ListNode(list1.val);
    list1 = list1.next;
    rsltList = rsltList.next;
  }
  while (list2 != null) {
    rsltList.next = new ListNode(list2.val);
    list2 = list2.next;
    rsltList = rsltList.next;
  }
  return head.next;
};

function main() {
  const l1 = ListNode.fromArr([1, 2, 3]);
  const l2 = ListNode.fromArr([4, 5, 6]);

  let rslt = mergeTwoLists(l1, l2);
  rslt.printList();
}

main();
