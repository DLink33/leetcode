/**
 * @param {number[]} nums
 * @return {number[][]}
 */
export var threeSum = function (nums) {
  const rslt = [];
  const n = nums.length;
  //sort the array so we can use two pointer technique
  nums.sort((a, b) => a - b);
  //start at the beginning of the array but stop at index n-2 since we need at least 3 numbers to make a triplet
  for (let i = 0; i < n - 2; ++i) {
    // skip adjacent duplicates since we have to have unique values
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let R = n - 1;
    let L = i + 1;
    while (L < R) {
      const sum = nums[i] + nums[L] + nums[R];
      if (sum === 0) {
        rslt.push([nums[i], nums[L], nums[R]]);
        // we need to move both pointers because we found a valid triplet
        L++;
        R--;
        while (L < R && nums[L] === nums[L - 1]) L++; // skip adjacent duplicates on the leff
        while (L < R && nums[R] === nums[R + 1]) R--; // skip adjacent duplicates on the right
      } else if (sum < 0) {
        L++; // we need a larger sum if sum is less than 0
      } else {
        // we need a smaller sum if sum is greater than 0
        R--;
      }
    }
  }
  return rslt;
};
