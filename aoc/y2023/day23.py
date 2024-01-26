from aoc import get_input
from enum import Enum
import graphviz


class Direction(Enum):
    up = 0
    down = 1
    left = 2
    right = 3


class Node:
    def __init__(self, start_row, start_col):
        self.children = {}
        self.weight = 0
        self.start_row = start_row
        self.start_col = start_col
        self.steps = []

    def add_child(self, row, col, weight):
        if self.start_row != row or col != self.start_col:
            self.children[(row, col)] = weight

    def __repr__(self):
        return f"({self.start_row}, {self.start_col}: {self.weight} -> {len(self.children)})"

    def __hash__(self):
        return hash((self.start_row, self.start_col))

    def __eq__(self, other):
        return self.start_row == other.start_row and self.start_col == other.start_col


def traverse(start, amap):
    start_node = Node(0, start)
    all_nodes = {(0, start): start_node}
    to_visit = [(start_node, 1, 0, start, set())]
    count = 0
    while to_visit:
        node, distance, row, col, visited = to_visit[0]
        to_visit = to_visit[1:]
        if (row, col) in visited:
            continue
        visited.add((row, col))
        node.steps.append((row, col))
        if row == len(amap) - 1:
            new_node = Node(row, col)
            end_node = new_node
            all_nodes[(row, col)] = new_node
            node.add_child(row, col, distance)
        for dr, dc, new_direct in [
            (1, 0, Direction.down),
            (-1, 0, Direction.up),
            (0, 1, Direction.right),
            (0, -1, Direction.left),
        ]:
            new_row = dr + row
            new_col = dc + col
            if 0 <= new_row < len(amap) and 0 <= new_col < len(amap[0]):
                if (new_row, new_col) in visited:
                    if (new_row, new_col) in all_nodes:
                        if (new_row, new_col) != (0, start):
                            node.add_child(new_row, new_col, distance)
                elif "#" == amap[new_row][new_col]:
                    pass
                elif amap[new_row][new_col] == ".":
                    to_visit.append(
                        (node, distance + 1, new_row, new_col, set(visited))
                    )
                else:
                    char = amap[new_row][new_col]
                    if cango(char, new_direct):
                        count += 1
                        new_node = Node(new_row, new_col)
                        all_nodes[(new_row, new_col)] = new_node
                        node.add_child(new_row, new_col, distance)
                        to_visit.append((new_node, 1, new_row, new_col, set(visited)))
    return start_node, end_node, all_nodes


def cango(char: str, direct: Direction):
    to_ret = False
    if direct == Direction.left and char == "<":
        to_ret = True
    if direct == Direction.right and char == ">":
        to_ret = True
    if direct == Direction.up and char == "^":
        to_ret = True
    if direct == Direction.down and char == "v":
        to_ret = True
    return to_ret


def sort(nodes):
    in_order = []
    visited = set()

    def visit(node, sorted_nodes, visited):
        if node not in visited:
            visited.add(node)
            for child in node.children:
                if child not in visited:
                    visit(child, sorted_nodes, visited)
                sorted_nodes.append(child)

    for node in nodes:
        visit(node, in_order, visited)
    return [nodes[0]] + in_order[::-1]


def build_graph(instuff):
    lines = instuff.split("\n")
    start = lines[0].find(".")
    start, end, allthem = traverse(start, lines)
    dot = graphviz.Digraph()
    degree = {}
    for row, col in allthem:
        x = allthem[(row, col)]
        node_name = f"{x.start_row}, {x.start_col}"
        dot.node(node_name, node_name)
        for row, col in x.children:
            dist = x.children[(row, col)]
            if (row, col) in degree:
                degree[(row, col)] += 1
            else:
                degree[(row, col)] = 1
            dot.edge(
                node_name,
                f"{row}, {col}",
                label=str(dist),
            )
    dot.render()
    do_work(allthem, start, degree, end)


def do_work(allthem, start, degree, end):
    # Do topo sort
    queue = [(start.start_row, start.start_col)]
    sorted_nodes = []
    while queue:
        u = queue[0]
        queue = queue[1:]
        sorted_nodes.append(u)
        for vert_key in allthem[u].children:
            degree[vert_key] -= 1
            if degree[vert_key] == 0:
                queue.append(vert_key)
    dist = {x: -99999999999999 for x in sorted_nodes}
    dist[(start.start_row, start.start_col)] = 0
    for idx in range(len(dist)):
        vert = sorted_nodes[idx]
        node = allthem[vert]
        for child in node.children:
            if dist[child] < dist[vert] + node.children[child]:
                dist[child] = dist[vert] + node.children[child]
    print(dist[(end.start_row, end.start_col)] - 1)


def main():
    with open("input.txt") as f:
        build_graph(get_input(2023, 23).strip())


if __name__ == "__main__":
    main()
