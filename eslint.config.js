import js from "@eslint/js";

export default [
  js.configs.recommended,

  // ignore stuff repo-wide
  {
    ignores: [
      "**/node_modules/**",
      "**/dist/**",
      "**/build/**",
    ],
  },

  // apply rules to your leetcode folders too
  {
    files: ["**/*.js", "**/*.mjs", "**/*.cjs"],
    rules: {
      // your overrides here
    },
  },
];

