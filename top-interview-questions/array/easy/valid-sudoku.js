/* global console */

// VALID SUDOKU //

/*
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

NOTES:
The big kicker here is that this puzzle doesn't have  to be solvable.  We are simily writing a function that 
checks for a valid state of the board. 

I am immediately inclined to write methods that checka for rows, columns, or neighbors (in same 3x3) given a coordinate. We can then go through each coordinate, and check if the value is valid. For blank values we can skip.

This brutet force method however will do some redundant work.  What would be better would be to make a hash map
of all coordinate and what values could be placed in there (start with 0 through 9).  When we check to see if a value is valid for any coordinate, we would first check against the hash map to see if we haven't already determined if it can have this value or not. We would then determine if it is valid. If it is, then we can go through all of the associated coordination for x and y and update their hash value to not include that number.  This could even be done recursively if we wanted until we have visited every single coordinate. Like DFS.
This might be a little more complex than what is necessary to solve this problem.  Let's just focus on the validation.

Another thought: Since iterating through columns might be annoying, We could transpose the matrix first and then we are only checking rows. 

*/

// SOLUTION //

// function transpose(board) {
//   // Check if the input is a valid 2D array
//   if (!Array.isArray(board) || !Array.isArray(board[0])) {
//     console.error("Input must be a 2D array.");
//     return [];
//   }

//   // get the dimensions of the new board
//   const numRows = board.length;
//   const numCols = board[0].length;

//   // create the new board
//   const transposed = new Array(numCols);
//   for (let i = 0; i < numCols; i++) {
//     transposed[i] = new Array(numRows);
//   }

//   // Populate the new board
//   for (let i = 0; i < numRows; i++) {
//     for (let j = 0; j < numCols; j++) {
//       transposed[j][i] = board[i][j];
//     }
//   }

//   return transposed;
// }

// regex for testing char in each location
const validChars = /^[.1-9]$/i;

function checkRow(board, [x, y], val) {
  const m = board[0].length;
  const row = board[y];
  for (let j = 0; j < m; j++) {
    if (j !== x && row[j] === val) return false;
  }
  return true;
}

function checkColumn(board, [x, y], val) {
  const n = board.length;
  for (let i = 0; i < n; i++) {
    if (i !== y && board[i][x] === val) return false;
  }
  return true;
}

function checkBox(board, [x, y], val) {
  let startX = x - (x % 3);
  let startY = y - (y % 3);
  for (let i = startX; i < startX + 3; ++i) {
    for (let j = startY; j < startY + 3; ++j) {
      if (i === x && j === y) continue;
      if (board[j][i] === val) return false;
    }
  }
  return true;
}

/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  // Check if the input is a valid 2D array
  if (!Array.isArray(board) || !Array.isArray(board[0])) {
    console.error("Input must be a 2D array.");
    return false;
  }
  // First validate board dimensions (this is part of the constraints but I will test for them anyways)
  const n = board.length;
  // Number of rows has to be 9
  if (n !== 9) return false;
  // Each row has to have 9 elemens for 9 columns total
  for (const row of board) {
    let m = row.length;
    if (m !== 9) return false;
  }

  const m = 9;

  for (let i = 0; i < n; ++i) {
    let row = board[i];
    for (let j = 0; j < m; ++j) {
      let val = row[j];
      if (!validChars.test(val)) return false;
      if (val === ".") continue;
      if (
        !(
          checkRow(board, [j, i], val) &&
          checkColumn(board, [j, i], val) &&
          checkBox(board, [j, i], val)
        )
      ) {
        return false;
      }
    }
  }
  return true;
};

//// MAIN ////
function main() {
  //Smoke testing:
  let board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
  ];
  console.log(isValidSudoku(board)); // true

  board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
  ];
  console.log(isValidSudoku(board)); // false
}

main();
