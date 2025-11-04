import { describe, it, expect } from 'vitest';
import { rotateString } from '../src/solution.js';

describe('test rotateString', () => {
  it.each([
    { input: ["abcde", "cdeab"], expected: true },
    { input: ["abcde", "abced"], expected: false },
    { input: ["a", "a"], expected: true },
    { input: ["aa", "aa"], expected: true },
    { input: ["abc", "bca"], expected: true },
    { input: ["abc", "cab"], expected: true },
    { input: ["abcd", "dabc"], expected: true },
    { input: ["abcd", "abcd"], expected: true },
    { input: ["abcd", "abdc"], expected: false },
    { input: ["xyz", "yzx"], expected: true },
    { input: ["xyz", "zxy"], expected: true },
    { input: ["xyz", "xyz"], expected: true },
    { input: ["xyz", "xzy"], expected: false },
    { input: ["rotation", "tationro"], expected: true },
    { input: ["rotation", "ationrot"], expected: true },
    { input: ["rotation", "rotation"], expected: true },
    { input: ["rotation", "rotatio"], expected: false },
    { input: ["", ""], expected: true },
    { input: ["a", ""], expected: false },
    { input: ["", "a"], expected: false },
  ])('returns expected result', ({ input, expected }) => {
    const result = rotateString(...input);
    expect(result).toBe(expected);
  });
});
