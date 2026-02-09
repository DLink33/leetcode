// Max Depth of Binary Tree //

/*
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
*/

function TreeNode(val, left, right) {
  this.val = val ?? null;
  this.left = left ?? null;
  this.right = right ?? null;
}

TreeNode.prototype.printTree = function () {
  console.log(this.val);
  if (this.left) {
    this.left.printTree();
  }
  if (this.right) {
    this.right.printTree();
  }
};

/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function (root) {
  const depth = (node) => {
    if (node == null) return 0;
    return 1 + Math.max(depth(node.left), depth(node.right));
  };
  return depth(root);
};

function main() {
  const tree = new TreeNode(
    0,
    new TreeNode(1, null, null),
    new TreeNode(2, null, null),
  );
  tree.printTree();
  let rslt = maxDepth(tree);
  console.log(rslt);
}

main();
