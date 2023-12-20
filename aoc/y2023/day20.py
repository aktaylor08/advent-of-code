from aoc import get_input

from abc import ABC


class Module(ABC):
    name: str

    def get_name(self):
        return self.name

    def handle(self, from_mod: str, sig: int) -> list[tuple[str, str, int]]:
        raise Exception("Not implemented")


class Broadcaster(Module):
    def __init__(self, dests: list[str]):
        self.dests = dests
        self.name = "broadcaster"

    def handle(self, from_mod: str, sig: int):
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

    def handle(self, from_mod, sig):
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

    def handle(self, from_mod: str, sig: int):
        if sig == 0:
            self.count += 1
        return []


class Conjunction(Module):
    def __init__(self, name, dest):
        self.name = name
        self.dest = dest
        self.inputs = {}

    def add_input(self, name):
        print(f"Added input to {self.name} from {name}")
        self.inputs[name] = 0

    def handle(self, from_mod: str, sig: int):
        to_ret = []
        if from_mod not in self.inputs:
            raise Exception("not there")
        self.inputs[from_mod] = sig
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


def main():
    the_map = {}
    modules = {}
    alldests = set()
    for line in get_input(2023, 20).strip().split("\n"):
        thing = None
        name, dest_v = line.split(" -> ")
        if name != "broadcaster":
            name = name.lstrip().rstrip()[1:]
        print(name)
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
        print(name)
        modules[name] = thing
        alldests.update(dests)
    print(the_map)
    print(modules)
    print(alldests)
    for x in alldests:
        print(x)
        if x not in modules:
            modules[x] = Noop(x)
    for key, value in the_map.items():
        for rec in value:
            wire(modules[key], modules[rec])
    lows = 0
    highs = 0
    print("Starting iter\n\n")
    for i in range(1000):
        queue = [("button", "broadcaster", 0)]
        while len(queue) > 0:
            from_mod, dest, sig = queue[0]
            if sig:
                highs += 1
            else:
                lows += 1
            queue = queue[1:]
            print(f"{from_mod}--{sig}-->{dest}")
            rec = modules[dest]
            results = rec.handle(from_mod, sig)
            for x in results:
                queue.append(x)
    print(lows)
    print(highs)
    print(lows * highs)


if __name__ == "__main__":
    main()
