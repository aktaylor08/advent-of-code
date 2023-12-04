import math

from aoc import get_input


class MapSquare:
    def __init__(self, height):
        self.distance = math.inf
        self.height = height
        self.parent = None
        self.finished = False


class ElfMap:
    def __init__(self):
        self.map: dict[tuple[int, int], MapSquare] = {}
        self.start = None
        self.target = None
        self.queue = []

    def parse(self, input):
        for row, line in enumerate(input.split("\n")):
            for column, height in enumerate(line):
                square = MapSquare(height)
                if height == "S":
                    self.start = (row, column)
                    square.distance = 0
                    square.finished = True
                    self.queue.append((row, column))
                if height == "E":
                    self.target = (row, column)
                self.map[(row, column)] = square

    def can_travel(self, square1: MapSquare, square2: MapSquare):
        ret = False
        if square1.height == "S":
            if square2.height == "a":
                ret = True
        elif square2.height == "E":
            if square1.height == "z":
                ret = True
        else:
            if ord(square2.height) - ord(square1.height) < 2:
                ret = True
        return ret

    def work(self):
        while self.queue:
            key = self.queue[0]
            row, col = key
            self.queue = self.queue[1:]
            cur_square = self.map[key]
            if key == self.target:
                return
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                n_key = (row + dr, col + dc)
                if n_key in self.map:
                    neighbor = self.map[n_key]
                    # Can I get there
                    if not neighbor.finished:
                        if self.can_travel(cur_square, neighbor):
                            neighbor.finished = True
                            neighbor.parent = key
                            neighbor.distance = cur_square.distance + 1
                            self.queue.append(n_key)


def main():
    m = ElfMap()
    amap = get_input(2022, 12)
    m.parse(amap)
    m.work()
    print(m.map[m.target].distance)


if __name__ == "__main__":
    main()
