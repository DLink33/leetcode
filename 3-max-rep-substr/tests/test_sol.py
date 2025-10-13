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
    rslt = sol.lengthOfLongestSubstring(s)
    print(f'\nInput:\t\t"{s}"')
    print(f"Result:\t\t{rslt}")
    print(f"Expected:\t{expected}")
    assert rslt == expected


@pytest.mark.parametrize("s, expected", CASES)
def test_lengthOfLongestSubstring2(s: str, expected: int):
    sol = Solution()
    rslt = sol.lengthOfLongestSubstring2(s)
    print(f'\nInput:\t\t"{s}"')
    print(f"Result:\t\t{rslt}")
    print(f"Expected:\t{expected}")
    assert rslt == expected
