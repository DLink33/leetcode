/// Reverse Integer ///
/*
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

NOTES: We can use modulo and floor division to get the individual base-10 values from the number and add them together to produce the reversed.



*/

const MAX_INT_32 = 2147483647;
const MIN_INT_32 = -2147483648;

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  const isNeg = x < 0;
  let rslt = 0;
  let popped = 0;
  if (isNeg) x *= -1;
  while (x !== 0) {
    popped = x % 10;
    x = Math.floor(x / 10);
    if (
      rslt < MIN_INT_32 / 10 ||
      (rslt === Math.floor(MIN_INT_32 / 10) && popped < -8)
    )
      return 0;
    if (
      rslt > MAX_INT_32 / 10 ||
      (rslt === Math.floor(MAX_INT_32 / 10) && popped > 7)
    )
      return 0;
    rslt = rslt * 10 + popped;
  }
  if (isNeg) rslt *= -1;
  return rslt;
};

function main() {
  let n = 7463847413;
  console.log(reverse(n));
}

main();
