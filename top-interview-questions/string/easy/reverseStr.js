// Reverse String //
/*
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

NOTES:
A two pointer solution will work for this.
*/

/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function (s) {
  const n = s.length;
  let l = 0;
  let r = n - 1;
  while (l < r) {
    [s[l], s[r]] = [s[r], s[l]];
    r--;
    l++;
  }
};

function main() {
  let str = ["h", "e", "l", "l", "o"];
  console.log(str);
  reverseString(str);
  console.log(str);
}

main();
