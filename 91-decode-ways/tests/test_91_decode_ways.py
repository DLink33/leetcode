from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    ("12", 2),
    ("226", 3),
    ("0", 0),
    ("06", 0),
    ("10", 1),
    ("27", 1),
    ("11106", 2),
    ("111111111111111111111111111111111111111111111", 1836311903),
    ("2611055971756562", 4),
    ("10011", 0),
]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.numDecodings(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.numDecodings(*case_input) == expected
    else:
        assert sol.numDecodings(case_input) == expected  # pyright: ignore[reportArgumentType]
