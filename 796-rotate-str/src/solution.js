/* 
796. Rotate String

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.
*/

/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
export var rotateString = function(s, goal) {
  let n = s.length;
  if (n !== goal.length) return false;
  if (s === goal) return true;

  let sCpy = s;
  do {
    s = s.concat(s[0]);
    s = s.slice(1,n+1);
    if (s === goal) return true;
  } while (s !== sCpy);

  return false;
};

function main() {
  let s = 'abcde';
  let rslt = rotateString(s, 'cdeab');
  console.log(rslt);
}

main()
