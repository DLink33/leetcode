from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (6, 13),
    (7, 21),
    (8, 34),
    (9, 55),
    (10, 89),
    (20, 10946),
    (30, 1346269),
    (35, 14930352),
    (40, 165580141),
    (45, 1836311903),
    (50, 20365011074),
    (60, 2504730781961),
    (70, 308061521170129)
]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.climbStairsIterative(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.climbStairsIterative(*case_input) == expected
    else:
        assert sol.climbStairsIterative(case_input) == expected # pyright: ignore[reportArgumentType]
