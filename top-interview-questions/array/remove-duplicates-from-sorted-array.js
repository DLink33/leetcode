// 26. REMOVE DUPLICATES FROM SORTED ARRAY
/*
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
*/

/*
NOTES:
I am thinking a two-pointer solution could solve this problem. The left pointer will point at the boundary of the final array (k - 1), and r will point to the next value in the original array. We will first check if the len of the input array is >= 2.  If it isn't we can return 0 or 1 depending on if they gave us a empty or a single element array.  If have at least 2 elements, this will work.  Start the r at index l+1. If the elem at l is different than the elem at r, then we know we have found a new boundary for the final array. We will...
  - increment l
  - swap elems at r and l indicies
No matter what, we will always increment r.
This patter will repeat until r >= the array length.

In this way, we will always  track the end of the output array with l and iterate through all elements with r.

IMPROVEMENT IDEAS:
In an array will already all non-decreasing integers, we will perform unnecessary swaps at every iteration (i.e. will will be swapping at the same index). Since swaps are more expensive than checks, we could add a conditional that will swap if and only if l !== r.  This would save use some swaps.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  n = nums.length;
  if (n <= 1) return n;
  l = 0;
  r = l + 1;

  while (r <= n - 1) {
    if (nums[l] != nums[r]) {
      l++;
      let temp = nums[l];
      nums[l] = nums[r];
      nums[r] = temp;
    }
    r++;
  }
  return l + 1;
};

function main() {
  let nums = [1, 2, 2, 3, 4, 4, 6];
  nums = [1, 3, 5, 7, 9, 11];
  let rslt = removeDuplicates(nums);
  console.log(rslt);
}

main();
