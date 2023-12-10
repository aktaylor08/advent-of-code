from aoc import get_input


def get_possible_neighbors(
    loc: tuple[int, int], the_map: list[str]
) -> list[tuple[int, int]]:
    """| is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starti"""
    change_map = {
        "|": [(1, 0), (-1, 0)],
        "-": [(0, 1), (0, -1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
        ".": [],
        "S": [(1, 0), (-1, 0), (0, 1), (0, -1)],
    }
    options = []
    cur_char = the_map[loc[0]][loc[1]]
    for x in change_map[cur_char]:
        new_row = loc[0] + x[0]
        new_col = loc[1] + x[1]
        # check bounds
        if 0 <= new_row < len(the_map) and 0 <= new_col < len(the_map[new_row]):
            options.append((new_row, new_col))
    return options


def get_valid_neighbors(loc: tuple[int, int], the_map: list[str]):
    """| is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starti"""
    values = []
    possible = get_possible_neighbors(loc, the_map)
    for x in possible:
        if loc in get_possible_neighbors(x, the_map):
            values.append(x)
    return values


def parse_map(input: str) -> tuple[list[str], tuple[int, int]]:
    map = []
    start = (-1, -1)
    for idx, line in enumerate(input.split("\n")):
        if line.strip() != "":
            col = line.find("S")
            if col >= 0:
                start = (idx, col)
            map.append(line.strip())
    return map, start


def travel(start, the_map):
    queue = [start]
    visited = {start: 0}
    dist = 1
    while queue:
        new_queue = []
        for node in queue:
            for possible in get_valid_neighbors(node, the_map):
                if possible not in visited:
                    visited[possible] = dist
                    new_queue.append(possible)
            queue = new_queue
        dist += 1
    return visited, dist


if __name__ == "__main__":
    the_map, start = parse_map(get_input(2023, 10, sample=1))
    dist_map, dist = travel(start, the_map)
    for i in range(len(the_map)):
        for j in range(len(the_map[i])):
            get_possible_neighbors((i, j), the_map)
    print(max(dist_map.values()))
