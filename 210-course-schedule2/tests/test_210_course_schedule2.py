from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    # Basic example with branching dependencies:
    # 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3
    # One valid deterministic order from this implementation: [0, 1, 2, 3]
    (((4, [[1, 0], [2, 0], [3, 1], [3, 2]])), [0, 1, 2, 3]),

    # No prerequisites: any order is valid; this implementation yields [0, 1, 2]
    (((3, [])), [0, 1, 2]),

    # Simple 2-cycle: 0 <-> 1, impossible to finish
    (((2, [[0, 1], [1, 0]])), []),

    # Simple chain: 0 -> 1 -> 2, only valid order is [0, 1, 2]
    (((3, [[1, 0], [2, 1]])), [0, 1, 2]),

    # Longer cycle: 0 -> 1 -> 2 -> 0, impossible to finish
    (((3, [[1, 0], [2, 1], [0, 2]])), []),

    # Disconnected graph: 0 -> 1, and 2 has no prerequisites.
    # With this implementation, queue starts with [0, 2], so order is [0, 2, 1].
    (((3, [[1, 0]])), [0, 2, 1]),

    # Self-loop: 0 -> 0, impossible to finish (caught by your early self-loop check)
    (((1, [[0, 0]])), []),

    # Single course, no prerequisites
    (((1, [])), [0]),
]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.findOrder(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.findOrder(*case_input) == expected
    else:
        assert sol.findOrder(case_input) == expected
