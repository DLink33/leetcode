import { longestCommonPrefix } from './solution.js';

export function greet(name = 'world') {
  console.log(`Hello ${name}!`);
}

function main() {
  greet('david');
  let strs = ['flower', 'flow', 'flight'];
  let rslt = longestCommonPrefix(strs);
  console.log(rslt);
}

main();
