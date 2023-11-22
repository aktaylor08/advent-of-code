import pytest
from advent2022.day5 import Crane


def test_parse():
    values = [
        "    [D]     ",
        "[N] [C]     ",
        "[Z] [M] [P] ",
        " 1   2   3  ",
    ]
    crane = Crane()
    crane.parse(values)
    assert crane.stacks["1"] == ["N", "Z"]
    assert crane.stacks["2"] == ["D", "C", "M"]
    assert crane.stacks["3"] == ["P"]


def test_move():
    values = [
        "    [D]     ",
        "[N] [C]     ",
        "[Z] [M] [P] ",
        " 1   2   3  ",
    ]
    crane = Crane()
    crane.parse(values)
    crane.move(1, "2", "1")
    crane.move(3, "1", "3")
    crane.move(2, "2", "1")
    crane.move(1, "1", "2")
