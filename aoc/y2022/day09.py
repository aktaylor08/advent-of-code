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
    no = 8


class Rope:
    def __init__(self):
        # HEad tail loc
        self.current_loc = [(0, 0), (0, 0)]
        self.tail_locs = set([self.current_loc[1]])

    def move(self, direction: Dir) -> Dir | None:
        curx, cury = self.current_loc[0]
        if direction == Dir.left:
            curx -= 1
        if direction == Dir.right:
            curx += 1
        if direction == Dir.up:
            cury += 1
        if direction == Dir.down:
            cury -= 1
        if direction == Dir.up_left:
            cury += 1
            curx -= 1
        if direction == Dir.up_right:
            cury += 1
            curx += 1
        if direction == Dir.down_right:
            cury -= 1
            curx += 1
        if direction == Dir.down_left:
            cury -= 1
            curx -= 1
        self.current_loc[0] = (curx, cury)  # type: ignore
        return self.fix_tail()

    def fix_tail(self) -> Dir | None:
        (headx, heady) = self.current_loc[0]
        (tailx, taily) = self.current_loc[1]
        diffx = headx - tailx
        diffy = heady - taily
        dx = 0
        dy = 0
        if abs(diffx) > 1 or abs(diffy) > 1:
            if abs(diffy) > 0:
                dy = diffy / abs(diffy)
                taily += dy
            if abs(diffx) > 0:
                dx = diffx / abs(diffx)
                tailx += dx
        self.current_loc[1] = (tailx, taily)  # type: ignore
        self.tail_locs.add((tailx, taily))  # type: ignore
        return to_dir(dx, dy)

    def go(self, way: Dir, count: int):
        for _ in range(count):
            self.move(way)


class RopeGroup:
    def __init__(self, num_ropes: int):
        self.ropes = [Rope() for _ in range(num_ropes)]

    def move_head(self, way, count):
        for _ in range(count):
            action = way
            for idx, rope in enumerate(self.ropes):
                action = rope.move(action)


def to_dir(dx, dy):
    if abs(dx) == 0:
        if dy == 0:
            return Dir.no
        elif dy > 0:
            return Dir.up
        else:
            return Dir.down
    elif abs(dy) == 0:
        if dx == 0:
            return Dir.no
        elif dx > 0:
            return Dir.right
        else:
            return Dir.left
    else:
        if dx > 0:
            if dy > 0:
                return Dir.up_right
            else:
                return Dir.down_right
        elif dy > 0:
            return Dir.up_left
        else:
            return Dir.down_left


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        dmap = {
            "R": Dir.right,
            "L": Dir.left,
            "U": Dir.up,
            "D": Dir.down,
        }
        group = RopeGroup(10)
        r = Rope()
        for x in f:
            d, a = x.strip().split()
            group.move_head(dmap[d], int(a))
        print(len(group.ropes[-2].tail_locs))
