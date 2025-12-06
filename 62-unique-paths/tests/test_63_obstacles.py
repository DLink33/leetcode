from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    (
        ([[0,0,0],[0,1,0],[0,0,0]],),
        2
    ),
    (
        ([[0,1],[0,0]],),
        1
    ),
    (
        ([[1]],),
        0
    ),
    (
        ([[0]],),
        1
    ),
    (
        ([[0,0],[1,1],[0,0]],),
        0
    ),
    (
        ([[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,0]],),
        4
    ),
]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, tuple):
        assert sol.uniquePathsWithObstacles(*case_input) == expected
    else:
        raise TypeError
