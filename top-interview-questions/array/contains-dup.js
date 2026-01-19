/* global console */

// Contains Duplicate //

/*
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


NOTES:

This to me seesm like a straight forward hash map problem where we add each element as we discover it, and if it is already in the hash map, we return True.  This will allow use to pass through the array once O(n) time complexity and, at worst, O(n) space complexity if we have to go through the whole array without finding any duplicates.
*/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const numsSet = new Set();
  for (const n of nums) {
    if (!numsSet.has(n)) numsSet.add(n);
    else return true;
  }
  return false;
};

function main() {
  let nums = [];
  let rslt = containsDuplicate(nums);
  console.log(rslt);
}

main();
