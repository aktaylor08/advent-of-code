from aoc import get_input
from shapely import Polygon


def from_char(thechar: str) -> tuple[int, int]:
    return {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}[thechar]


def calc2(inputs):
    last = (0, 0)
    points = [last]
    for d, amount in inputs:
        dr, dc = from_char(d)
        dr = dr * amount
        dc = dc * amount
        new_point = (last[0] + dr, last[1] + dc)
        points.append(new_point)
        last = new_point
    p = Polygon(points)
    print(int(p.area + (p.length / 2) + 1))


def main():
    input1 = []
    input2 = []
    dd = {"0": "R", "1": "D", "2": "L", "3": "U"}
    for line in get_input(2023, 18).strip().split("\n"):
        d, num, color = line.split()
        input1.append((d, int(num)))
        color = color[2:8]
        val = int(color[:-1], 16)
        adir = dd[color[-1]]
        input2.append((adir, val))
    calc2(input1)
    calc2(input2)


if __name__ == "__main__":
    main()
