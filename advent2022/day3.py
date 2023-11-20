#!/usr/bin/env python3
import sys


def split_line(line: str) -> tuple[str, str]:
    size = len(line) // 2
    return line[:size], line[size:]


def file_gen(file_name):
    with open(file_name) as inf:
        for line in inf:
            yield split_line(line.strip())


def find_common(parts: list[str]):
    common = set(parts[0])
    for other in parts[1:]:
        common = common.intersection(other)
    return list(common)[0]


def find_priority(item: str) -> int:
    if item[0].isupper():
        return ord(item[0]) - ord("A") + 27
    else:
        return ord(item[0]) - ord("a") + 1


if __name__ == "__main__":
    score = 0
    lines = []
    for one, two in file_gen(sys.argv[1]):
        lines.append(one + two)
        if len(lines) == 3:
            score += find_priority(find_common(lines))
            lines = []
    print(score)
