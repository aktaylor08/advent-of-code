from aoc.y2022.day07 import Explorer
import pytest


@pytest.fixture
def example_input() -> list[str]:
    return [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]


def test_parsing(example_input):
    exp = Explorer()
    exp.process(example_input)
    exp.change_dir("/")
    assert len(exp.current.directorys) == 2
    assert len(exp.current.files) == 2
