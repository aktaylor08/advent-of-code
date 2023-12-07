from ctypes.wintypes import HANDLE
from aoc.y2023.day07 import HandType, parse_type, Hand

import pytest


@pytest.mark.parametrize(
    "hand,result",
    [
        ["AAAAA", HandType.FIVE_OF_KIND],
        ["AA8AA", HandType.FOUR_OF_KIND],
        ["23332", HandType.FULL_HOUSE],
        ["TTT98", HandType.THREE_KIND],
        ["23432", HandType.TWO_PAIR],
        ["A23A4", HandType.ONE_PAIR],
        ["23456", HandType.HIGH_CARD],
    ],
)
def test_parse_type(hand, result):
    assert parse_type(hand).value == result.value


@pytest.mark.parametrize(
    "hand1,hand2,whowon",
    [
        ["AAAAA", "22345", 1],
        ["22345", "AAAAA", -1],
        ["88888", "AAAAA", -1],
        ["88288", "AA2AA", -1],
        ["28888", "AA2AA", -1],
        ["AAA88", "AAA77", 1],
        ["33332", "2AAAA", 1],
        ["77888", "77788", 1],
        ["KK677", "KTJJT", 1],
    ],
)
def test_comparision(hand1, hand2, whowon):
    h1 = Hand(hand1, "0")
    h2 = Hand(hand2, "0")
    print(h1, h2)
    assert h1.__cmp__(h2) == whowon


@pytest.mark.parametrize(
    "hand,result",
    [
        ["JJJJJ", HandType.FIVE_OF_KIND],
        ["AAAAJ", HandType.FIVE_OF_KIND],
        ["JJJJA", HandType.FIVE_OF_KIND],
        ["AAAJJ", HandType.FIVE_OF_KIND],
        ["JJJAA", HandType.FIVE_OF_KIND],
        ["AAAJ1", HandType.FOUR_OF_KIND],
        ["AAA1J", HandType.FOUR_OF_KIND],
        ["JJJAK", HandType.FOUR_OF_KIND],
        ["KTJJT", HandType.FOUR_OF_KIND],
        ["AAKKJ", HandType.FULL_HOUSE],
        ["JJKK2", HandType.FOUR_OF_KIND],
        ["JJ234", HandType.THREE_KIND],
        ["22J34", HandType.THREE_KIND],
        ["26J34", HandType.ONE_PAIR],
    ],
)
def test_wild(hand, result):
    assert parse_type(hand, wild_allowed=True).value == result.value
