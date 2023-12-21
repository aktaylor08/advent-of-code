from aoc import get_input


def search(amap, row, col, depth, complete) -> int:
    complete.add((row, col, depth))
    if depth == 0:
        return 1
    sum = 0
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newr = row + dr
        newc = col + dc
        if 0 <= newr < len(amap) and 0 <= newc < len(amap[0]):
            if amap[newr][newc] == "." and (newr, newc, depth - 1) not in complete:
                sum += search(amap, newr, newc, depth - 1, complete)
    return sum


def main():
    amap = get_input(2023, 21).strip().split()
    start = None
    for row, x in enumerate(amap):
        col = x.find("S")
        if col >= 0:
            start = (row, col)
    value = search(amap, start[0], start[1], 64, set())
    print(value + 1)


if __name__ == "__main__":
    main()
