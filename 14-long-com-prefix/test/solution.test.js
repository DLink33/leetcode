import { describe, it, expect } from 'vitest';
import { longestCommonPrefix } from '../src/solution';

describe('test longestCommonPrefix', () => {
  it.each([
    { in: ['flower', 'flow', 'flight'], out: 'fl' },
    { in: ['dog', 'racecar', 'car'], out: '' },
    { in: ['interspecies', 'interstellar', 'interstate'], out: 'inters' },
    { in: ['a'], out: 'a' },
    { in: ['', ''], out: '' },
    { in: ['cir', 'car'], out: 'c' },
    { in: ['throne', 'dungeon'], out: '' },
    { in: ['prefix', 'prefix'], out: 'prefix' },
    { in: ['flower', 'flow', ''], out: '' },
  ])('returns $out for $in', ({ in: arr, out }) => {
    expect(longestCommonPrefix(arr)).toBe(out);
  });
});
