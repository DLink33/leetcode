// Palindromic Linked List //

/*
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

NOTES:
Initially, I am thinking I can prob out all of the values of the linked list into an array, and then use a standard two-pointer solution on the array to determine if the linked list is a palindrome or not.  However, the challenge here should be to do this is O(n) time and O(1) space.  I will have to do some more thinking on this...

Ok, after thinking about this for a second, I think we can do this with a stack.  All we should have to do is push to the stack values as we see them. Before pushing to the stack, we will check the to see if the current value matched the peeked stack value. If it is the same then we will pop the val off of the stack. If by the end of iterating through the linked list we have a stack of size 0, then we know we have a palindrome.

Alirght, this will work but only for certain cases.  Instead, I have a new idea thanks to a hint: 
We can have a "slow" and a "fast" pointer for the linked list.  The fast pointer will traverse the list twice as fast as the slow pointer.  When the fast pointer has reached the end of the linked list, the slow will be at the mid point.  We can then reverse list from slow to fast and compare it to the original.  If there is not mismatc before we reach the end of the reversed list, then we can assume we have a palindrome.


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

var reverseList = function (head) {
  if (head?.next == null) return false; //guard for null head or a single value (head.next === null)
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

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {
  let fast = head;
  let slow = head;
  while (fast.next !== null) {
    fast = fast.next?.next ?? fast.next;
    slow = slow.next;
  }
  let rev2ndHalf = reverseList(slow);
  let firstHalf = head;
  while (rev2ndHalf !== null) {
    if (rev2ndHalf.val !== firstHalf.val) return false;
    rev2ndHalf = rev2ndHalf.next;
    firstHalf = firstHalf.next;
  }
  return true;
};

function main() {
  const list = ListNode.fromArr([1, 2, 2, 1]);
  let rslt = isPalindrome(list);
  console.log(rslt);
}

main();
