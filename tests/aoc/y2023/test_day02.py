from aoc.y2023.day02 import line_to_info, get_min_set

import pytest


"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


@pytest.mark.parametrize(
    "line,exp_game,exp_turns",
    [
        [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            1,
            [{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}],
        ],
        [
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            2,
            [
                {"blue": 1, "green": 2},
                {"red": 1, "green": 3, "blue": 4},
                {"green": 1, "blue": 1},
            ],
        ],
    ],
)
def test_parse(line, exp_game, exp_turns):
    game_num, turns = line_to_info(line)
    assert game_num == exp_game
    assert exp_turns == turns


def test_min_set():
    min_set = get_min_set(
        [
            {"blue": 1, "green": 2},
            {"red": 1, "green": 3, "blue": 4},
            {"green": 1, "blue": 1},
        ]
    )
    assert min_set == {"red": 1, "blue": 4, "green": 3}
