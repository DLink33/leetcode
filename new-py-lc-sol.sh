#!/usr/bin/env bash
set -euo pipefail

log() { echo "==> $*"; }

# Prompt for the problem number/name
read -rp "Enter the problem number/name: " problem_name

# Ensure python3.11 exists
if ! command -v python3.11 >/dev/null 2>&1; then
  echo "ERROR: python3.11 not found on PATH. Install Python 3.11 and re-run."
  exit 1
fi

log "Scaffolding project structure for '$problem_name'..."
mkdir -p "$problem_name/src" "$problem_name/tests"
: > "$problem_name/src/__init__.py"

log "Writing pyproject.toml..."
cat <<EOL > "$problem_name/pyproject.toml"

pythonpath = ["src", "/home/vulpski/projects/fundamentals/data-structures/python/"]

[tool.poetry]
name = "$problem_name"
version = "0.1.0"
package-mode = false
description = "A solution to LeetCode $problem_name"
authors = ["David Linkowski <david.linkowski@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.11"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4"
pytest-cov = "^4.0"
black = "^24.3"
# use a broad isort constraint to avoid strict resolution failures across indexes
isort = "^5.0"
flake8 = "^6.0"
mypy = "^1.7"
pre-commit = "^3.4"

[tool.black]
line-length = 88

[tool.isort]
profile = "black"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.pytest.ini_options]
pythonpath = ["src", "/home/vulpski/projects/fundamentals/data-structures/python/"]

EOL

# Ensure Poetry is available
if ! command -v poetry >/dev/null 2>&1; then
  log "Poetry not found — installing Poetry to user space (~/.local/bin)..."
  curl -sSL https://install.python-poetry.org | python3 -
  export PATH="$HOME/.local/bin:$PATH"
  hash -r
  log "Poetry installed at: $(command -v poetry)"
else
  log "Poetry found at: $(command -v poetry)"
fi

# --- Create and activate a Python 3.11 venv under the project ---
proj_dir="$problem_name"
venv_dir="$proj_dir/.venv"

log "Creating Python 3.11 virtual environment at '$venv_dir'..."
python3.11 -m venv "$venv_dir"

log "Activating virtual environment..."
# shellcheck source=/dev/null
source "$venv_dir/bin/activate"

log "Upgrading pip/setuptools/wheel inside the venv..."
python -m pip install --upgrade pip setuptools wheel

log "Configuring Poetry to use the active venv (no Poetry-managed venvs) for this project..."
pushd "$proj_dir" >/dev/null
poetry config virtualenvs.create false --local

log "Installing project dependencies into .venv via Poetry..."
poetry install --no-interaction
popd >/dev/null

log "Creating src/Solution.py..."
problem_name_without_numbers=${problem_name//[0-9]/}
cat > "$problem_name/src/Solution.py" <<EOL
class Solution:
    def ${problem_name_without_numbers//-/_}(self, *args):
        # Implement your solution here
        raise NotImplementedError

def main():
    raise NotImplementedError

if __name__ == '__main__':
    main()
  
EOL

log "Creating tests/test_<name>.py..."
cat <<'EOL' > "$problem_name/tests/test_template.py"
import pytest
from src.Solution import Solution

TEST_CASES = [
    # Add your test cases here. Common patterns:
    # (input_value, expected_value)
    # ((arg1, arg2, ...), expected_value)
    # ({"args": (a1, ...), "kwargs": {"k": v}}, expected_value)
]

@pytest.mark.parametrize("input, expected", TEST_CASES)
def test_solution(input, expected):
    sol: Solution = Solution()
    if isinstance(input, dict) and ("args" in input or "kwargs" in input):
        args = input.get("args", ())
        kwargs = input.get("kwargs", {})
        assert sol.solve(*args, **kwargs) == expected
    elif isinstance(input, tuple):
        assert sol.solve(*input) == expected
    else:
        assert sol.solve(input) == expected
EOL

mv "$problem_name/tests/test_template.py" "$problem_name/tests/test_${problem_name//-/_}.py"

log "Writing README.md..."
cat > "$problem_name/README.md" <<EOL
# $problem_name Solution
-----------

This directory was scaffolded by \`new-lc-sol.sh\`.

Environment
-----------
A Python 3.11 virtual environment is created at \`.venv/\` in this project.
Poetry is configured to install dependencies **into this venv** (no separate Poetry venv).

Quick start
-----------
bash 
cd $problem_name

# activate the venv
. .venv/bin/activate

# run tests
pytest -q

# or run via Poetry (still uses the active .venv)
poetry run pytest -q
EOL

echo "Finished creating Python3.11 solution scaffold for $problem_name!"