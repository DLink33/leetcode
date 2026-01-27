import js from "@eslint/js";
import globals from "globals"; // 1. Import globals

export default [
  js.configs.recommended,

  // ignore stuff repo-wide
  {
    ignores: ["**/node_modules/**", "**/dist/**", "**/build/**"],
  },

  // apply rules to your leetcode folders too
  {
    files: ["**/*.js", "**/*.mjs", "**/*.cjs"],
    languageOptions: {
      // 2. Define the environment globals here
      globals: {
        ...globals.browser,
        ...globals.node,
      },
    },
    rules: {
      // 3. Optional: disable the warning if you want to allow console.log
      "no-console": "off",
    },
  },
];
