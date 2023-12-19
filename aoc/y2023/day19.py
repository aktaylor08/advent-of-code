from aoc import get_input
import re


class Workflow:
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules

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

    def by_set(self, input_sets):
        result_sets = {}
        for rule in self.rules:
            if ":" not in rule:
                res_dict = {x: set(v) for x, v in input_sets.items()}
                result_sets[rule] = res_dict
            else:
                check, dest = rule.split(":")
                if "<" in rule:
                    left, right = check.split("<")
                    res_dict = {x: set(v) for x, v in input_sets.items()}
                    the_split = set(filter(lambda x: x < int(right), input_sets[left]))
                    res_dict[left] = the_split
                    input_sets[left] = input_sets[left] - the_split
                    result_sets[dest] = res_dict
                elif ">" in rule:
                    left, right = check.split(">")
                    res_dict = {x: set(v) for x, v in input_sets.items()}
                    the_split = set(filter(lambda x: x > int(right), input_sets[left]))
                    res_dict[left] = the_split
                    input_sets[left] = input_sets[left] - the_split
                    result_sets[dest] = res_dict
                else:
                    raise Exception("NO check in rule?")
        return result_sets


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


def part_2(workflows):
    start = 1
    end = 4001
    inputs = [
        (
            "in",
            {
                "x": set([x for x in range(start, end)]),
                "m": set([x for x in range(start, end)]),
                "a": set([x for x in range(start, end)]),
                "s": set([x for x in range(start, end)]),
            },
        )
    ]
    input_vals = {a[0] for a in inputs}
    while input_vals != set(["R", "A"]):
        next_inputs = []
        for w, to_compute in inputs:
            if w not in ["A", "R"]:
                worker = workflows[w]
                res = worker.by_set(to_compute)
            else:
                res = {w: to_compute}
            for dest in res:
                next_inputs.append((dest, res[dest]))
        inputs = next_inputs
        input_vals = {a[0] for a in inputs}
    print("-------")
    result = 1
    for x in inputs:
        if x[0] == "A":
            print(x[1])
            temp = 1
            for v in "xmas":
                temp *= len(x[1][v])
            result += temp
    print(result)


def main():
    input = get_input(2023, 19, 0)
    workflows, parts = input.split("\n\n")
    workflows = get_work(workflows)
    parts = get_parts(parts)
    process(workflows, parts)
    part_2(workflows)


if __name__ == "__main__":
    main()
