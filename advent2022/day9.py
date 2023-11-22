#!/usr/bin/env python3

import sys
from enum import Enum


class Dir(Enum):
    left = 0
    right = 1
    up = 2
    down = 3
    up_left = 4
    up_right = 5
    down_right = 6
    down_left = 7


class Rope:
    def __init__(self):
        # HEad tail loc
        self.current_loc = [(0, 0), (0, 0)]
        self.tail_locs = set([self.current_loc[1]])

    def move(self, direction: Dir):
        curx, cury = self.current_loc[0]
        if direction in [Dir.left, Dir.down_left, Dir.up_left]:
            curx -= 1
        if direction in [Dir.right, Dir.up_right, Dir.down_right]:
            curx += 1
        if direction in [Dir.up, Dir.up_left, Dir.up_right]:
            cury += 1
        if direction == [Dir.down, Dir.down_right, Dir.down_left]:
            cury -= 1
        self.current_loc[0] = (curx, cury)  # type: ignore
        return self.fix_tail()

    def fix_tail(self) -> bool:
        (headx, heady) = self.current_loc[0]
        (tailx, taily) = self.current_loc[1]
        diffx = headx - tailx
        diffy = heady - taily
        move = False
        if abs(diffx) > 1 or abs(diffy) > 1:
            move = True
            if abs(diffy) > 0:
                taily += diffy / abs(diffy)
            if abs(diffx) > 0:
                tailx += diffx / abs(diffx)
        self.current_loc[1] = (tailx, taily)  # type: ignore
        self.tail_locs.add((tailx, taily))  # type: ignore
        return move

    def go(self, way: Dir, count: int):
        tail_moved = False
        for _ in range(count):
            tail_moved = tail_moved or self.move(way)
        return tail_moved


class RopConnection:
    def __init__(self, num: int):
        ropes = []


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        dmap = {
            "R": Dir.right,
            "L": Dir.left,
            "U": Dir.up,
            "D": Dir.down,
        }
        r = Rope()
        for x in f:
            d, a = x.strip().split()
            r.go(dmap[d], int(a))
        print(len(r.tail_locs))
