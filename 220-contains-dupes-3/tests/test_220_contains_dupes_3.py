from typing import Any

import pytest
from Solution import Solution

# A test case is: (input_payload, expected_output)
# input_payload can be:
#   - (nums, indexDiff, valueDiff)
#   - {"args": (nums, indexDiff, valueDiff), "kwargs": {...}} if you ever need kwargs
TestCase = tuple[Any, bool]

TEST_CASES: list[TestCase] = [
    # Basic true case: exact duplicate within indexDiff, valueDiff = 0
    (([1, 2, 3, 1], 3, 0), True),

    # Basic false case: same values but index difference too large
    (([1, 2, 3, 1], 2, 0), False),

    # Example with small indexDiff and non-zero valueDiff
    # nums[2] = 1, nums[3] = 1 -> diff 0 <= 2 and |2 - 3| = 1 <= 1
    (([1, 0, 1, 1], 1, 2), True),

    # Classic false example: values close in value, but not close enough in index
    (([1, 5, 9, 1, 5, 9], 2, 3), False),

    # Edge: indexDiff = 0 means you can't have i != j with |i - j| <= 0
    (([1, 2, 3], 0, 1), False),

    # Edge: negative valueDiff should logically give False (no |diff| <= negative)
    (([1, 1], 1, -1), False),

    # Negative numbers with valid pair
    # nums[1] = -3, nums[3] = -2 -> diff 1 <= 1, |1 - 3| = 2 <= 2
    (([-1, -3, -6, -2], 2, 1), True),

    # Large indexDiff relative to array size (effectively no index restriction)
    (([1, 2, 1], 10, 0), True),

    # No valid pairs: values just outside the allowed valueDiff
    (([1, 4, 7, 10], 3, 1), False),

    # Single element: cannot form a pair
    (([42], 5, 100), False),
]


@pytest.mark.parametrize(("case_input", "expected"), TEST_CASES)
def test_contains_nearby_almost_duplicate(case_input: Any, expected: bool) -> None:
    sol = Solution()

    if isinstance(case_input, dict) and ("args" in case_input or "kwargs" in case_input):
        args = case_input.get("args", ())
        kwargs = case_input.get("kwargs", {})
        result = sol.containsNearbyAlmostDuplicate(*args, **kwargs)
    elif isinstance(case_input, tuple):
        result = sol.containsNearbyAlmostDuplicate(*case_input)
    else:
        # Fallback if you ever decide to pass just nums and hard-code the rest
        result = sol.containsNearbyAlmostDuplicate(case_input)

    assert result == expected
