from ctypes.wintypes import DWORD
from aoc import get_input


class Grouping:
    def __init__(self, mark: str, size: int, start: int):
        self.mark = mark
        self.size = size
        self.start = start
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.mark} {self.start}-{self.start + self.size} -> {self.size}"


def get_groups(group_str: str):
    last = None
    start_idx = 0
    groups = []
    for idx, c in enumerate(group_str):
        if last != c or idx == len(group_str) - 1:
            if last is not None:
                g = Grouping(last, idx - start_idx, start_idx)
                groups.append(g)
            start_idx = idx
        last = c

    return groups


def possible_fits(count, line_str):
    if count > len(line_str):
        return None
    if line_str[0] == ".":
        return None
    sub_str = line_str[:count]
    if "." in sub_str:
        return None
    if count < len(line_str):
        if line_str[count] == ".":
            return line_str[count:]
        elif line_str[count] == "?":
            return "." + line_str[count + 1 :]
        else:
            return None
    else:
        return ""

    # If there is leftover and it is a ? we have to flip it to '.' if it is a # it isn't possible


def do_line(springs, counts) -> int:
    if len(counts) == 0:
        if "#" in springs:
            return 0
        else:
            return 1
    first = counts[0]
    rest = counts[1:]
    total_sub = 0
    for idx in range(len(springs)):
        next_spring = possible_fits(first, springs[idx:])
        if next_spring is not None:
            total_sub += do_line(next_spring, rest)
    return total_sub


def main():
    sum = 0
    for line in get_input(2023, 12, 1).split("\n"):
        if line.strip() == "":
            continue
        springs, counts = line.split()
        counts = [int(x) for x in counts.strip().split(",")]
        a = do_line(springs, counts)
        print(a, line)
        sum += a
    do_line("?###????????", [3, 2, 1])


if __name__ == "__main__":
    main()
