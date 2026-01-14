// PLUS ONE //
/*
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.


NOTES:
We can iterate backwards through the array.  If our current value is 9 we know we are going to have to carry.
We set our carry and current value at the current digit appropriately. If we don't have a carry (i.e. carry is 0)
then we can break out of the loop early.  If we get to the end and we still have a carry, we are going to need to splice in a 1 into the beginning of the array. 
*/

/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    const n = digits.length;
    let carry = 1;
    let val = 0;
    for (let i=n-1; i >=0; --i) {
        let currDigit = digits[i];
        if (currDigit !== 9) {
            val = (carry+currDigit);
            carry = 0;
        } else {
            val = 0;
            carry = 1;
        }
        digits[i] = val;
        if (carry === 0) break;
        if( i===0 && carry !== 0) {
            digits.splice(0, 0, carry);
        }
    }
    return digits;
};

function main() {
    let a = [1, 2];
    console.log(plusOne(a));
}

main();