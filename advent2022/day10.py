#!/usr/bin/env python3
import sys


class Computer:
    def __init__(self):
        self.reg = 1
        self.cycle = 0
        self.history = []

    def do_op(self, args):
        self.history.append(self.reg)
        if args[0] == "noop":
            pass
        if args[0] == "addx":
            self.history.append(self.reg)
            self.reg = self.reg + int(args[1])


if __name__ == "__main__":
    c = Computer()
    with open(sys.argv[1]) as f:
        for line in f:
            c.do_op(line.strip().split())
    value = 0
    for cycle in range(20, len(c.history), 40):
        value += cycle * c.history[cycle - 1]
    pixels = []
    for row in range(6):
        values = []
        for pix in range(40):
            if pix - 1 <= c.history[pix + (row * 40)] <= pix + 1:
                values.append("#")
            else:
                values.append(".")
        pixels.append(values)
    for row in pixels:
        print("".join(row))
