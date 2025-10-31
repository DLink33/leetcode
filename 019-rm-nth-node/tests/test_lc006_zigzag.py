# tests/test_lc006_zigzag.py
import pytest
from lc006_zigzag import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize(
    "s,numRows,expected",
    [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),  # sample
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),  # common second sample
        ("ABCD", 2, "ACBD"),  # small check
        ("A", 1, "A"),  # numRows=1
        ("AB", 5, "AB"),  # numRows >= len(s)
        ("", 3, ""),  # empty
        ("ABCDE", 4, "ABCED"),  # short string with more rows
        ("ABCDEFGHIJKLMN", 3, "AEIMBDFHJLNCGK"),
        ("A" * 1000, 10, "A" * 1000),  # long string with single character
    ],
)
def test_convert(sol: Solution, s: str, numRows: int, expected: str):
    assert sol.convert(s, numRows) == expected
