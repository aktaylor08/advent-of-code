import heapq
from enum import Enum
from collections import Counter

from aoc import get_input


class HandType(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_KIND = 5
    FIVE_OF_KIND = 6


def parse_type(hand: str, wild_allowed=False) -> HandType:
    handcount = Counter(hand)
    wild_count = 0
    if wild_allowed and "J" in hand:
        wild_count = handcount["J"]
    if len(handcount) == 1:
        # FIve of a kind only one card type
        return HandType.FIVE_OF_KIND
    elif len(handcount) == 2:
        # Two card types, either full house with 3/2 split or 4/1 four of kind
        # Any wilds make this a  five of kind right away
        if wild_count > 0:
            return HandType.FIVE_OF_KIND
        elif 3 in handcount.values():
            return HandType.FULL_HOUSE
        elif 1 in handcount.values():
            return HandType.FOUR_OF_KIND
    elif len(handcount) == 3:
        # 3 values mens a Three of a kind or two pairj
        if 3 in handcount.values():
            # With three of a kind wild can only be 1  or 3 so it goes to four of a kind
            if wild_count > 0:
                return HandType.FOUR_OF_KIND
            else:
                return HandType.THREE_KIND
        else:
            if wild_count == 2:
                return HandType.FOUR_OF_KIND
            elif wild_count == 1:
                return HandType.FULL_HOUSE
            # Wild cn either be 2 or 1 so it goes to three of kind?
            return HandType.TWO_PAIR
    elif len(handcount) == 4:
        if wild_count > 0:
            return HandType.THREE_KIND
        else:
            return HandType.ONE_PAIR
    if wild_count > 0:
        return HandType.ONE_PAIR
    return HandType.HIGH_CARD


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
    WILD = -1


def to_card(cha: str, wild_allowed: bool) -> Card:
    if cha.isdigit():
        cha = "a" + str(cha)
    if cha == "J" and wild_allowed:
        cha = "WILD"
    return Card[cha]


class Hand:
    def __init__(self, hand_str: str, wager: str, wild_allowed=False):
        self.hand_str = hand_str
        self.hand = parse_type(hand_str, wild_allowed)
        self.cards = [to_card(x, wild_allowed) for x in hand_str]
        self.wild_allowed = wild_allowed
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


def do_work():
    hand_heap = []
    hand_wild_heap = []
    for line in get_input(2023, 7).strip().split("\n"):
        a_hand = Hand(*line.strip().split(), wild_allowed=False)
        wild_hand = Hand(*line.strip().split(), wild_allowed=True)
        heapq.heappush(hand_heap, a_hand)
        heapq.heappush(hand_wild_heap, wild_hand)
    rank = 1
    sum1 = 0
    sum2 = 0
    while hand_heap:
        value = heapq.heappop(hand_heap)
        value_wild = heapq.heappop(hand_wild_heap)
        sum1 += rank * value.wager
        sum2 += rank * value_wild.wager
        rank += 1
    print(sum1)
    print(sum2)


if __name__ == "__main__":
    do_work()
