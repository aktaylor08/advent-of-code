from aoc import get_input

import numpy as np
from functools import total_ordering
import matplotlib.pyplot as plt
import heapq


@total_ordering
class Brick:
    def __init__(self, start, end, idx):
        self.start = start
        self.end = end
        self.hset = set()
        count = idx % 26
        double = idx // 26
        self.name = chr(97 + count) * (double + 1)

        startx = start[0]
        endx = end[0]
        starty = start[1]
        endy = end[1]
        for x in range(startx, endx + 1):
            for y in range(starty, endy + 1):
                self.hset.add((x, y))
        self.resting = []
        self.support = []

    def down(self):
        self.start = (self.start[0], self.start[1], self.start[2] - 1)
        self.end = (self.end[0], self.end[1], self.end[2] - 1)

    def collide(self, other):
        if len(self.hset.intersection(other.hset)) > 0:
            return True
        return

    def __lt__(self, other):
        return self.start[2] < other.start[2]

    def __repr__(self):
        return self.name


def break_shit(brick):
    count = 0
    to_remove = [brick]
    removed = set()
    while to_remove:
        count += 1
        current = to_remove[0]
        to_remove = to_remove[1:]
        removed.add(current.name)
        for x in current.support:
            names = {gone.name for gone in x.resting}
            if len(names.difference(removed)) == 0:
                to_remove.append(x)
    return count - 1


def parse(stuff):
    bricks = []
    settled = []
    base_bricks = []
    for idx, line in enumerate(stuff.split("\n")):
        start, end = line.split("~")
        start = tuple(int(x) for x in start.split(","))
        end = tuple(int(x) for x in end.split(","))
        heapq.heappush(bricks, Brick(start, end, idx))
    while bricks:
        falling_brick = heapq.heappop(bricks)
        go_on = True
        while go_on:
            zlow = falling_brick.start[2]
            if zlow == 1:
                settled.append(falling_brick)
                base_bricks.append(falling_brick)
                go_on = False
            else:
                # Check for bricks that it will collide with on the way down
                for other_brick in reversed(settled):
                    if other_brick.end[2] == zlow - 1:
                        if falling_brick.collide(other_brick):
                            other_brick.support.append(falling_brick)
                            falling_brick.resting.append(other_brick)
                            if go_on:
                                settled.append(falling_brick)
                                go_on = False
            if go_on:
                falling_brick.down()
    destroy_count = 0
    will_break = []
    for brick in settled:
        if len(brick.support) == 0:
            destroy_count += 1
        else:
            for other in brick.support:
                if len(other.resting) < 2:
                    will_break.append(brick)
                    break
            else:
                destroy_count += 1
    print(destroy_count)
    print(len(will_break))
    removed = 0
    for x in will_break:
        a = break_shit(x)
        removed += a
    print(removed)


def main():
    garbagein = get_input(2023, 22).strip()
    parse(garbagein)


if __name__ == "__main__":
    main()
