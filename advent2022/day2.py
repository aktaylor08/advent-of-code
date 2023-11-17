#!/usr/bin/env python3
import sys


from enum import Enum


class Choice(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


match_table = {
    Choice.Rock: {Choice.Rock: 3, Choice.Paper: 0, Choice.Scissors: 6},
    Choice.Paper: {Choice.Rock: 6, Choice.Paper: 3, Choice.Scissors: 0},
    Choice.Scissors: {Choice.Rock: 0, Choice.Paper: 6, Choice.Scissors: 3},

}


key = {
    'A': Choice.Rock,
    'B': Choice.Paper,
    'C': Choice.Scissors,
    'Y': Choice.Paper,
    'X': Choice.Rock,
    'Z': Choice.Scissors
}


def outcome(you: Choice, opp: Choice) -> int:
    """
    Win 6
    Lose 0 
    draw 3
    """
    return match_table[you][opp]


def score_game(choices: tuple[Choice, Choice]):
    return outcome(*choices) + choices[0].value


def parse_line(line: str) -> tuple[Choice, Choice]:
    a, b = line.split()
    return key[a], key[b]


def file_gen(file_name):
    with open(file_name) as inf:
        for line in inf:
            yield line.strip()


if __name__ == "__main__":
    pass
