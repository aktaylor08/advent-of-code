#!/usr/bin/env python3
import sys
import re


class Crane:
    def __init__(self):
        self.stacks = {}

    def parse(self, init_lines: list[str]):
        idxs = {}
        for idx, ch in enumerate(init_lines[-1]):
            if ch.isdigit():
                idxs[idx] = ch
                self.stacks[ch] = []
        for line in reversed(init_lines[:-1]):
            for idx, ch in enumerate(line):
                if idx in idxs:
                    if ch != " ":
                        self.add_item(idxs[idx], [ch])

    def add_item(self, stack: str, item: list[str]):
        self.stacks[stack] = item + self.stacks[stack]

    def remove_item(self, stack: str, count: int = 1) -> list[str]:
        val = self.stacks[stack][:count]
        self.stacks[stack] = self.stacks[stack][count:]
        return val

    def move(self, num: int, stack_from: str, stack_to: str):
        v = self.remove_item(stack_from, num)
        self.add_item(stack_to, v)


if __name__ == "__main__":
    with open(sys.argv[1]) as inf:
        init_lines = []
        done_init = False
        crane = Crane()
        search = re.compile("move (\d+) from (\d+) to (\d+)")
        for line in inf:
            if done_init:
                res = search.search(line)
                crane.move(int(res.group(1)), res.group(2), res.group(3))
            else:
                if line.strip() == "":
                    done_init = True
                    crane.parse(init_lines)
                else:
                    init_lines.append(line)
        print("".join(crane.stacks[str(x + 1)][0] for x in range(len(crane.stacks))))
