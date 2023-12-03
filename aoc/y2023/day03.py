import re
import uuid

from aoc import get_input


class Number:
    def __init__(self, value):
        self.value = value
        self.used = False
        self.id = uuid.uuid4()

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


def parse_line(
    row: int, line: str
) -> tuple[list[tuple[int, int]], dict[tuple[int, int], Number]]:
    symbols = []
    numbers = {}
    for match in re.finditer(r"\d+", line):
        new_num = Number(int(match.group()))
        for num in range(match.span(0)[0], match.span(0)[1]):
            numbers[(row, num)] = new_num
    for col, ch in enumerate(line.strip()):
        if ch != "." and not ch.isdigit():
            symbols.append((row, col, ch))
    return symbols, numbers


def get_adjacent_numbers(row, col, numbers):
    adjacent = set()
    for dx, dy in [
        (1, 0),
        (1, 1),
        (1, -1),
        (0, 1),
        (0, -1),
        (-1, 0),
        (-1, 1),
        (-1, -1),
    ]:
        nx = row + dx
        ny = col + dy
        if (nx, ny) in numbers:
            adjacent.add(numbers[nx, ny])
    return list(adjacent)


def work():
    symbols = []
    numbers = {}
    for row, line in enumerate(get_input(2023, 3).split("\n")):
        sym, num = parse_line(row, line)
        symbols += sym
        numbers = {**numbers, **num}
    sum_1 = 0
    sum_2 = 0
    for x, y, ch in symbols:
        adj = get_adjacent_numbers(x, y, numbers)
        for num in adj:
            if not num.used:
                sum_1 += num.value
                num.used = True
        if ch == "*" and len(adj) == 2:
            sum_2 += adj[0].value * adj[1].value
    print(sum_1)
    print(sum_2)


if __name__ == "__main__":
    work()
