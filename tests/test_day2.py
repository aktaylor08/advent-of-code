import pytest
from advent2022.day2 import outcome, Choice, parse_line, score_game


@pytest.mark.parametrize(
    "p1,p2,res",
    [
        [Choice.Scissors, Choice.Scissors, 3],
        [Choice.Scissors, Choice.Paper, 6],
        [Choice.Scissors, Choice.Rock, 0],
        [Choice.Rock, Choice.Scissors, 6],
        [Choice.Rock, Choice.Paper, 0],
        [Choice.Rock, Choice.Rock, 3],
        [Choice.Paper, Choice.Scissors, 0],
        [Choice.Paper, Choice.Paper, 3],
        [Choice.Paper, Choice.Rock, 6],
    ],
)
def test_win(p1, p2, res):
    assert res == outcome(p1, p2)


@pytest.mark.parametrize(
    "line,choices",
    [
        ["A Y", (Choice.Rock, Choice.Paper)],
        ["B X", (Choice.Paper, Choice.Rock)],
        ["C Z", (Choice.Scissors, Choice.Scissors)],
    ],
)
def test_parse(line, choices):
    assert parse_line(line) == choices


@pytest.mark.parametrize(
    "choices,score",
    [
        [(Choice.Rock, Choice.Paper), 1],
        [(Choice.Paper, Choice.Rock), 8],
        [(Choice.Scissors, Choice.Scissors), 6],
    ],
)
def test_score(choices, score):
    assert score_game(choices) == score
