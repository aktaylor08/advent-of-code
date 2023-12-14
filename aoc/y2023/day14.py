from itertools import cycle
from aoc import get_input


def tilt_up(rocks: list[list[str]]) -> list[list[str]]:
    for col in range(len(rocks[0])):
        for row in range(len(rocks)):
            if rocks[row][col] in ["O", "#"]:
                continue
            for up in range(row + 1, len(rocks)):
                if rocks[up][col] == "#":
                    break
                if rocks[up][col] == "O":
                    rocks[row][col] = "O"
                    rocks[up][col] = "."
                    break
    return rocks


def tilt_down(rocks: list[list[str]]) -> list[list[str]]:
    rocks.reverse()
    tilt_up(rocks)
    rocks.reverse()
    return rocks


def tilt_left(rocks: list[list[str]]) -> list[list[str]]:
    for row in range(len(rocks)):
        for col in range(len(rocks[0])):
            if rocks[row][col] in ["O", "#"]:
                continue
            for right in range(col, len(rocks[row])):
                if rocks[row][right] == "#":
                    break
                if rocks[row][right] == "O":
                    rocks[row][col] = "O"
                    rocks[row][right] = "."
                    break
    return rocks


def tilt_right(rocks: list[list[str]]) -> list[list[str]]:
    for x in rocks:
        x.reverse()
    tilt_left(rocks)
    for x in rocks:
        x.reverse()
    return rocks


def spin(rocks):
    rocks = tilt_up(rocks)
    rocks = tilt_left(rocks)
    rocks = tilt_down(rocks)
    rocks = tilt_right(rocks)
    rock_locs = set()
    for r in range(len(rocks)):
        for c in range(len(rocks[0])):
            if rocks[r][c] == "O":
                rock_locs.add((r, c))
    return rocks, rock_locs


def pr(rest):
    print("------")
    for x in rest:
        print(x)


def weight(rock_locs, size):
    sum = 0
    for row, _ in rock_locs:
        sum += size - row
    return sum


if __name__ == "__main__":
    input = [[c for c in x] for x in get_input(2023, 14).split("\n")][:-1]
    rest = tilt_up(input)
    sum1 = 0
    for i, x in enumerate(rest):
        sum1 += sum([r == "O" for r in x]) * (len(rest) - i)
    rocks = input
    weights = {}
    history = []
    last = None
    while True:
        rocks, rock_locs = spin(rocks)
        a_hash = hash(tuple(rock_locs))
        if a_hash in weights:
            last = a_hash
            break
        else:
            weights[a_hash] = weight(rock_locs, len(rocks))
        history.append(a_hash)
    cycle_start = history.index(last)
    cycle_size = len(history) - cycle_start
    total = 1000000000
    cycle_count = (total - cycle_start) // cycle_size
    end_full_cycle = cycle_start + (cycle_size * cycle_count)
    remaining = total - end_full_cycle
    result = 0
    for x in range(remaining):
        result = weights[history[x + cycle_start]]
    print(sum1)
    print(result)
