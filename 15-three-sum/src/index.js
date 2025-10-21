import { threeSum, threeSumNaive } from './solution.js';

function main() {
  console.log('Hello, World!');
  const nums = [2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10];
  const result0 = threeSum(nums);
  const result1 = threeSumNaive(nums);
  console.log(result0);
  console.log(result1);
}

main();
