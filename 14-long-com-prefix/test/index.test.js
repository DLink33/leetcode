import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { greet } from '../src/index.js';

let logSpy;

beforeEach(() => {
  //prevents real printing and capture calls
  logSpy = vi.spyOn(console, 'log').mockImplementation(() => {});
});

afterEach(() => {
  logSpy.mockRestore();
});

// Tests the return values of 'greet' function
describe('greet', () => {
  it('greet default', () => {
    expect(greet()).toBe('Hello world!');
  });
  it('greet name', () => {
    expect(greet('vulp')).toBe('Hello vulp!');
  });
});

// Tests the 'greet' function's ability to print out to console
describe('report', () => {
  it('prints deafult greeting', () => {
    greet();
    expect(logSpy).toHaveBeenCalledTimes(1);
    expect(logSpy).toHaveBeenCalledWith('Hello world!');
  });
  it('prints greeting with name', () => {
    greet('vulp');
    expect(logSpy).toHaveBeenCalledWith('Hello vulp!');
  });
});
