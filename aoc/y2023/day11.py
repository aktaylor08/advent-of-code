from aoc import get_input
import numpy as np


def parse_input(input: list[str]) -> tuple[list[tuple[int, int]], list[int], list[int]]:
    locs = []
    gal_rows = set()
    gal_cols = set()
    rows = 0
    cols = 0
    for row, line in enumerate(input):
        line = line.strip()
        if line == "":
            continue
        cols = len(line)
        rows += 1
        for col, thing in enumerate(line):
            if thing == "#":
                gal_rows.add(row)
                gal_cols.add(col)
                locs.append((row, col))
    offset = 0
    row_mask = []
    empty_count = 999999
    for x in range(rows):
        if x not in gal_rows:
            offset += empty_count
        row_mask.append(offset)
    offset = 0
    col_mask = []
    for y in range(cols):
        if y not in gal_cols:
            offset += empty_count
        col_mask.append(offset)
    return (
        locs,
        row_mask,
        col_mask,
    )


def dist(l1, l2, row_mask, col_mask):
    x1 = l1[0] + row_mask[l1[0]]
    y1 = l1[1] + col_mask[l1[1]]
    x2 = l2[0] + row_mask[l2[0]]
    y2 = l2[1] + col_mask[l2[1]]
    return abs((x2 - x1)) + abs((y2 - y1))


def main():
    input = get_input(2023, 11)
    locs, row_mask, col_mask = parse_input(input.split("\n"))
    sum = 0
    for i, loc in enumerate(locs):
        for j in range(i + 1, len(locs)):
            sum += dist(locs[i], locs[j], row_mask, col_mask)
    print(sum)


if __name__ == "__main__":
    main()
