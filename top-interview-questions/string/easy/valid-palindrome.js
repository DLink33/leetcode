/// Valid Palidrome ///

/*
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

NOTES:

This can be solved with a two-pointer system, similar to reverse string.  Could even use the reverse string solution in here to check if the given string is the same both forward and backward. We will use the two-pointer solution in isolation. 
*/
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const stripped = s.toLocaleLowerCase().replace(/[^a-z0-9]/gi, "");
  const n = stripped.length;
  let l = 0;
  let r = n - 1;
  while (l < r) {
    if (stripped[l] !== stripped[r]) return false;
    l++;
    r--;
  }
  return true;
};

function main() {
  const s = "a man, a plan, a canal: Panama";
  console.log(isPalindrome(s));
}

main();
