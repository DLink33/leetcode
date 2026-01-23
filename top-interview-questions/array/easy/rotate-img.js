/// Rotate Image ///

/*
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
*/

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {};

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
  console.assert(
    JSON.stringify(matrix) === JSON.stringify(out),
    "Matrix rotation failed",
  );
}

main();
