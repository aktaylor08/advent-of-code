from operator import ne
from aoc import get_input
from enum import Enum
import math

import heapq
from dataclasses import dataclass, field


class Direction(Enum):
    none = -1
    up = 0
    right = 1
    down = 2
    left = 3


@dataclass(order=True)
class Square:
    dist: float
    value: int
    row: int = field(compare=False)
    col: int = field(compare=False)
    dir: Direction = field(compare=False)
    count: int = field(compare=False)


def parse_input(input):
    return [[int(c) for c in row] for row in input.strip().split("\n")]


def search(amap):
    # row, col, dist, direction, direction count
    square_map = {}
    visited = set()
    for row in range(len(amap)):
        for col in range(len(amap[row])):
            square = Square(math.inf, amap[row][col], row, col, Direction.none, 1)
            square_map[(row, col)] = square
    prev = [[None for c in range(len(amap[0]))] for r in range(len(amap))]
    square_map[(0, 0)].dist = 0
    square_map[(0, 0)].dir = Direction.right
    visited.add((0, 0))
    the_heap = [square_map[(0, 0)]]
    heapq.heapify(the_heap)
    while len(the_heap) > 0:
        square = heapq.heappop(the_heap)
        print(square)
        if square.row == len(amap) - 1 and square.col == len(amap[0]) - 1:
            break
        for dr, dc, new_direct in get_diffs(square.dir, square.count):
            newr = dr + square.row
            newc = dc + square.col
            if 0 <= newr < len(amap) and 0 <= newc < len(amap[0]):
                if (newr, newc) not in visited:
                    neighbor = square_map[(newr, newc)]
                    next = neighbor.value + square.dist
                    if next < neighbor.dist:
                        if new_direct == square.dir:
                            neighbor.count = square.count + 1
                            neighbor.dir = square.dir
                        else:
                            neighbor.count = 1
                            neighbor.dir = new_direct
                        neighbor.dist = next
                        # Change directions too
                        the_heap.append(neighbor)
                        prev[newr][newc] = square
        visited.add((square.row, square.col))
        heapq.heapify(the_heap)
    cur = (len(amap) - 1, len(amap) - 1)
    no_print = set()
    print(square_map[cur])
    while cur != (0, 0):
        no_print.add(cur)
        thing = prev[cur[0]][cur[1]]
        cur = (thing.row, thing.col)
    for row in range(len(amap)):
        for col in range(len(amap[0])):
            if (row, col) in no_print:
                print(".", end="")
            else:
                print(amap[row][col], end="")
        print()
    cur = (len(amap) - 1, len(amap) - 1)
    no_print = set()
    print(square_map[cur])


def get_diffs(direction, direction_count):
    if direction_count <= 3:
        return [
            (1, 0, Direction.down),
            (-1, 0, Direction.up),
            (0, 1, Direction.right),
            (0, -1, Direction.left),
        ]
    else:
        dmap = {
            Direction.right: [
                (1, 0, Direction.down),
                (-1, 0, Direction.up),
                (0, -1, Direction.left),
            ],
            Direction.left: [
                (1, 0, Direction.down),
                (-1, 0, Direction.up),
                (0, 1, Direction.right),
            ],
            Direction.up: [
                (1, 0, Direction.down),
                (0, 1, Direction.right),
                (0, -1, Direction.left),
            ],
            Direction.down: [
                (-1, 0, Direction.up),
                (0, 1, Direction.right),
                (0, -1, Direction.left),
            ],
        }
        return dmap[direction]


def sample_input():
    return "11599\n99199\n99199\n99199\n99111\n"


def main():
    amap = parse_input(sample_input())  # parse_input(get_input(2023, 17, 0))
    # amap = parse_input(get_input(2023, 17, 0))
    search(amap)


if __name__ == "__main__":
    main()
