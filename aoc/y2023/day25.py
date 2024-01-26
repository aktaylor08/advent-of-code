from aoc import get_input
import graphviz


def main():
    nodes = set()
    connections = set()
    bad_connections = [
        tuple(sorted(v)) for v in [["vnm", "qpp"], ["rhk", "bff"], ["vkp", "kfr"]]
    ]
    for x in get_input(2023, 25).strip().split("\n"):
        one_side, others = x.split(":")
        nodes.add(one_side)
        for wire in others.strip().lstrip().split():
            thing = tuple(sorted([one_side, wire]))
            nodes.add(wire)
            if thing not in bad_connections:
                connections.add(thing)

    dot = graphviz.Graph(engine="neato")
    agraph = {}
    for x in nodes:
        dot.node(x, x)
        agraph[x] = []
    for one, two in connections:
        agraph[two].append(one)
        agraph[one].append(two)
        dot.edge(one, two)
    visited = set()
    to_visit = [list(nodes)[0]]
    while to_visit:
        node = to_visit[0]
        to_visit = to_visit[1:]
        visited.add(node)
        for new_node in agraph[node]:
            if new_node not in visited:
                to_visit.append(new_node)
    dot.render()
    print(len(visited))
    print(len(visited) * (len(agraph) - len(visited)))


if __name__ == "__main__":
    main()
