// SINGLE NUBMER
/*
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

NOTES:
NOTES:
My initial thought was the naive solution to have a double for loop with a flag for if a duplicate value was not found.
I quickly implemented this, but now I have to think about how to get this in linear time complexity. 
My next thought is we could do this with a hash map in which we keep track of the frequency of each entry in the array, but this is not correct as it would require space complexity proportional to the size of the input array. Going back to the drawing board.

The hint states that we should be using XOR somehow.  I know what XOR means, but there isn't an XOR operation.  The closes you get is !==.  Ok after a bit of confusion, I realized they meant that bitwise XOR operation ^. Now this is making a little more sense.  If you XOR a number with itself, it becomes 0.  For example 2 = 010 in binary. If you XOR it with itself: 010 ^ 010 the result is 0 (000). The other thing to realize is that XOR is communicative, meaning it doesn't matter what order you perform XOR. Hence, if we keep a running XOR over each element of the array, all number that have a duplicate will cancel out to 0 and the only one remaning will be our ans:

 001 (1)
^
 010 (2)
^
 010 (2)
^
 001 (1)
^
 100 (4)
=
 100 (4)

or another way to see it:
> 1 ^ 2
3
> 3 ^ 2
1
> 1 ^ 1
0
> 0 ^ 4
4

The cool thing is that it doesn't matter the order.  It may seem like it, but it actually does matter which elems we XOR first or last:

> 4^2^1^2^1
4
> 2^2^1^4^1
4
> 2^1^4^2^1
4

Pretty neat!
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber_naive = function(nums) {
    const n = nums.length;
    let f;
    for (let i = 0; i < n; ++i){
        f = false;
        for (let j = 0; j < n; ++j) {
            if (i === j) continue;
            if (nums[i] == nums[j]) {
                f = true;
                break;
            }
        }
        if (!f) return nums[i];
    }
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let rslt = nums[0];
    for (let i = 1; i < nums.length; i++) {
        rslt ^= nums[i];
    }
    return rslt;
}

function main() {
    const nums = [4,2,1,2,1];
    console.log(singleNumber_naive(nums));
    console.log(singleNumber(nums));
}

main();