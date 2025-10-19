/**
 * @param {string[]} strs
 * @return {string}
 */

export var longestCommonPrefix = function (strs) {
  let rslt = '';
  for (let i = 0; i < strs[0].length; ++i) {
    let currChar = strs[0][i];
    for (let j = 1; j < strs.length; ++j) {
      if (strs[j][i] !== currChar) return rslt;
    }
    rslt += currChar;
  }
  return rslt;
};
