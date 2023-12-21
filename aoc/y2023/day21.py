from aoc import get_input


def search(
    amap, row, col, depth, complete, history, oob_history, off_down=0, off_right=0
) -> tuple[int, set]:
    sum = 0
    oob = set()
    complete.add((row, col, depth, off_down, off_right))
    if (row, col, depth, off_down, off_right) in history:
        return history[(row, col, depth, off_down, off_right)], oob_history[
            (row, col, depth, off_down, off_right)
        ]
    if depth == 0:
        sum += 1
    else:
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newr = row + dr
            newc = col + dc
            if 0 <= newr < len(amap) and 0 <= newc < len(amap[0]):
                if (
                    amap[newr][newc] in [".", "S"]
                    and (newr, newc, depth - 1, off_down, off_right) not in complete
                ):
                    value, new_oob = search(
                        amap,
                        newr,
                        newc,
                        depth - 1,
                        complete,
                        history,
                        oob_history,
                        off_down,
                        off_right,
                    )
                    oob.update(new_oob)
                    sum += value
            else:
                oob.add((newr, newc, depth - 1, off_down, off_right))
    if (row, col, depth, off_down, off_right) not in history:
        history[(row, col, depth, off_down, off_right)] = sum
    if (row, col, depth, off_down, off_right) not in oob_history:
        history[(row, col, depth, off_down, off_right)] = set(oob)
    return sum, set(oob)


def main():
    step_count = 500
    amap = get_input(2023, 21, 0).strip().split()
    start = None
    for row, x in enumerate(amap):
        col = x.find("S")
        if col >= 0:
            start = (row, col)
    history = {}
    complete = set()
    oob_history = {}
    value, oob = search(
        amap, start[0], start[1], step_count, complete, history, oob_history
    )
    out_of_bounds = [(o[0], o[1], o[2], o[3], o[4]) for o in oob]
    total = value
    while out_of_bounds:
        row, col, dist, off_down, off_right = out_of_bounds[0]
        out_of_bounds = out_of_bounds[1:]
        row, col, off_down, off_right = wrap(
            row, col, len(amap), len(amap[0]), off_down, off_right
        )
        if (row, col, dist, off_down, off_right) not in complete:
            if (row, col, dist, off_down, off_right) in history:
                new_value = history[(row, col, dist, off_down, off_right)]
                oob = []
            else:
                new_value, oob = search(
                    amap,
                    row,
                    col,
                    dist,
                    complete,
                    history,
                    oob_history,
                    off_down,
                    off_right,
                )
            for x in oob:
                out_of_bounds.append(x)
            total += new_value
    print(total)


def wrap(row, col, len_row, len_col, off_down, off_right):
    if row < 0:
        row = len_row - 1
        off_down -= 1
    if row >= len_row:
        row = 0
        off_down += 1
    if col < 0:
        col = len_col - 1
        off_right -= 1
    if col >= len_col:
        col = 0
        off_right += 1
    return row, col, off_down, off_right


if __name__ == "__main__":
    main()
