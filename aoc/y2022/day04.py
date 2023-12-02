#!/usr/bin/env python3
import sys


def file_gen(file_name):
    with open(file_name) as inf:
        for line in inf:
            yield get_ranges(line.strip())


def contains(range1: tuple[int, int], range2: tuple[int, int]) -> bool:
    """
    x1      x2
       y1 y2
       or
      x1 x2
    y1      y2
    """
    x1, x2 = range1
    y1, y2 = range2
    if x1 <= y1 <= x2 and x1 <= y2 <= x2:
        return True
    if y1 <= x1 <= y2 and y1 <= x2 <= y2:
        return True
    return False


def overlap(range1: tuple[int, int], range2: tuple[int, int]) -> bool:
    """
      x1      x2
     y1   y2
         or
    x1    x2
      y1      y2
    """
    x1, x2 = range1
    y1, y2 = range2
    if x1 <= y2 <= x2 or x1 <= y1 <= x2:
        return True
    if y1 <= x1 <= y2 or y1 <= x2 <= y2:
        return True
    return False


def get_ranges(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    r1, r2 = line.split(",")
    r1 = r1.split("-")
    r2 = r2.split("-")
    return (int(r1[0]), int(r1[1])), (int(r2[0]), int(r2[1]))


if __name__ == "__main__":
    val = 0
    for range1, range2 in file_gen(sys.argv[1]):
        if overlap(range1, range2):
            val += 1
    print(val)
