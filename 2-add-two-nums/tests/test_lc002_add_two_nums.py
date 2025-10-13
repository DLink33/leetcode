import pytest

from lc002_add_two_nums import LinkedIntList, ListNode, Solution

CASES = [
    (LinkedIntList(342).head, LinkedIntList(465).head, 807),
    (LinkedIntList(0).head, LinkedIntList(0).head, 0),
    (LinkedIntList(9999999).head, LinkedIntList(9999).head, 10009998),
    (LinkedIntList(1).head, LinkedIntList(9999).head, 10000),
    (LinkedIntList(9999).head, LinkedIntList(1).head, 10000),
    (LinkedIntList(1).head, LinkedIntList(999).head, 1000),
    (LinkedIntList(999).head, LinkedIntList(1).head, 1000),
    (LinkedIntList(123456789).head, LinkedIntList(987654321).head, 1111111110),
    (
        LinkedIntList(1000000000000000000000000000001).head,
        LinkedIntList(564).head,
        1000000000000000000000000000565,
    ),
    (LinkedIntList(0).head, LinkedIntList(123456789).head, 123456789),  # one empty
    (LinkedIntList(123456789).head, LinkedIntList(0).head, 123456789),  # one empty
    (
        LinkedIntList(1).head,
        LinkedIntList(9999999999).head,
        10000000000,
    ),  # different lengths
    (
        LinkedIntList(9999999999).head,
        LinkedIntList(1).head,
        10000000000,
    ),  # different lengths
    (LinkedIntList(123).head, LinkedIntList(4567).head, 4690),  # different lengths
]


@pytest.fixture
def sol() -> "Solution":
    return Solution()


@pytest.mark.parametrize("l1,l2,expected", CASES)
def test_addTwoNumbers(sol: Solution, l1: ListNode, l2: ListNode, expected: int):
    result = sol.addTwoNumbers(l1, l2)
    print(f"\nInput 1:{l1}")
    print(f"Input 2:{l2}")
    print(f"Linked List Result:{result}")
    print(f"Result as int:\t{result.toInt() if result is not None else None}")
    print(f"Expected:\t{expected}")
    assert (result.toInt() if result is not None else None) == expected
