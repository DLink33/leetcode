/**
 * @param {string[]} strs
 * @return {string}
 */

export var longestCommonPrefix = function (strs) {
  let rslt = '';
  // check all strings against the first string
  for (let i = 0; i < strs[0].length; ++i) {
    let currChar = strs[0][i];
    // start our inner loop index from the second str (j=1) since we are checking against the 0th str
    for (let j = 1; j < strs.length; ++j) {
      if (strs[j][i] !== currChar) return rslt;
    }
    // Add char if it is found in every string within the array at position i
    rslt += currChar;
  }
  return rslt;
};
