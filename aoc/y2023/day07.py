from curses.ascii import isdigit
import heapq
from enum import Enum
from collections import Counter
from aoc import get_input, sample_input


class HandType(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_KIND = 5
    FIVE_OF_KIND = 6


class Card(Enum):
    A = 12
    K = 11
    Q = 10
    J = 9
    T = 8
    a9 = 7
    a8 = 6
    a7 = 5
    a6 = 4
    a5 = 3
    a4 = 2
    a3 = 1
    a2 = 0


def to_card(cha: str) -> Card:
    if cha.isdigit():
        cha = "a" + str(cha)
    return Card[cha]


class Hand:
    def __init__(self, hand_str: str, wager: str):
        self.hand_str = hand_str
        self.hand = parse_type(hand_str)
        self.cards = [to_card(x) for x in hand_str]
        self.wager = int(wager)

    def __repr__(self):
        return f"{self.hand_str} -> {self.hand.name}: {self.wager}"

    def __cmp__(self, other):
        if self.hand.value > other.hand.value:
            return 1
        elif self.hand.value < other.hand.value:
            return -1
        else:
            for mine, theirs in zip(self.cards, other.cards):
                if mine.value > theirs.value:
                    return 1
                elif mine.value < theirs.value:
                    return -1
        return 0

    def __lt__(self, other):
        if self.__cmp__(other) == -1:
            return True
        else:
            return False


def parse_type(hand: str) -> HandType:
    handcount = Counter(hand)
    if len(handcount) == 1:
        return HandType.FIVE_OF_KIND
    elif len(handcount) == 2:
        if 3 in handcount.values():
            return HandType.FULL_HOUSE
        elif 1 in handcount.values():
            return HandType.FOUR_OF_KIND
    elif len(handcount) == 3:
        if 3 in handcount.values():
            return HandType.THREE_KIND
        else:
            return HandType.TWO_PAIR
    elif len(handcount) == 4:
        return HandType.ONE_PAIR
    return HandType.HIGH_CARD


def do_work():
    hand_heap = []
    for line in get_input(2023, 7).strip().split("\n"):
        a_hand = Hand(*line.strip().split())
        heapq.heappush(hand_heap, a_hand)
    rank = 1
    sum1 = 0
    while hand_heap:
        value = heapq.heappop(hand_heap)
        sum1 += rank * value.wager
        rank += 1
    print(sum1)


if __name__ == "__main__":
    do_work()
