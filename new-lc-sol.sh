#!/usr/bin/env bash
set -euo pipefail
name="${1:?usage: new-lc <kebab-name>}"
dir="$HOME/projects/leetcode/$name"
mkdir -p "$dir"/{src,test}
cd "$dir"
[ -f package.json ] || npm init -y >/dev/null
corepack prepare pnpm@9.12.0 >/dev/null
pnpm pkg set packageManager="pnpm@9.12.0" >/dev/null
pnpm add -D vitest >/dev/null
jq '.type="module" | .scripts += {"test":"vitest run","test:watch":"vitest"}' package.json > package.tmp && mv package.tmp package.json
cat > src/solution.js <<'JS'
export function solve(/* your inputs */) {
  // TODO: implement
  return null;
}
JS
cat > test/solution.test.js <<'JS'
import { describe, it, expect } from 'vitest';
import { solve } from '../src/solution.js';

describe('solve', () => {
  it.each([
    // { input: ..., expected: ... },
  ])('returns expected result', ({ input, expected }) => {
    expect(solve(input)).toEqual(expected);
  });
});
JS
printf "node_modules/\ncoverage/\npnpm-lock.yaml\n" > .gitignore
echo "Project ready in $dir"; ls -R

