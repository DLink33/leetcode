// Symmetric Tree //

/*
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
*/

function TreeNode(val, left, right) {
  this.val = val ?? null;
  this.left = left ?? null;
  this.right = right ?? null;
}

TreeNode.prototype.print = function () {
  console.log(this.val);
  if (this.left) {
    this.left.print();
  }
  if (this.right) {
    this.right.print();
  }
};

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function (root) {
  function isMirror(left, right) {
    if (left === null && right === null) {
      return true;
    }
    if (left === null || right === null || left.val !== right.val) {
      return false;
    }

    // it is symmetric if the outer leaves match and if the inner leaves match
    return isMirror(left.left, right.right) && isMirror(left.right, right.left);
  }
  if (root === null) return true;
  return isMirror(root.left, root.right);
};

function main() {
  const tree = new TreeNode(
    0,
    new TreeNode(1, null, null),
    new TreeNode(1, null, null),
  );
  tree.print();
  let rslt = isSymmetric(tree);
  console.log(rslt);

  const tree2 = new TreeNode(
    0,
    new TreeNode(1, null, null),
    new TreeNode(2, null, null),
  );
  tree2.print();
  rslt = isSymmetric(tree2);
  console.log(rslt);

  const tree3 = new TreeNode(
    0,
    new TreeNode(1, null, new TreeNode(2, null, null)),
    new TreeNode(1, null, new TreeNode(2, null, null)),
  );
  tree3.print();
  rslt = isSymmetric(tree3);
  console.log(rslt);

  //complex tree
  const tree4 = new TreeNode(
    0,
    new TreeNode(1, new TreeNode(2, null, null), new TreeNode(3, null, null)),
    new TreeNode(1, new TreeNode(3, null, null), new TreeNode(2, null, null)),
  );
  tree4.print();
  rslt = isSymmetric(tree4);
  console.log(rslt);
}

main();
