from typing import List, Tuple

import pytest

from lc011_fill import Solution


@pytest.fixture
def sol():
    return Solution()


CASES: List[Tuple[List[int], int]] = [
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
    ([1] * 1000, 999),
    ([i for i in range(1000)], 249500),
]


@pytest.mark.parametrize("height, expected", CASES)
def test_max_area(sol: Solution, height: List[int], expected: int):
    assert sol.maxArea(height) == expected


@pytest.mark.parametrize("height, expected", CASES)
def test_max_area2(sol: Solution, height: List[int], expected: int):
    assert sol.maxArea2(height) == expected
