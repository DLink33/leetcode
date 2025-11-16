from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    # 1) No prerequisites at all → always can finish
    ((2, []), True),

    # 2) Simple acyclic chain: 0 -> 1
    ((2, [[1, 0]]), True),

    # 3) Simple 2-node cycle: 0 <-> 1
    ((2, [[1, 0], [0, 1]]), False),

    # 4) Longer acyclic chain: 0 -> 1 -> 2 -> 3
    ((4, [[1, 0], [2, 1], [3, 2]]), True),

    # 5) One course depending on two different prereqs: 1 -> 0, 2 -> 0
    ((3, [[0, 1], [0, 2]]), True),

    # 6) 3-node cycle: 0 -> 1 -> 2 -> 0
    ((3, [[1, 0], [2, 1], [0, 2]]), False),

    # 7) Bigger DAG, no cycles
    # 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3, 3 -> 4
    ((5, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]), True),

    # 8) Disconnected graph where one component has a cycle
    # component1: 0 <-> 1 (cycle), component2: 2 -> 3
    ((4, [[1, 0], [0, 1], [3, 2]]), False),

    # 9) Single course, no prereqs
    ((1, []), True),

    # 10) Courses exist but all are in a single big cycle
    # 0 -> 1 -> 2 -> 3 -> 0
    ((4, [[1, 0], [2, 1], [3, 2], [0, 3]]), False),

    ((20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]), False)
    ]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.canFinish(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.canFinish(*case_input) == expected
    else:
        assert sol.canFinish(case_input) == expected
