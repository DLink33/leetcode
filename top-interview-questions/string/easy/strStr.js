// Implement strStr() //

/*

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

NOTES:

Initial thoughts are to 

*/

function buildLps(str) {
  const n = str.length;
  const lps = new Array(n).fill(0);
  let i = 1;
  let j = 0;

  while (i < n) {
    if (str[j] === str[i]) {
      j++;
      lps[i] = j;
      i++;
    } else if (j > 0) {
      j = lps[j - 1];
    } else {
      lps[i] = 0;
      i++;
    }
  }
  return lps;
}

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
  const m = needle.length;
  if (m === 0) return 0;
  const n = haystack.length;
  if (n < m) return -1;

  let lsp = buildLps(needle);

  let i = 0;
  let j = 0;
  while (i < n) {
    if (haystack[i] === needle[j]) {
      i++;
      j++;
      if (j === m) return i - m;
    } else if (j > 0) {
      j = lsp[j - 1];
    } else {
      i++;
    }
  }
  return -1;
};

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr_naive = function (haystack, needle) {
  const m = needle.length;
  if (m === 0) return 0;
  const n = haystack.length;
  if (n < m) return -1;
  let i;
  let k;
  for (i = 0; i <= n - m; i++) {
    k = 0;
    while (k < m && haystack[i + k] === needle[k]) {
      k++;
    }
    if (k === m) return i;
  }
  return -1;
};

function main() {
  const needle = "issip";
  const haystack = "mississippi";
  let rslt = strStr_naive(haystack, needle);
  console.log(rslt);
  rslt = strStr(haystack, needle);
  console.log(rslt);
}

main();
