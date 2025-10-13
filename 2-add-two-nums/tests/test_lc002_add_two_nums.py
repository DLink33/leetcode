import pytest

from lc002_add_two_nums import LinkedIntList, ListNode, Solution

CASES = [
    (LinkedIntList(342).head, LinkedIntList(465).head, 807),
    (LinkedIntList(0).head, LinkedIntList(0).head, 0),
]


@pytest.fixture
def sol() -> "Solution":
    return Solution()


@pytest.mark.parametrize("l1,l2,expected", CASES)
def test_addTwoNumbers(sol: Solution, l1: ListNode, l2: ListNode, expected: int):
    result = sol.addTwoNumbers(l1, l2)
    print(result)
    assert (result.toInt() if result is not None else None) == expected
