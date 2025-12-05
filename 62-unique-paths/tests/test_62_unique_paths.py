from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    ((5, 3), 15),
    ((3, 2), 3),
    ((7, 3), 28),
    ((3, 3), 6),
    ((10, 10), 48620),
    ((1, 1), 1),
    ((2, 2), 2),
    ((3, 7), 28),
    ((4, 4), 20),
    ((5, 5), 70),
    ((1, 10), 1),
    ((10, 1), 1),
    ((2, 10), 10),
    ((10, 2), 10),
    ((20, 20), 35345263800),
    ((100, 100), 22750883079422934966181954039568885395604168260154104734000)
]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.uniquePaths(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.uniquePaths(*case_input) == expected
        assert sol.uniquePaths_choose(*case_input) == expected
    else:
        assert sol.uniquePaths(case_input) == expected  # pyright: ignore[reportCallIssue]
