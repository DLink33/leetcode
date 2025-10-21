/**
 * @param {number[]} nums
 * @return {number[][]}
 */
export var threeSum = function (nums) {
  const cands = new Set();
  const n = nums.length;
  nums.sort((a, b) => a - b);
  for (let i = 0; i < n - 2; ++i) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
  }
};
