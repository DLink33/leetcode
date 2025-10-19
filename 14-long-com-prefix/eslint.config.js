// eslint.config.js
import js from '@eslint/js';
import eslintPluginImport from 'eslint-plugin-import';
import eslintPluginUnusedImports from 'eslint-plugin-unused-imports';
import globals from 'globals';

export default [
  { ignores: ['node_modules', 'dist', 'coverage'] },

  {
    files: ['**/*.{js,mjs,cjs}'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      // 👇 This line tells ESLint about Node built-ins like console, process, __dirname, etc.
      globals: { ...globals.node },
    },
    plugins: {
      import: eslintPluginImport,
      'unused-imports': eslintPluginUnusedImports,
    },
    rules: {
      ...js.configs.recommended.rules,

      'import/first': 'error',
      'import/newline-after-import': 'error',
      'import/no-duplicates': 'error',

      'unused-imports/no-unused-imports': 'error',
      'unused-imports/no-unused-vars': [
        'warn',
        {
          vars: 'all',
          args: 'after-used',
          ignoreRestSiblings: true,
          argsIgnorePattern: '^_',
          varsIgnorePattern: '^_',
        },
      ],

      'no-console': 'off',
      'no-constant-condition': ['error', { checkLoops: false }],
    },
  },

  // (optional) If you have Vitest tests, enable test globals in test files:
  // {
  //   files: ['test/**/*.{js,ts}'],
  //   languageOptions: { globals: { ...globals.node, ...globals.jest } } // Vitest uses Jest-like globals
  // }
];
