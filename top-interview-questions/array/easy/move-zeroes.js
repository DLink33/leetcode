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
var moveZeroes = function(nums) {
    const n = nums.length;
    let l = 0;
    let r = 0;
    let temp;
    while (r < n) {
        if (nums[l] !== 0) l++;
        while (true) {
            if (r === n) break;
            r++;
            if (nums[r] !== 0) {
                temp = nums[l];
                nums[l] = nums[r];
                nums[r] = temp;
                break;
            }
        }
        r++;
    }
    
};

function main() {
    const nums = [0,1,0,3,12];
    let rslt = moveZeroes(nums);
    console.log(rslt);
}

main();