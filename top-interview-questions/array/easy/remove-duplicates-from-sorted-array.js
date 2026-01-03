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
  - swap elems at r and l indicies (or set arr[l] = arr[r])
No matter what, we will always increment r.
This pattern will repeat until r >= the array length.

In this way, we will always  track the end of the output array with l (k = l+1) and iterate through all elements with r.

IMPROVEMENT IDEAS:
In an array that doesn't have duplicates, we will perform unnecessary swaps at every iteration (i.e. will will be swapping at the same index). Since swaps are more expensive than checks, we could add a conditional that will swap if and only if l !== r.  This would save use some swaps and additional memory.

After futher consideration, we don't even nee to swap, we can just set the value at index l to the value at index r since we don't care about losing the duplicate value at all (we ignore all values after index k at the end)

COMPLEXITY:
Time: O(n) proportional to the size of the array
Space 0(1)

*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let n = nums.length;
  if (n <= 1) return n;
  let l = 0;
  let r = l + 1;

  while (r < n) {
    if (nums[l] != nums[r]) {
      l++;
      nums[l] = nums[r];
    }
    r++;
  }
  return l + 1;
};

function main() {
  let nums = [1, 2, 2, 3, 4, 4, 6];
  let rslt = removeDuplicates(nums);
  console.log(rslt);
}

main();
