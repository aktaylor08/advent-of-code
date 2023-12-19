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
    print(sum1)


def main():
    input = get_input(2023, 19)
    workflows, parts = input.split("\n\n")
    workflows = get_work(workflows)
    parts = get_parts(parts)
    process(workflows, parts)


if __name__ == "__main__":
    main()
