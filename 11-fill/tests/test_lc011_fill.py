from typing import List

import pytest
from lc011_fill import Solution


@pytest.fixture  # .fixture is used to set up a common test object
def sol():
    return Solution()


@pytest.mark.parametrize(  # .parametrize is used to run the same test with different inputs
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([1, 2, 4, 3], 4),
        ([1, 3, 2, 5, 25, 24, 5], 24),
        ([2, 3, 4, 5, 18, 17, 6], 17),
        ([1, 2, 1], 2),
        ([1, 1], 1),
        ([1], 0),
        ([], 0),
        ([1, 2], 1),
        ([2, 1], 1),
        ([1, 3], 1),
        ([3, 1], 1),
        ([1] * 1000, 999),  # long array with single height
    ],
)
def test_max_area(sol: Solution, height: List[int], expected: int):
    assert sol.maxArea(height) == expected
