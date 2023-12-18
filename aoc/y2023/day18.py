from aoc import get_input
from itertools import chain
from shapely.geometry import Polygon, LinearRing, Point


def from_char(thechar: str) -> tuple[int, int]:
    return {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}[thechar]


def do_calc(instructions):
    last = None
    row_map = {}
    point_to_part = {}
    points = []
    parts = []
    xy = None
    for d, num in instructions:
        dr, dc = from_char(d)
        if last is None:
            row_map[0] = [(0, 0, d)]
            last = (0, 0, d)
            xy = (0, 0)
        part = [(last[0], last[1], d)]
        if xy in point_to_part:
            point_to_part[xy].append(part)
        else:
            point_to_part[xy] = [part]
        for _ in range(int(num)):
            last = (last[0] + dr, last[1] + dc, d)
            xy = (last[0], last[1])
            points.append(last)
            part.append(last)
            if last[0] in row_map:
                row_map[last[0]].append(last)
            else:
                row_map[last[0]] = [last]
            if xy in point_to_part:
                point_to_part[xy].append(part)
            else:
                point_to_part[xy] = [part]
        parts.append(part)

    rr, cc, zz = zip(*points)
    maxr = max(rr)
    minr = min(rr)
    minc = min(cc)
    maxc = max(cc)
    print(maxr, minr, minc, maxc)
    in_shape = False
    count = 0
    for row in range(minr, maxr + 1):
        for col in range(minc, maxc + 1):
            if (row, col) in point_to_part:
                count += 1
                dirs = set([p[2] for p in chain(*point_to_part[(row, col)])])
                if len(dirs) > 1:
                    if "U" in dirs:
                        in_shape = True
                    if "D" in dirs:
                        in_shape = False
                else:
                    if "D" in dirs or "U" in dirs:
                        in_shape = not in_shape
            else:
                if in_shape:
                    count += 1
    print(count)


def main():
    input1 = []
    input2 = []
    dd = {"0": "R", "1": "D", "2": "L", "3": "U"}
    for line in get_input(2023, 18, 0).strip().split("\n"):
        d, num, color = line.split()
        input1.append((d, num))
        color = color[2:8]
        val = int(color[:-1], 16)
        adir = dd[color[-1]]
        input2.append((adir, val))

    do_calc(input1)
    do_calc(input2)


if __name__ == "__main__":
    main()
