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

    def split_ranges(self, inputs):
        outputs = {}
        still_valid = inputs
        for arule in self.rules:
            if ":" not in arule:
                outputs[arule] = still_valid
            else:
                check, dest = arule.split(":")
                if "<" in check:
                    left, right = check.split("<")
                    valid = still_valid[left]
                    good_range = (valid[0], int(right))
                    rest_range = (int(right), valid[1])
                    new_dict = dict(**still_valid)
                    new_dict[left] = good_range
                    outputs[dest] = new_dict
                    still_valid[left] = rest_range
                elif ">" in check:
                    left, right = check.split(">")
                    valid = still_valid[left]
                    good_range = (int(right) + 1, valid[1])
                    rest_range = (valid[0], int(right))
                    new_dict = dict(**still_valid)
                    new_dict[left] = good_range
                    outputs[dest] = new_dict
                    still_valid[left] = rest_range
        return outputs

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


def part_2point2(workflows, input_set="xy", minv=1, maxv=10):
    input_ranges = {x: (minv, maxv) for x in input_set}
    input_things = [("in", input_ranges, [], 0)]
    sum = 0
    ranges = []
    while input_things:
        w, in_data, path, depth = input_things[0]
        print(depth)
        input_things = input_things[1:]
        if w not in ["R", "A"]:
            worker = workflows[w]
            for dest, inputs in worker.split_ranges(in_data).items():
                input_things.append((dest, inputs, path[:] + [w], depth + 1))
        elif w == "A":
            temp = 1
            print(depth, path)
            for x in in_data:
                print("\t", x, in_data[x])
            for k, (minv, maxv) in in_data.items():
                print(maxv - minv)
                temp = temp * (maxv - minv + 1)
            ranges.append(temp)
            sum += temp
    print(ranges)
    print(sum)


def main():
    input = get_input(2023, 19, 0)
    workflows, parts = input.split("\n\n")
    workflows = get_work(workflows)
    parts = get_parts(parts)
    part_2point2(workflows, input_set="xmas", minv=1, maxv=4000)
    workflows = {
        "in": Workflow("in", ["x<5:one", "two"]),
        "one": Workflow("in", ["y>7:A", "R"]),
        "two": Workflow("in", ["y<3:A", "R"]),
    }


if __name__ == "__main__":
    main()
