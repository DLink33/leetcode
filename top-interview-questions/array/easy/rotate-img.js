/// Rotate Image ///

/*
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
*/

function transposeSqrMatrix(matrix) {
  const n = matrix.length;
  for (let i = 0; i < n; ++i) {
    for (let j = i; j < n; ++j) {
      if (i !== j) [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
    }
  }
}

function reverseArr(arr) {
  const n = arr.length;
  let r = n - 1;
  let l = 0;
  while (l <= r) {
    [arr[l], arr[r]] = [arr[r], arr[l]];
    l++;
    r--;
  }
}

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
  const n = matrix.length;
  for (let i = 0; i < n; ++i) {
    for (let j = i; j < n; ++j) {
      if (i !== j) [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
    }
    reverseArr(matrix[i]);
  }
};

function main() {
  let matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ];
  const out = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
  ];
  console.log(matrix);
  rotate(matrix);
  console.log(matrix);
  console.assert(
    JSON.stringify(matrix) === JSON.stringify(out),
    "Matrix rotation failed",
  );
}

main();
