/* global console */
// Move Zeroes //
/*
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

NOTES:
Initial thought is to do something like bubble sort does, where we "float" or "sink" the desired value(s) to one end of the array.
This can be done by swap adjacently until we reach the end of the array. We can track how many zeroes we have "collected" along the way and swap only the first 0.  This essentially makes this a two-pointer solution with one pointer at the first 0 and the second pointer at the num after the last 0. If we the next value is a 0 iterate the second pointer and first pointers 

*/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */

var moveZeroes = function (nums) {
  const n = nums.length;
  let l = 0;
  for (let r = 0; r < n; ++r) {
    if (nums[r] !== 0) {
      if (l !== r) {
        [nums[r], nums[l]] = [nums[l], nums[r]];
      }
      l++;
    }
  }
};

// Another solution that avoids writes by performing one swap and writing zeros at the end
var moveZeroes2 = function (nums) {
  let w = 0;
  for (let r = 0; r < nums.length; r++) {
    if (nums[r] !== 0) nums[w++] = nums[r];
  }
  for (; w < nums.length; w++) nums[w] = 0;
};

function main() {
  const nums = [0, 1, 0, 3, 12];
  moveZeroes(nums);
  console.log(nums);
}

main();
