============================================================
JavaScript / Node Setup (WSL - RHEL 9)
Simplified npm-only workflow using Volta + ESLint + Prettier + Vitest
============================================================

STACK:
  Volta (Node toolchain manager)
  Node LTS (with npm)
  ESLint (Flat Config)
  Prettier
  Vitest
  WSL (RHEL9)
------------------------------------------------------------


============================================================
PART 1 — GLOBAL SETUP (Run once per system)
============================================================

1. BASE OS TOOLS
------------------------------------------------------------
sudo dnf -y upgrade
sudo dnf -y install git curl ca-certificates
sudo dnf -y groupinstall "Development Tools"
sudo dnf -y install python3 gcc-c++ make openssl-devel

# Verify
git --version
curl --version
python3 --version
gcc --version


2. INSTALL VOLTA (Node toolchain manager)
------------------------------------------------------------
curl https://get.volta.sh | bash
exec $SHELL
volta --version

# Volta automatically manages Node/npm binaries in your PATH.


3. INSTALL NODE (LTS) AND VERIFY
------------------------------------------------------------
volta install node@lts
node -v

# This installs and globally pins a default Node version for your user account.
# npm comes bundled with Node.


============================================================
PART 2 — PER-PROJECT SETUP (Repeat for each new repo)
============================================================

4. CREATE PROJECT DIRECTORY
------------------------------------------------------------
mkdir -p ~/projects/my-node-app && cd ~/projects/my-node-app
npm init -y

# Edit package.json:
# Add or verify the following keys:

"type": "module",
"private": true,
"scripts": {
  "start": "node src/index.js"
}


5. PIN NODE VERSION PER PROJECT
------------------------------------------------------------
volta pin node@20
cat package.json | grep '"volta"' || echo "No volta block found"
node -v

# This ensures anyone cloning the project uses the same Node version.


6. PROJECT STRUCTURE
------------------------------------------------------------
mkdir -p src test

cat > src/index.js <<'JS'
export function greet(name = 'world') {
  return `Hello, ${name}!`;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(greet());
}
JS

cat > test/index.test.js <<'JS'
import { describe, it, expect } from 'vitest';
import { greet } from '../src/index.js';

describe('greet', () => {
  it('greets default', () => {
    expect(greet()).toBe('Hello, world!');
  });
});
JS


7. INSTALL DEV DEPENDENCIES
------------------------------------------------------------
npm i -D eslint @eslint/js eslint-plugin-import eslint-plugin-unused-imports \
  prettier vitest @vitest/coverage-v8


8. ESLINT FLAT CONFIG (eslint.config.js)
------------------------------------------------------------
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


9. PRETTIER CONFIG
------------------------------------------------------------
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
.vscode/*.log
TXT


10. PACKAGE SCRIPTS (merge into package.json)
------------------------------------------------------------
"scripts": {
  "start": "node src/index.js",
  "test": "vitest run",
  "test:ui": "vitest",
  "coverage": "vitest run --coverage",
  "lint": "eslint .",
  "lint:fix": "eslint . --fix",
  "format": "prettier . --write",
  "format:check": "prettier . --check"
}


11. VS CODE SETTINGS (WSL Remote)
------------------------------------------------------------
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

# Open the project via the "Remote - WSL" extension in VS Code.


12. GITIGNORE
------------------------------------------------------------
cat > .gitignore <<'TXT'
# Dependencies and build
node_modules/
dist/
coverage/

# Environment
.env
.env.*

# Editor/OS junk
.DS_Store
Thumbs.db
.vscode/*.log
TXT


13. VERIFY EVERYTHING
------------------------------------------------------------
npm run lint
npm run format:check
npm test
npm start

EXPECTED OUTPUT:
  ✓ Lint passes (or fix with npm run lint:fix)
  ✓ Prettier check clean
  ✓ Vitest passes tests
  ✓ "Hello, world!" printed on npm start


============================================================
OPTIONAL — ADD TYPESCRIPT (Per Project)
============================================================
npm i -D typescript @types/node tsx
npx tsc --init --rootDir src --outDir dist \
  --esModuleInterop --resolveJsonModule \
  --module node16 --moduleResolution node16 --target ES2022

# Add or replace scripts:
"scripts": {
  "dev": "tsx src/index.ts",
  "build": "tsc -p tsconfig.json",
  "start": "node dist/index.js",
  "test": "vitest run",
  "test:ui": "vitest",
  "coverage": "vitest run --coverage",
  "lint": "eslint .",
  "lint:fix": "eslint . --fix",
  "format": "prettier . --write",
  "format:check": "prettier . --check"
}


============================================================
PART 3 — WORKING WITH AN EXISTING REPO (Clone & Run)
============================================================

OVERVIEW
------------------------------------------------------------
Use this when you are NOT creating a new project, but cloning an existing one
that follows this guide (npm-only, Volta-pinned Node, ESLint/Prettier/Vitest).

PREREQS (run once per system):
  - Part 1 (GLOBAL SETUP) completed:
      * Volta installed and in PATH
      * At least one Node LTS installed via Volta
  - VS Code Remote – WSL extension installed (optional but recommended)


A) CLONE THE REPOSITORY
------------------------------------------------------------
cd ~/projects
git clone <REPO_URL> my-node-app
cd my-node-app

# Verify package.json exists and (optionally) has a "volta" block:
cat package.json | sed -n '1,120p' | grep -E '"name"|"type"|"volta"|^  "scripts"'


B) ENSURE CORRECT NODE VERSION (Volta)
------------------------------------------------------------
# If the repo has "volta": { "node": "20.x" } in package.json,
# Volta will automatically use (or fetch) that Node when you run node/npm.

# You can also proactively fetch the pinned Node version:
volta install node@20 || true

# Confirm:
which node
node -v
volta list


C) INSTALL DEPENDENCIES
------------------------------------------------------------
# Prefer 'npm ci' if package-lock.json is present (clean, reproducible install).
# Otherwise fallback to 'npm install'.

if [ -f package-lock.json ]; then
  npm ci
else
  npm install
fi

# Tip: if native modules fail to build, ensure build tools are installed:
#   sudo dnf -y groupinstall "Development Tools"
#   sudo dnf -y install python3 gcc-c++ make openssl-devel


D) RUN DEV CHECKS & TESTS
------------------------------------------------------------
npm run lint
npm run format:check
npm test

# Optional interactive test UI:
# npm run test:ui


E) START THE APP (if applicable)
------------------------------------------------------------
# For libraries, this may not apply. For apps/CLIs:
npm start


F) OPEN IN VS CODE (WSL)
------------------------------------------------------------
# From the repo directory:
code .

# VS Code will honor the pinned Node via Volta shims.
# Save-on-format and ESLint fixes depend on the project's .vscode/settings.json
# and having the Prettier + ESLint extensions installed.


QUICK START (one-liner-ish)
------------------------------------------------------------
# Assumes Part 1 (Global) is done and repo has package-lock.json
cd ~/projects && git clone <REPO_URL> my-node-app && cd my-node-app \
  && volta install node@20 || true \
  && ( [ -f package-lock.json ] && npm ci || npm install ) \
  && npm run lint && npm test && npm start


COMMON TROUBLESHOOTING
------------------------------------------------------------
1) "node: command not found" or wrong Node version
   - Ensure Volta is on PATH:
     echo $PATH | tr ':' '\n' | grep volta
   - Re-source your shell or open a new terminal:
     exec $SHELL
   - Verify Volta + Node:
     volta --version && node -v

2) Native module build errors
   - Ensure build tools installed:
     sudo dnf -y groupinstall "Development Tools"
     sudo dnf -y install python3 gcc-c++ make openssl-devel

3) ESLint/Prettier not formatting on save in VS Code
   - Check .vscode/settings.json in the repo
   - Install "ESLint" and "Prettier - Code formatter" extensions
   - Confirm "eslint.useFlatConfig": true

4) Dependency mismatch / weird behavior
   - Clean and reinstall:
     rm -rf node_modules
     npm ci          # or npm install if no package-lock.json
   - Make sure you're on the right Node:
     node -v; cat package.json | grep -A3 '"volta"'
------------------------------------------------------------


============================================================
SUMMARY
============================================================
GLOBAL (Run once per WSL instance):
  ✔ Install base build tools (git, curl, compilers)
  ✔ Install Volta
  ✔ Install global Node LTS

PER-PROJECT (Repeat for each repo):
  ✔ npm init project (or clone an existing repo)
  ✔ volta pin Node version (or rely on repo's volta block)
  ✔ create src/ and test/ (new project only)
  ✔ install dev dependencies (or npm ci after clone)
  ✔ configure ESLint + Prettier + Vitest (new project only)
  ✔ set up VS Code settings and gitignore (new project only)
  ✔ verify lint, format, and tests
  ✔ (optional) add TypeScript support

Everything uses npm only — no pnpm, no Corepack.
Volta ensures Node and npm versions are consistent across machines.
------------------------------------------------------------
