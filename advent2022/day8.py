#!/usr/bin/env python3

import sys


from enum import Enum


class Dir(Enum):
    left = 0
    up = 1
    right = 2
    down = 3


class Square:
    def __init__(self, height: int):
        self.height = height
        # left up right down
        self.max_tree = [-1, -1, -1, -1]
        self.since_tree = [{x: 0 for x in range(0, 10)} for _ in range(4)]

    def is_visible(self):
        return any((self.height > x for x in self.max_tree))

    def vis_num(self):
        return 1 if self.is_visible() else 0

    def viz_string(self):
        if self.is_visible():
            return "0"
        else:
            return "x"

    def view_in_direction(self, direction: Dir) -> int:
        return self.since_tree[direction.value][self.height]

    def view_score(self):
        return (
            self.since_tree[0][self.height]
            * self.since_tree[1][self.height]
            * self.since_tree[2][self.height]
            * self.since_tree[3][self.height]
        )

    def __repr__(self):
        return str(self.height)


class TreeMap:
    def __init__(self):
        self.mapping: list[list[Square]] = []

    def parse(self, map: list[str]):
        for x in map:
            x = x.strip()
            row = []
            for val in x:
                row.append(Square(int(val)))
            self.mapping.append(row)

    def print_viz(self):
        for row in self.mapping:
            print("".join(s.viz_string() for s in row))

    def do_viz(self):
        columns = len(self.mapping[0])
        rows = len(self.mapping)
        for col in range(0, columns):
            for row in range(0, rows):
                # Set the max left tree to be the lefts max or the left tree value
                if col > 0:
                    current_tree = self.mapping[row][col]
                    other = self.mapping[row][col - 1]
                    update_tree(current_tree, other, Dir.left)
                    offset_col = columns - col - 1
                    current_tree = self.mapping[row][offset_col]
                    other = self.mapping[row][offset_col + 1]
                    update_tree(current_tree, other, Dir.right)
                if row > 0:
                    current_tree = self.mapping[row][col]
                    other = self.mapping[row - 1][col]
                    update_tree(current_tree, other, Dir.up)
                    offset_row = rows - row - 1
                    current_tree = self.mapping[offset_row][col]
                    other = self.mapping[offset_row + 1][col]
                    update_tree(current_tree, other, Dir.down)


def update_tree(tree: Square, other: Square, direction: Dir):
    tree.max_tree[direction.value] = max(other.height, other.max_tree[direction.value])
    for height in range(0, 10):
        if height <= other.height:
            tree.since_tree[direction.value][height] = 1
            print("YET")
        else:
            print("opop")
            tree.since_tree[direction.value][height] = (
                other.since_tree[direction.value][height] + 1
            )


def main():
    map = TreeMap()
    with open(sys.argv[1]) as f:
        map.parse(f.readlines())
    map.do_viz()
    map.print_viz()
    value = 0
    for x in map.mapping:
        value += sum(y.vis_num() for y in x)
    print(f"viz: {value}")
    value = 0
    for row in map.mapping:
        for tree in row:
            value = max(tree.view_score(), value)
    print(value)


if __name__ == "__main__":
    main()
