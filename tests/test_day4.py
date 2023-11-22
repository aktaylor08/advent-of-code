import pytest
from advent2022.day4 import get_ranges, contains


@pytest.mark.parametrize(
    "input,ranges",
    [
        ["2-4,6-8", ((2, 4), (6, 8))],
        ["2-3,4-5", ((2, 3), (4, 5))],
        ["5-7,7-9", ((5, 7), (7, 9))],
        ["2-8,3-7", ((2, 8), (3, 7))],
        ["6-6,4-6", ((6, 6), (4, 6))],
        ["2-6,4-8", ((2, 6), (4, 8))],
    ],
)
def test_range(input, ranges):
    assert get_ranges(input) == ranges


@pytest.mark.parametrize(
    "ranges,is_subset",
    [
        [((2, 4), (6, 8)), False],
        [((2, 3), (4, 5)), False],
        [((5, 7), (7, 9)), False],
        [((2, 8), (3, 7)), True],
        [((6, 6), (4, 6)), True],
        [((2, 6), (4, 8)), False],
    ],
)
def test_subset(ranges, is_subset):
    assert contains(ranges[0], ranges[1]) == is_subset
