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

function isSymmetric2(root) {
  if (root === null) return true;

  const leftStack = [];
  const rightStack = [];
  let currL = root.left;
  let currR = root.right;

  while (
    currL !== null ||
    currR !== null ||
    leftStack.length ||
    rightStack.length
  ) {
    // descend as far as possible, but enforce mirror structure
    while (true) {
      if (currL === null && currR === null) break; // done descending this lane
      if (currL === null || currR === null) return false; // structural mismatch

      if (currL.val !== currR.val) return false; // value mismatch early (nice optimization)

      leftStack.push(currL);
      rightStack.push(currR);
      currL = currL.left;
      currR = currR.right;
    }

    // pop next frame
    currL = leftStack.pop();
    currR = rightStack.pop();

    // move to the cross-children
    currL = currL.right;
    currR = currR.left;
  }

  return true;
}

function main() {
  const tree = new TreeNode(
    0,
    new TreeNode(1, null, null),
    new TreeNode(1, null, null),
  );
  tree.print();
  let rslt1 = isSymmetric(tree);
  let rslt2 = isSymmetric2(tree);
  console.log(rslt1);
  console.log(rslt2);

  const tree2 = new TreeNode(
    0,
    new TreeNode(1, null, null),
    new TreeNode(2, null, null),
  );
  tree2.print();
  rslt1 = isSymmetric(tree2);
  rslt2 = isSymmetric2(tree2);
  console.log(rslt1);
  console.log(rslt2);

  const tree3 = new TreeNode(
    0,
    new TreeNode(1, null, new TreeNode(2, null, null)),
    new TreeNode(1, null, new TreeNode(2, null, null)),
  );
  tree3.print();
  rslt1 = isSymmetric(tree3);
  rslt2 = isSymmetric2(tree3);
  console.log(rslt1);
  console.log(rslt2);

  //complex tree
  const tree4 = new TreeNode(
    0,
    new TreeNode(1, new TreeNode(2, null, null), new TreeNode(3, null, null)),
    new TreeNode(1, new TreeNode(3, null, null), new TreeNode(2, null, null)),
  );
  tree4.print();
  rslt1 = isSymmetric(tree4);
  rslt2 = isSymmetric2(tree4);
  console.log(rslt1);
  console.log(rslt2);
}

main();
