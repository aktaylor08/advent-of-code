from advent2023.day01 import get_numbers


import pytest


@pytest.mark.parametrize(
    "line,nums",
    [
        ["1abc2I", [1, 2]],
        ["pqr3stu8vwx", [3, 8]],
        ["a1b2c3d4e5f", [1, 2, 3, 4, 5]],
        ["treb7uchet", [7]],
    ],
)
def test_parse(line, nums):
    assert get_numbers(line) == nums


@pytest.mark.parametrize(
    "line,nums",
    [
        ["two1nine", [2, 1, 9]],
        ["eightwothree", [8, 2, 3]],
        ["abcone2threexyz", [1, 2, 3]],
        ["xtwone3four", [2, 1, 3, 4]],
        ["4nineeightseven2", [4, 9, 8, 7, 2]],
        ["zoneight234", [1, 8, 2, 3, 4]],
        ["7pqrstsixteen", [7, 6]],
    ],
)
def test_evil_numbers(line, nums):
    assert get_numbers(line) == nums
