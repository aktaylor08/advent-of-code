from aoc import get_input

from abc import ABC


class Module(ABC):
    name: str

    def get_name(self):
        return self.name

    def handle(self, from_mod: str, sig: int, round: int) -> list[tuple[str, str, int]]:
        raise Exception("Not implemented")


class Broadcaster(Module):
    def __init__(self, dests: list[str]):
        self.dests = dests
        self.name = "broadcaster"

    def handle(self, from_mod: str, sig: int, round: int):
        return [(self.name, x, sig) for x in self.get_dest()]

    def get_dest(self) -> list[str]:
        return self.dests

    def __repr__(self):
        return f"{self.name} -> {self.dests}"


class FlipFlop(Module):
    def __init__(self, name, dest):
        self.name = name
        self.dest = dest
        self.on = False

    def handle(self, from_mod: str, sig: int, round: int):
        rev_val = []
        to_send = None
        if sig == 0:
            if self.on:
                self.on = False
                to_send = 0
            else:
                self.on = True
                to_send = 1
        if to_send is not None:
            for adest in self.dest:
                rev_val.append((self.name, adest, to_send))
        return rev_val

    def __repr__(self):
        return f"{self.name} -> {list(self.dest)}"


class Noop(Module):
    def __init__(self, name):
        self.name = name
        self.count = 0

    def handle(self, from_mod: str, sig: int, round: int):
        if sig == 0:
            self.count += 1
        return []


class Conjunction(Module):
    def __init__(self, name, dest):
        self.name = name
        self.dest = dest
        self.inputs = {}
        self.names = []
        self.seen_at = {}

    def add_input(self, name):
        self.inputs[name] = 0
        self.names.append(name)

    def handle(self, from_mod: str, sig: int, round: int):
        to_ret = []
        if from_mod not in self.inputs:
            raise Exception("not there")
        self.inputs[from_mod] = sig
        vals = tuple([self.inputs[x] for x in self.names])
        if vals not in self.seen_at:
            print(round, vals)
            self.seen_at[vals] = round
        for adest in self.dest:
            if all(self.inputs.values()):
                to_ret.append((self.name, adest, 0))
            else:
                to_ret.append((self.name, adest, 1))
        return to_ret

    def __repr__(self):
        return f"{self.name} -> {self.dest}:  {self.inputs}"


def wire(sender: Module, rec: Module):
    print(f"Wiring {sender}, {rec}")
    if isinstance(rec, Conjunction):
        rec.add_input(sender.name)


def search_flops(the_map, nodes):
    flops = []
    path = ["broadcaster"]
    paths = {}
    seen = set()
    queue = [("broadcaster", 0, path)]
    while queue:
        node, dist, path = queue[0]
        paths[node] = path
        queue = queue[1:]
        if isinstance(nodes[node], FlipFlop):
            flops.append(nodes[node])
        for x in the_map.get(node, []):
            if x not in seen:
                queue.append((x, dist + 1, path[:] + [node]))
        seen.add(node)
    return flops, paths


def main():
    the_map = {}
    modules = {}
    alldests = set()
    for line in get_input(2023, 20).strip().split("\n"):
        thing = None
        name, dest_v = line.split(" -> ")
        if name != "broadcaster":
            name = name.lstrip().rstrip()[1:]
        dests = [x.lstrip().strip() for x in dest_v.strip().split(",")]
        if line.startswith("broadcaster"):
            thing = Broadcaster(dests)
            the_map[name] = dests
        elif line.startswith("%"):
            thing = FlipFlop(name, dests)
            the_map[name] = dests
        elif line.startswith("&"):
            thing = Conjunction(name, dests)
            the_map[name] = dests
        else:
            raise Exception("Bad line")
        modules[name] = thing
        alldests.update(dests)
    for x in alldests:
        if x not in modules:
            modules[x] = Noop(x)
            the_map[x] = []
    for key, value in the_map.items():
        for rec in value:
            wire(modules[key], modules[rec])
    lows = 0
    highs = 0
    print("Starting iter\n\n")
    cycle = 0
    flops, paths = search_flops(the_map, modules)
    print(paths["rx"])
    conjuncs = [modules[x] for x in paths["rx"] if isinstance(modules[x], Conjunction)]
    print(conjuncs)
    while modules["rx"].count == 0:
        cycle += 1
        queue = [("button", "broadcaster", 0)]
        while len(queue) > 0:
            from_mod, dest, sig = queue[0]
            if sig:
                highs += 1
            else:
                lows += 1
            queue = queue[1:]
            rec = modules[dest]
            results = rec.handle(from_mod, sig, cycle)
            for x in results:
                queue.append(x)
        if cycle == 1000:
            print(lows * highs)
        if cycle % 1_000_000 == 0:
            for x in conjuncs:
                print(x.seen_at)


if __name__ == "__main__":
    main()
