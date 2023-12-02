import math
import heapq


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
        self.heap = []

    def parse(self, input):
        for row, line in enumerate(input.split("\n")):
            for column, height in enumerate(line):
                square = MapSquare(height)
                if height == "S":
                    self.start = (row, column)
                    square.distance = 0
                    square.height = ")"
                    self.heap = [(0, (row, column))]
                if height == "E":
                    self.target = (row, column)
                    square.height = ")"
                self.map[(row, column)] = square

    def work(self):
        while self.heap:
            d, (row, col) = heapq.heappop(self.heap)
            key = (row, col)
            cur_square = self.map[key]
            if cur_square.finished:
                continue
            cur_square.finished = True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                n_key = (row + dr, col + dc)
                if n_key in self.map:
                    neighbor = self.map[n_key]
                    # Can I get there
                    if (
                        ord(neighbor.height) - ord(cur_square.height) < 2
                        or key == self.start
                        or (n_key == self.target and cur_square.height == "z")
                    ):
                        new_d = d + 1
                        if new_d < neighbor.distance:
                            print(
                                cur_square.height,
                                neighbor.height,
                                ord(neighbor.height) - ord(cur_square.height),
                            )
                            neighbor.parent = key
                            neighbor.distance = new_d
                            heapq.heappush(self.heap, (new_d, n_key))


def main():
    m = ElfMap()
    amap = """Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi\n"""
    m.parse(amap)
    m.work()
    print(m.map[m.target].distance)
    print(m.map[m.target].parent)
    current = m.target
    while current != m.start:
        print(current)
        current = m.map[current].parent


if __name__ == "__main__":
    main()
