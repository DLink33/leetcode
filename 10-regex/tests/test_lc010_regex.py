# tests/test_lc006_zigzag.py
import pytest

from lc010_regex import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize(
    "s,p,expected",
    [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("", ".*", True),
        ("", "", True),
        ("a", "", False),
        ("", "a*", True),
        ("ab", ".*c", False),
        ("aaa", "ab*a*c*a", True),
        ("a", "ab*", True),
        ("a", ".*..a*", False),
        ("bbbba", ".*a*a", True),
        ("a", ".*..a*", False),
    ],
)
def test_isMatch(sol: Solution, s: str, p: str, expected: str):
    assert sol.isMatch(s, p) == expected
