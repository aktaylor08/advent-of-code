from aoc import get_input, sample_input
from functools import reduce

import numpy as np


def recursive(arr):
    if np.all(arr == 0):
        return 0, 0
    else:
        front, back = recursive(np.diff(arr))
        return arr[0] - front, arr[-1] + back


def work():
    part1 = 0
    part2 = 0
    for line in [
        np.array([int(n) for n in line.split()])
        for line in get_input(2023, 9).split("\n")
        if line != ""
    ]:
        a, b = recursive(line)
        part1 += b
        part2 += a
    print(part1)
    print(part2)


if __name__ == "__main__":
    work()
