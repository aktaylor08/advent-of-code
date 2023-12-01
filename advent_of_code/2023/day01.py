#!/usr/bin/env python3

from advent_of_code import get_input

DIGITS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def get_numbers(line: str) -> list[int, int]:
    nums = []
    for idx, ch in enumerate(line):
        if ch.isdigit():
            nums.append(int(ch))
        for stupid_idx, dig in enumerate(DIGITS):
            if line[idx:].startswith(dig):
                nums.append(stupid_idx + 1)
    return nums


if __name__ == "__main__":
    value = 0
    for line in get_input(2023, 1).split("\n"):
        line = line.strip()
        if not line:
            continue
        nums = get_numbers(line)
        value += nums[0] * 10
        value += nums[-1]
    print(value)
