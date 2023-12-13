from attr import field
from aoc import get_input


def find_mirror(line) -> set[tuple[int, int]]:
    # Assum mirror is at least after 1 or before end
    mirrors = set()
    for idx in range(1, len(line)):
        smallest = min(idx, len(line) - idx)
        front = tuple(line[idx - smallest : idx])
        back = tuple(reversed(line[idx : idx + smallest]))
        if front == back:
            mirrors.add((idx, smallest))
    return mirrors


def merge_lines(current: set[tuple[int, int]] | None, new_lines: set[tuple[int, int]]):
    if current is None:
        return new_lines
    else:
        return current.intersection(new_lines)


def process_input(lines, v=False):
    in_lines = None
    for line in lines:
        in_lines = merge_lines(in_lines, find_mirror(line))
        if v:
            print(in_lines)
    return in_lines


def main():
    sum = 0
    for data in open("/Users/adamtaylor/poop.txt").read().split("\n\n"):
        feild = [x for x in data.split("\n")]
        cols = {x: [] for x in range(len(feild[0]))}
        for line in feild:
            for i, ch in enumerate(line):
                cols[i].append(ch)
        result = process_input(feild)
        if len(result) == 1:
            sum += list(result)[0][0]
        else:
            result = process_input(["".join(x) for x in cols.values()])
            if len(result) == 1:
                sum += list(result)[0][0] * 100
            else:
                print("\n".join(feild))
                process_input(feild, v=True)
                for x in cols.values():
                    print(x)
                process_input(cols.values(), v=True)
    print(sum)


if __name__ == "__main__":
    main()
