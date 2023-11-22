from advent2022.day9 import Rope, Dir
import pytest


def test_move_head():
    r = Rope()
    r.move(Dir.left)
    r.move(Dir.left)
    r.move(Dir.left)
    assert r.current_loc[0] == (-3, 0)
    r.move(Dir.up)
    r.move(Dir.up)
    assert r.current_loc[0] == (-3, 2)
    r.move(Dir.down)
    r.move(Dir.right)
    r.move(Dir.right)
    r.move(Dir.right)
    r.move(Dir.right)
    assert r.current_loc[0] == (1, 1)
    r.move(Dir.down_right)
    r.move(Dir.down_right)
    assert r.current_loc[0] == (3, -1)


@pytest.mark.parametrize(
    "movement,tail_loc",
    [
        [[Dir.up, Dir.up], (0, 1)],
        [[Dir.down, Dir.down], (0, -1)],
        [[Dir.left, Dir.left], (-1, 0)],
        [[Dir.right, Dir.right], (1, 0)],
        [[Dir.right, Dir.up], (0, 0)],
        [[Dir.right, Dir.up, Dir.right], (1, 1)],
        [[Dir.right, Dir.up, Dir.up], (1, 1)],
        [[Dir.left, Dir.down, Dir.down], (-1, -1)],
    ],
)
def test_tail(movement, tail_loc):
    r = Rope()
    for x in movement:
        r.move(x)
    assert tail_loc == r.current_loc[1]


def test_count():
    r = Rope()
    for way, count in [
        (Dir.right, 4),
        (Dir.up, 4),
        (Dir.left, 3),
        (Dir.down, 1),
        (Dir.right, 4),
        (Dir.down, 1),
        (Dir.left, 5),
        (Dir.right, 2),
    ]:
        r.go(way, count)
    print(sorted(r.tail_locs))
    assert len(r.tail_locs) == 13
