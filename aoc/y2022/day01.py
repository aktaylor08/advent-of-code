#!/usr/bin/env python3
import sys


def file_gen(file_name):
    with open(file_name) as inf:
        for line in inf:
            try:
                yield int(line.strip())
            except:
                yield None


def top_three(current: list[tuple[int, int]], new_elf: int, new_max: int, top_x: int = 3) -> list[tuple[int, int]]:
    ret = list(current)
    if len(current) < top_x:
        ret.append((new_max, new_elf))
    elif any([x[0] < new_max for x in current]):
        ret = ret[:-1] + [(new_max, new_elf)]
    return sorted(ret, reverse=True)


def find_elf(cal_gen):
    result = []
    elf = 0
    cal = 0
    for val in cal_gen:
        if val is None:
            result = top_three(result, elf, cal)
            elf += 1
            cal = 0
        else:
            cal += val
    print(result)
    print(sum([x[0] for x in result]))


if __name__ == "__main__":
    find_elf(file_gen(sys.argv[1]))
