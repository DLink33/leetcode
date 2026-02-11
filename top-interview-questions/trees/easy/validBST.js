// Valid Binary Search Tree //
/*
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

class TreeNode {
  constructor(val, left, right) {
    this.val = val ?? null;
    this.left = left ?? null;
    this.right = right ?? null;
  }
  printTree() {
    console.log(this.val);
    if (this.left) this.printTree(this.left);
    if (this.right) this.printTree(this.right);
  }
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
  function helper(node, lo = -Infinity, hi = Infinity) {
    if (node === null) return true;
    if (node.val <= lo || node.val >= hi) return false;
    return helper(node.left, lo, node.val) && helper(node.right, node.val, hi);
  }
  return helper(root);
};

function main() {
  const root = new TreeNode(
    10,
    new TreeNode(5),
    new TreeNode(15, new TreeNode(6), new TreeNode(20)),
  );

  console.log(isValidBST(root)); // Output: false
}

main();
