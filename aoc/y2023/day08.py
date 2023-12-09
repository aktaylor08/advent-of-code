from asyncore import loop
from matplotlib.cbook import get_sample_data
import numpy as np
import math

from aoc import get_input, sample_input


def parse_input(
    input: str
) -> tuple[set[str], set[str], list[str], dict[str, tuple[str, str]]]:
    """
    Return list of RLRLRLRLRLRL
    and name, left, right tuple for steps
    """
    lines = input.split("\n\n")
    commands = lines[0][:]
    nodes = {}
    starts = set()
    targets = set()
    for x in lines[1].split("\n"):
        if x != "":
            name, goto = x.strip().split("=")
            left, right = goto.split(",")
            nodes[name.strip()] = (left.lstrip()[1:], right.strip()[:-1])
            if name.strip()[-1] == "A":
                starts.add(name.strip())
            elif name.strip()[-1] == "Z":
                targets.add(name.strip())

    return starts, targets, commands, nodes


def done(values: set[str]) -> bool:
    for x in list(values):
        if x[-1] != "Z":
            return False
    return True


def travel_1(current, targets, commands, nodes):
    idx = 0
    while not done(targets):
        if idx % 1_000_000 == 0:
            print(idx)
        new_current = set()
        for c in current:
            targets = nodes[c]
            cmd = commands[idx % len(commands)]
            if cmd == "L":
                c = targets[0]
            else:
                c = targets[1]
            new_current.add(c)
        current = new_current
        idx += 1
    return idx


def travel_2(current, final_dest, commands, nodes):
    indexes = {x: [] for x in final_dest}
    idx = 0
    while not all([len(v) > 1 for v in indexes.values()]):
        new_current = set()
        for c in current:
            if c in indexes:
                indexes[c].append(idx)
            places = nodes[c]
            cmd = commands[idx % len(commands)]
            if cmd == "L":
                c = places[0]
            else:
                c = places[1]
            new_current.add(c)
        current = new_current
        idx += 1
    # We now have first time seen and second time seen for all nodes. So we can assume that we can now just do some math to see when they all meet
    eqs = []
    values = []
    p_facs = []
    for t, locs in indexes.items():
        print(t, locs)
        q = locs[0], locs[1] - locs[0]
        values.append(locs[0])
        eqs.append(q)
    print(math.lcm(*values))
    math.gcd()
    print(values)
    x = 1
    for v, _ in eqs:
        x *= v
    return x


if __name__ == "__main__":
    starts, targets, commands, nodes = parse_input(get_input(2023, 8))
    # print(travel_1(set(["AAA"]), ["ZZZ"], commands, nodes))
    print(travel_2(starts, targets, commands, nodes))
