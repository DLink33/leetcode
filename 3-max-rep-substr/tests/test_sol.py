import pytest

from sol import Solution

CASES = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    (" ", 1),
    ("au", 2),
    ("dvdf", 3),
]


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize("s, expected", CASES)
def test_lengthOfLongestSubstring(s: str, expected: int):
    sol = Solution()
    print(f'\nInput:\t\t"{s}"')
    print(f"Result:\t\t{sol.lengthOfLongestSubstring(s)}")
    print(f"Expected:\t{expected}")
    assert sol.lengthOfLongestSubstring(s) == expected
