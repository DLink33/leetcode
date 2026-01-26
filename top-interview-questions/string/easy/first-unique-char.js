/// First Unique Character in String ///
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  const freq = new Map();
  for (const c of s) {
    freq.set(c, (freq.get(c) ?? 0) + 1);
  }
  let i = 0;
  for (const str of s) {
    if (freq.get(str) === 1) return i;
    i++;
  }
  return -1;
};

function main() {
  let str = "loveleetcode";
  console.log(firstUniqChar(str));
}

main();
