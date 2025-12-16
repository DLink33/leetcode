from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    (([2, 3, 1, 1, 4],), 2),
    (([2, 3, 0, 1, 4],), 2),
    (([0],), 0),
    (([1, 2, 3],), 2),
    (([2, 1],), 1),
    (([1, 1, 1, 1],), 3),
    (([3, 2, 1, 0, 4],), 2),
    (([2, 5, 0, 0],), 2),
    (([1, 2, 1, 1, 1],), 3),
    (([4, 1, 1, 3, 1, 1, 1],), 2),
    (([1, 4, 3, 7, 1, 2, 6, 7, 6, 10],), 3),
]

@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    assert sol.jump_greedy(*case_input) == expected

