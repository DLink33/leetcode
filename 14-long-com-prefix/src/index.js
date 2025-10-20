import { longestCommonPrefix } from './solution.js';

export function greet(name = 'world') {
  let rslt = `Hello ${name}!`;
  console.log(rslt);
  return rslt;
}

function main() {
  greet('david');
  let strs = ['flower', 'flow', 'flight'];
  let rslt = longestCommonPrefix(strs);
  console.log(rslt);
}

main();
