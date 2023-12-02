import pytest
from aoc.y2022.day03 import split_line, find_common, find_priority


@pytest.mark.parametrize(
    "line,split",
    [
        ["vJrwpWtwJgWrhcsFMMfFFhFp", ("vJrwpWtwJgWr", "hcsFMMfFFhFp")],
        ["jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL")],
        ["PmmdzqPrVvPwwTWBwg", ("PmmdzqPrV", "vPwwTWBwg")],
        ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", ("wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn")],
        ["ttgJtRGJQctTZtZT", ("ttgJtRGJ", "QctTZtZT")],
        ["CrZsJsPPZsGzwwsLwLmpwMDw", ("CrZsJsPPZsGz", "wwsLwLmpwMDw")],
    ],
)
def test_score(line, split):
    print(line)
    assert split_line(line) == split


@pytest.mark.parametrize(
    "parts,result",
    [
        [("vJrwpWtwJgWr", "hcsFMMfFFhFp"), "p"],
        [("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"), "L"],
        [("PmmdzqPrV", "vPwwTWBwg"), "P"],
        [("wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn"), "v"],
        [("ttgJtRGJ", "QctTZtZT"), "t"],
        [("CrZsJsPPZsGz", "wwsLwLmpwMDw"), "s"],
    ],
)
def test_same(parts, result):
    assert find_common(parts) == result


@pytest.mark.parametrize(
    "item,val",
    [
        ["p", 16],
        ["L", 38],
        ["P", 42],
        ["v", 22],
        ["t", 20],
        ["s", 19],
    ],
)
def test_priority(item, val):
    assert find_priority(item) == val
