from aoc import get_input
from functools import cache


@cache
def do_line(springs, counts, pos=0, current=0) -> int:
    if pos == len(springs):
        if not counts and not current:
            return 1
        elif len(counts) == 1 and counts[0] == current:
            return 1
        else:
            return 0

        return not counts and not current
    if not counts:
        return "#" not in springs[pos:]
    chars = springs[pos]
    values = 0
    if chars in ["?", "."]:
        # A good spot
        if current != 0:
            if len(counts) > 0 and current == counts[0]:
                values += do_line(springs, counts[1:], pos + 1, current=0)
        else:
            values += do_line(springs, counts, pos + 1, current=0)
    if chars in ["?", "#"]:
        values += do_line(springs, counts, pos + 1, current + 1)
        # A bad spot
    return values


def main():
    sum = 0
    sum2 = 0
    for line in get_input(2023, 12).split("\n"):
        if line.strip() == "":
            continue
        springs, counts = line.split()
        counts = [int(x) for x in counts.strip().split(",")]
        sum += do_line(springs, tuple(counts))
        springs2 = "?".join(springs for x in range(5))
        counts2 = counts * 5
        sum2 += do_line(springs2, tuple(counts2))
    print(sum)
    print(sum2)
    springs = ".#"


if __name__ == "__main__":
    main()
