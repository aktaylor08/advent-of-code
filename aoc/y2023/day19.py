from aoc import get_input
import re
import math


class Workflow:
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules

    def get_dests(self, minv, maxv):
        chain = []
        to_ret = {}
        for arule in self.rules:
            if ":" not in arule:
                to_ret[arule] = chain
            else:
                check, dest = arule.split(":")
                if "<" in check:
                    left, right = check.split("<")
                    happy = chain[:] + [(left, minv, int(right))]
                    to_ret[dest] = happy
                    chain.append((left, int(right), maxv + 1))
                elif ">" in check:
                    left, right = check.split(">")
                    happy = chain[:] + [(left, int(right) + 1, maxv + 1)]
                    to_ret[dest] = happy
                    chain.append((left, minv, int(right) + 1))
        return to_ret

    def process(self, part):
        for rule in self.rules:
            if ":" not in rule:
                return rule
            else:
                check, dest = rule.split(":")
                if "<" in rule:
                    left, right = check.split("<")
                    if part[left] < int(right):
                        return dest

                elif ">" in rule:
                    left, right = check.split(">")
                    if part[left] > int(right):
                        return dest
                else:
                    raise Exception("NO check in rule?")
        return None


def parse_rule(aline: str) -> Workflow:
    name, rest = aline.split("{")
    rules = [x for x in rest.strip()[:-1].split(",")]
    return Workflow(name, rules)


def get_work(workflows):
    result = {}
    for x in workflows.split("\n"):
        w = parse_rule(x.strip())
        result[w.name] = w
    return result


def get_parts(input_str) -> list[dict[str, int]]:
    parts = []
    for aline in input_str.strip().split("\n"):
        thing = {}
        for pair in aline[1:-1].split(","):
            k, v = pair.split("=")
            thing[k] = int(v)
        parts.append(thing)
    return parts


def process(workflows: dict[str, Workflow], inparts: list[dict[str, int]]):
    sum1 = 0
    for part in inparts:
        wf = "in"
        while wf not in ["R", "A"]:
            worker = workflows[wf]
            wf = worker.process(part)
        if wf == "A":
            sum1 += part["x"]
            sum1 += part["m"]
            sum1 += part["a"]
            sum1 += part["s"]
    return sum1


def calc2(conditions, input_set, minv, maxv):
    the_sum = 0
    ranges = {x: set() for x in input_set}
    for a_ending in conditions:
        pos = {k: list(range(minv, maxv + 1)) for k in input_set}
        for key, min_r, max_r in a_ending:
            if key is None:
                continue
            else:
                pos[key] = list(
                    filter(lambda x: int(min_r) <= x < int(max_r), pos[key])
                )
        for x in pos:
            ranges[x] = ranges[x] | set(pos[x])
            print(len(ranges[x]))
    print(the_sum)


def part_2(workflows, input_set="xy", minv=1, maxv=10):
    queue = [("in", [])]
    visited = set()
    conditions = []
    while len(queue) > 0:
        cur, tests = queue[0]
        queue = queue[1:]
        if cur not in ["A", "R"]:
            worker = workflows[cur]
            for dest, funcs in worker.get_dests(minv, maxv).items():
                if dest not in visited:
                    queue.append((dest, tests[:] + funcs))
            visited.add(cur)
        elif cur == "A":
            conditions.append(tests)
        elif cur != "R":
            print("WHY")
    calc2(conditions, input_set, minv, maxv)


def main():
    input = get_input(2023, 19, 0)
    workflows, parts = input.split("\n\n")
    workflows = get_work(workflows)
    parts = get_parts(parts)
    part_2(workflows, input_set="xmas", minv=1, maxv=4000)


if __name__ == "__main__":
    main()
