// Binary Tree Level Order Traversal //

/*
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

NOTES:

Initial thoughts is that this is just a BFS of the tree starting at the root. So we will use a queue instead of a stack in our iteration.
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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    if (root === null) return [];
    const rslt = [];
    const q = [root];
    while (q.length) {
        const lvlSize = q.length;
        const lvl = [];
        for(let i=0; i < lvlSize; ++i) {
            const currNode = q.pop()
            lvl.push(currNode.val);
            if (currNode.left) {
                q.unshift(currNode.left);
            }
            if (currNode.right) {
                q.unshift(currNode.right);
            }
        }
        rslt.push(lvl);
    }
    return rslt;
};
