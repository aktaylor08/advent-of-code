from aoc.y2022.day06 import find_first

import pytest


@pytest.mark.parametrize(
    "input,result",
    [
        ["bvwbjplbgvbhsrlpgdmjqwftvncz", 5],
        ["nppdvjthqldpwncqszvftbrmjlhg", 6],
        ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10],
        ["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11],
    ],
)
def test_find_first(input, result):
    assert find_first(input) == result
