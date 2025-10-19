============================================================
JavaScript / Node Project Setup Guide (WSL - RHEL 8/9)
Using: Volta + pnpm + Corepack + ESLint + Prettier + Vitest
============================================================

---

1. Update OS & Install Base Tools

---

sudo dnf -y upgrade
sudo dnf -y install git curl ca-certificates
sudo dnf -y groupinstall "Development Tools"
sudo dnf -y install python3 gcc-c++ make openssl-devel

WHY:
Installs Git and cURL for version control and downloads,
and a build toolchain (gcc, make, python3, OpenSSL headers)
needed for compiling Node native modules.

CHECK:
git --version
curl --version
python3 --version
gcc --version

---

2. Install Volta (Node Toolchain Manager)

---

curl https://get.volta.sh | bash
exec $SHELL
volta --version

WHY:
Volta lets you pin Node versions per project and installs
Node/npm/pnpm globally in a reproducible way.

CHECK:
echo $PATH | tr ':' '\n' | grep volta
volta which node || true

---

3. Install Node LTS (and optionally pnpm globally)

---

volta install node@lts

# Optional:

volta install pnpm@9

WHY:
Installs a modern Node runtime via Volta. pnpm here is
optional since Corepack will manage it later.

CHECK:
node -v
which node

---

4. Enable Corepack

---

command -v corepack || npm i -g corepack
corepack --version
corepack enable

WHY:
Corepack activates the exact package-manager version
declared in each project’s package.json ("packageManager").

CHECK:
corepack list

---

5. Create Project Root & Initialize package.json

---

mkdir -p ~/projects/my-node-app && cd ~/projects/my-node-app
npm init -y

WHY:
Creates the root folder and initializes a package.json.

CHECK:
test -f package.json && echo "OK: package.json present"

---

6. Pin Node for This Project

---

volta pin node@20

WHY:
Ensures this repo always runs with Node 20.x.

CHECK:
cat package.json | grep '"volta"'
volta list
node -v

---

7. Record the pnpm Version for This Project

---

corepack prepare pnpm@9.12.0
pnpm pkg set packageManager="pnpm@9.12.0"

WHY:
Locks an exact pnpm version via Corepack for reproducible installs.

CHECK:
cat package.json | grep '"packageManager"'
corepack list | grep pnpm

---

8. Create Basic Directory Structure

---

mkdir -p src test

# Example Node file

cat > src/index.js <<'JS'
export function greet(name = 'world') {
return `Hello, ${name}!`;
}
if (import.meta.url === `file://${process.argv[1]}`) {
console.log(greet());
}
JS

# Example test file

cat > test/index.test.js <<'JS'
import { describe, it, expect } from 'vitest';
import { greet } from '../src/index.js';

describe('greet', () => {
it('greets default', () => {
expect(greet()).toBe('Hello, world!');
});
});
JS

WHY:
Provides a simple Node entry point and a Vitest test.

CHECK:
ls -R src test

---

9. Install Dev Tools (Lint, Format, Test)

---

corepack use pnpm@9.12.0
pnpm add -D eslint @eslint/js eslint-plugin-import \
 eslint-plugin-unused-imports prettier eslint-config-prettier \
 vitest @vitest/coverage-v8

WHY:
Adds all developer tools needed for linting, formatting,
and testing.

CHECK:
pnpm ls eslint prettier vitest

---

10. Create ESLint Flat Config (eslint.config.js)

---

cat > eslint.config.js <<'JS'
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
globals: { ...globals.node }
},
plugins: {
import: eslintPluginImport,
'unused-imports': eslintPluginUnusedImports
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
varsIgnorePattern: '^_'
}
],
'no-console': 'off',
'no-constant-condition': ['error', { checkLoops: false }]
}
}
];
JS

WHY:
Configures ESLint with Node globals and good import/cleanup rules.

CHECK:
pnpm exec eslint --version
pnpm lint

---

11. Create Prettier Configs

---

cat > .prettierrc.json <<'JSON'
{
"singleQuote": true,
"trailingComma": "all",
"semi": true,
"printWidth": 100
}
JSON

cat > .prettierignore <<'TXT'
node_modules
dist
coverage
pnpm-lock.yaml
.vscode/\*.log
TXT

WHY:
Defines Prettier formatting style and excludes unwanted files.

CHECK:
pnpm exec prettier --version
pnpm format:check

---

12. Add VS Code Workspace Settings

---

mkdir -p .vscode
cat > .vscode/settings.json <<'JSON'
{
"files.eol": "\n",
"editor.formatOnSave": true,
"editor.defaultFormatter": "esbenp.prettier-vscode",
"editor.codeActionsOnSave": {
"source.fixAll": "explicit",
"source.fixAll.eslint": "explicit"
},
"eslint.useFlatConfig": true
}
JSON

WHY:
Enables Prettier + ESLint integration with format/fix on save.

CHECK:
Open the folder in VS Code (WSL Remote), edit a file, save—
it should auto-format.

---

13. Create or Update .gitignore

---

cat > .gitignore <<'TXT'

# Dependencies and build

node_modules/
.pnpm-store/
dist/
coverage/

# Environment

.env
.env.\*

# Editor/OS junk

.DS_Store
Thumbs.db
.vscode/\*.log

# Backup files

_~
_.un~
.\*.un~

# (Optional Python/IDE sections can remain)

TXT

WHY:
Prevents node_modules, builds, env files, and temp files
from being committed to Git.

CHECK:
git add .gitignore
git check-ignore -v node_modules/

---

14. Update package.json Scripts

---

Add (or merge) these scripts into package.json:

"scripts": {
"start": "node src/index.js",
"test": "vitest run",
"test:ui": "vitest",
"coverage": "vitest run --coverage",
"lint": "eslint .",
"lint:fix": "eslint . --fix",
"format": "prettier . --write",
"format:check": "prettier . --check",
"preinstall": "node -e \"const ua=process.env.npm_config_user_agent||''; if(!ua.startsWith('pnpm/')){console.error('❌ Use pnpm, not '+ua); process.exit(1)}\""
}

WHY:
Defines scripts for testing, linting, formatting,
and a preinstall guard against using npm.

CHECK:
pnpm start
pnpm test
pnpm lint
pnpm format:check

---

15. Install and Lock Dependencies

---

pnpm install

WHY:
Generates or updates pnpm-lock.yaml for reproducible installs.

CHECK:
test -f pnpm-lock.yaml && echo "Lockfile OK"

---

16. Full Sanity Sweep

---

node -v
pnpm -v
pnpm lint
pnpm format:check
pnpm test
pnpm start

All should succeed.
If Prettier shows warnings, run:
pnpm format
then recheck.
