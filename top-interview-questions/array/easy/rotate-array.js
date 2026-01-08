// ROTATE ARRAY
/*
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

NOTES:

My initial thought is to have a swap that runs through the whole array k times with modulo logic.
*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */

function swap(arr, idx1, idx2) {
  if (idx1 === idx2) return;
  arr[idx1] = arr[idx1] ^ arr[idx2];
  arr[idx2] = arr[idx1] ^ arr[idx2];
  arr[idx1] = arr[idx1] ^ arr[idx2];
}

function reverse(arr, l = 0, r = arr.length - 1) {
  while (l < r) {
    swap(arr, l, r);
    l++;
    r--;
  }
}

var rotate = function (nums, k) {
  if (k === 0) return;
  let n = nums.length;
  k %= n;
  reverse(nums, 0, n - 1); // reverse the whole arr
  reverse(nums, 0, k - 1); // reverse beginning subarr
  reverse(nums, k, n - 1); // reverse remaning arr
};

function main() {
  let arr = [1, 2, 3, 4, 5];
  //arr = [-1, -100, 3, 99];
  let k = 1;
  console.log(arr);
  rotate(arr, k);
  console.log(arr);
}

main();
