from aoc.y2023.day19 import Workflow, parse_rule, get_parts


def test_aworkflow():
    funcs = ["x>10:one", "m<20:two", "a>30:R", "A"]
    w = Workflow("test", funcs)
    assert w.process({"x": 14, "m": 10, "a": 32}) == "one"
    assert w.process({"x": 1, "m": 10, "a": 32}) == "two"
    assert w.process({"x": 1, "m": 40, "a": 32}) == "R"
    assert w.process({"x": 1, "m": 40, "a": 0}) == "A"


def test_parse_rulez():
    in1 = "px{a<2006:qkq,m>2090:A,rfg}"
    w = parse_rule(in1)
    assert w.name == "px"
    assert w.rules == ["a<2006:qkq", "m>2090:A", "rfg"]
    in2 = "pv{a>1716:R,A}"
    w = parse_rule(in2)
    assert w.name == "pv"
    assert w.rules == ["a>1716:R", "A"]


def test_parse_parts():
    stuff = "{x=787,m=2655,a=1222,s=2876}\n{x=1679,m=44,a=2067,s=496}"
    parts = get_parts(stuff)
    assert len(parts) == 2
    assert parts[0]["x"] == 787
    assert parts[1]["x"] == 1679
