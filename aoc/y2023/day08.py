from aoc import get_input, sample_input


def parse_input(input: str) -> tuple[set[str], list[str], dict[str, tuple[str, str]]]:
    """
    Return list of RLRLRLRLRLRL
    and name, left, right tuple for steps
    """
    lines = input.split("\n\n")
    commands = lines[0][:]
    nodes = {}
    starts = set()
    for x in lines[1].split("\n"):
        if x != "":
            name, goto = x.strip().split("=")
            left, right = goto.split(",")
            nodes[name.strip()] = (left.lstrip()[1:], right.strip()[:-1])
            if name.strip()[-1] == "A":
                starts.add(name.strip())
    return starts, commands, nodes


def done(values: set[str]) -> bool:
    for x in list(values):
        if x[-1] != "Z":
            return False
    return True


def travel_1(current, commands, nodes):
    idx = 0
    while not done(current):
        if idx % 1_000_000 == 0:
            print(idx)
        new_current = set()
        for c in current:
            targets = nodes[c]
            cmd = commands[idx % len(commands)]
            if cmd == "L":
                c = targets[0]
            else:
                c = targets[1]
            new_current.add(c)
        current = new_current
        idx += 1
    return idx


if __name__ == "__main__":
    starts, commands, nodes = parse_input(get_input(2023, 8))
    print(travel_1(set(["AAA"]), commands, nodes))
    print(travel_1(starts, commands, nodes))
