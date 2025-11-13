from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
TestCase = tuple[Any, Any]

TEST_CASES: list[TestCase] = [
    (([[1,2], [1,3], [2,3]]),           [2,3]),
    (([[1,2],[2,3],[3,4],[1,4],[1,5]]), [1,4]),
    ([[1,5],[3,4],[3,5],[4,5],[2,4]],   [4,5]),
    (([[1,2],[2,3],[3,1]]),             [3,1]),
    (([[1,4],[3,4],[1,3],[1,2],[4,5]]), [1,3]),
    ([[1,2],[2,3],[4,5],[3,4],[1,5]],   [1,5]),
    ([[2,3],[1,2],[3,4],[1,4]],         [1,4]),

]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_solution(case_input: Any, expected: Any) -> None:
    sol = Solution()
    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        assert sol.findRedundantConnection(*args, **kwargs) == expected
    elif isinstance(case_input, tuple):
        assert sol.findRedundantConnection(*case_input) == expected
    else:
        assert sol.findRedundantConnection(case_input) == expected
