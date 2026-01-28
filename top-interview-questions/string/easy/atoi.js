// String to Ingeter //

/*
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

NOTES:
We could use a regex to remove all leading whitespace.
A boolean can be used to track if our value is negative or not
Can return early if we detect a non-numerical character after any potential signed char ('+' or '-').
There are plenty of built-in functions that can be used to determine the numerical, base-10 value of a char 0-9, however, it might be more pertinent to develop this ourselves. We can do this by creating a map or an obj, that hashes this correlation.

*/

/**
 * @param {string} s
 * @return {number}
 */
/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function (s) {
  const INT_MAX = 2147483647;
  const INT_MIN = -2147483648;

  let i = 0;
  const n = s.length;

  // 1) skip leading spaces
  while (i < n && s[i] === " ") i++;

  // 2) optional sign
  let sign = 1;
  if (i < n && (s[i] === "+" || s[i] === "-")) {
    if (s[i] === "-") sign = -1;
    i++;
  }

  // 3) parse digits
  let res = 0;
  while (i < n) {
    const c = s[i];
    if (c < "0" || c > "9") break;

    const digit = c.charCodeAt(0) - 48;

    // 4) overflow check BEFORE res = res * 10 + digit
    if (sign === 1) {
      if (
        res > Math.floor(INT_MAX / 10) ||
        (res === Math.floor(INT_MAX / 10) && digit > 7)
      ) {
        return INT_MAX;
      }
    } else {
      // INT_MIN has magnitude 2147483648, so last digit threshold is 8
      if (
        res > Math.floor(2147483648 / 10) ||
        (res === Math.floor(2147483648 / 10) && digit > 8)
      ) {
        return INT_MIN;
      }
    }

    res = res * 10 + digit;
    i++;
  }

  return sign * res;
};

function main() {
  let s = "123";
  console.log(myAtoi(s));
}

main();
