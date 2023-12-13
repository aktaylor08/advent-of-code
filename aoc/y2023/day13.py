from aoc import get_input


def find_mirror(line) -> dict[int, int]:
    # Assum mirror is at least after 1 or before end
    mirrors = dict()
    for idx in range(1, len(line)):
        smallest = min(idx, len(line) - idx)
        front = tuple(line[idx - smallest : idx])
        back = tuple(reversed(line[idx : idx + smallest]))
        if front == back:
            mirrors[idx] = smallest
    return mirrors


def merge_lines(current: dict[int, int] | None, new_lines: dict[int, int], v=False):
    if current is None:
        return new_lines
    else:
        if v:
            print("m", current, new_lines)
        ret = {}
        for key in set(current.keys()).intersection(new_lines.keys()):
            ret[key] = min(current[key], new_lines[key])
        return ret


def process_input(lines, v=False):
    in_lines = None
    for line in lines:
        line_vals = find_mirror(line)
        in_lines = merge_lines(in_lines, line_vals, v=v)
    return in_lines


def part2(lines):
    counts = {}
    for line in lines:
        line_vals = find_mirror(line)
        for x in line_vals:
            counts[x] = counts.get(x, 0) + 1
    return [i for i, x in counts.items() if x == len(lines) - 1]


def main():
    sum = 0
    sum2 = 0
    for data in get_input(2023, 13).split("\n\n"):
        feild = [x for x in data.split("\n") if x != ""]
        cols = {x: [] for x in range(len(feild[0]))}
        for line in feild:
            for i, ch in enumerate(line):
                cols[i].append(ch)
        result = process_input(feild)
        if len(result) == 1:
            sum += list(result.keys())[0]
        else:
            result = process_input(["".join(x) for x in cols.values()])
            if len(result) == 1:
                sum += list(result.keys())[0] * 100
            else:
                raise ("Exception")
        c = part2(feild)
        r = part2(["".join(x) for x in cols.values()])
        if c:
            sum2 += c[0]
        if r:
            sum2 += r[0] * 100
        if r and c:
            print("BAD")
        if not r and not c:
            print("BAD")

    print(sum)
    print(sum2)


if __name__ == "__main__":
    main()
