# tests/test_lc006_zigzag.py
import pytest

from Solution import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize(
    "s,expected",
    [
        ("", True),  # empty is valid
        ("()", True),
        ("()[]{}", True),
        ("(]", False),  # mismatched types
        ("([)]", False),  # wrong order
        ("{[]}", True),
        ("{[()]}", True),
        (")(", False),  # close before open
        ("(", False),  # single open
        (")", False),  # single close
        ("[]", True),
        ("[", False),
        ("]", False),
        ("{}", True),
        ("{", False),
        ("}", False),
        ("[[[]]]", True),  # nested same-type
        ("[[]", False),  # leftover open
        ("[]]", False),  # extra close
        ("{[]})", False),  # extra close after valid prefix
        ("{([])}[]({})", True),  # mixed valid groups
        ("{([])}[]({})(", False),  # valid then stray open
        ("[({})]()", True),  # classic nested then pair
        ("[({})](]", False),  # almost valid, last char wrong
        ("(([]){})", True),
        ("(([]){})(", False),
        ("([{}])", True),
        ("([{}{}])", True),
        ("([{])", False),
        # Long / stress shapes
        ("(" * 10 + ")" * 10, True),  # deep nesting all same type
        ("(" * 1000 + ")" * 1000, True),  # very long balanced
        ("(" * 1000 + ")", False),  # many opens, not enough closes
        ("()" * 5000, True),  # many small pairs
        # Tricky alternations
        ("([]){}", True),
        ("([)()]", False),  # interleaved wrong
        ("[(){}([])]", True),
        ("[(){}([)] ]", False),  # spacing not in LC input; remove space if needed
    ],
)
def test_convert(sol: Solution, s: str, expected: str):
    assert sol.isValid(s) == expected
