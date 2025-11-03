import pytest

from Solution import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize(
    "temps,expected",
    [
        ([123], [123]),
    ],
)
def test_convert(sol: Solution, temperatures: list[int], expected: list[int]):
    assert sol.dailyTemperatures(temperatures) == expected
