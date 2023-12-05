import enum
import math

from aoc import get_input, sample_input


class SeedMap:
    def __init__(self, name: str, entries: list[tuple[int, int, int]]):
        self.name = name
        self.entries = entries

    def __repr__(self):
        return f"{self.name}->{self.entries}"

    def get_dest(self, entry: int) -> int:
        for dest_start, src_start, the_range in self.entries:
            if src_start <= entry < (src_start + the_range):
                offset = dest_start - src_start
                diff = entry - src_start
                return src_start + offset + diff
        return entry


def parse(input: str) -> tuple[list[int], list[SeedMap]]:
    input_lines = input.split("\n")
    maps: list[SeedMap] = []
    seeds = [int(x) for x in input_lines[0].split(":")[1].lstrip().strip().split()]
    name = None
    entries = []
    for line in input_lines[2:]:
        if name is None:
            name = line.strip()[:-1]
            entries = []
        elif line != "":
            entries.append([int(x) for x in line.split(" ")])
        else:
            maps.append(SeedMap(name, entries))
            name = None
    return seeds, maps


def do_mapping(seed: int, mapping: list[SeedMap]):
    res = seed
    for x in mapping:
        res = x.get_dest(res)
    return res


def work():
    input = get_input(2023, 5)
    seeds, maps = parse(input)
    locations = [do_mapping(x, maps) for x in seeds]
    print("Part 1: ", min(locations))
    print(seeds)
    mins = []
    new_seeds = []
    for idx, start in enumerate(seeds[::2]):
        size = seeds[idx * 2 + 1]
        print(start, size)
        mins.append(min(do_mapping(x, maps) for x in range(start, start + size)))
    print("Part 2", min(mins))


if __name__ == "__main__":
    work()
