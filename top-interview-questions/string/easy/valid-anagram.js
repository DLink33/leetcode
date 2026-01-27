/// Is Valid Anagram ///

/*

NOTES: This can be done with two maps and comparing if they are the same after going through each string.  We can use a single map and add str counts from the first string and remove counts from the second string.  If we ever have a value in the map that is negative, we know to return false. If our count goes down to 0, we can delete the entry in the map. At the end, we return map.size === 0.
*/

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  const n = s.length;
  const m = t.length;
  if (n !== m) return false;

  const map = new Map();

  for (const chr of s) {
    map.set(chr, (map.get(chr) ?? 0) + 1);
  }

  for (const chr of t) {
    let count = (map.get(chr) ?? 0) - 1;
    if (count < 0) return false;
    if (count === 0) map.delete(chr);
    else map.set(chr, count);
  }
  return map.size === 0;
};

function main() {
  const s1 = "ab";
  const s2 = "bb";
  console.log(isAnagram(s1, s2));
}

main();
