// eslint.config.js (ESLint "flat" config; works great for JS now and TS later)
import js from '@eslint/js';

export default [
  // Ignore build artifacts and deps
  {
    ignores: ['node_modules', 'dist', 'coverage']
  },

  // Base JS rules for Node + ESM
  {
    files: ['**/*.{js,mjs,cjs}'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module'
    },
    plugins: {
      // these are loaded by name from node_modules
      'unused-imports': await import('eslint-plugin-unused-imports'),
      import: await import('eslint-plugin-import')
    },
    rules: {
      ...js.configs.recommended.rules,

      // Quality
      'no-console': 'off',
      'no-constant-condition': ['error', { checkLoops: false }],

      // Imports
      'import/first': 'error',
      'import/newline-after-import': 'error',
      'import/no-duplicates': 'error',

      // Unused code
      'unused-imports/no-unused-imports': 'error',
      'unused-imports/no-unused-vars': [
        'warn',
        { args: 'after-used', argsIgnorePattern: '^_', varsIgnorePattern: '^_' }
      ]
    }
  }
];

