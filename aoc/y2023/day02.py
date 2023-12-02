from pyrsistent import get_in
from aoc import get_input


def line_to_info(line: str) -> tuple[int, list[dict[str, int]]]:
    results = []

    split_line = line.split(":")
    game_num = int(split_line[0].split()[1])
    for games_splt in split_line[1].split(";"):
        result = {}
        for entry in games_splt.split(","):
            num, key = entry.split()
            result[key] = int(num)
        results.append(result)
    return game_num, results


def get_min_set(games: list[dict[str, int]]):
    big_set = {}
    for game in games:
        for key, value in game.items():
            if key not in big_set:
                big_set[key] = value
            else:
                big_set[key] = max(big_set[key], value)
    return big_set


def main():
    limits = {"red": 12, "green": 13, "blue": 14}
    aoc_in = get_input(2023, 2)
    bad_games = set()
    all_games = 0
    total_2 = 0
    for line in aoc_in.split("\n"):
        if len(line) < 1:
            continue
        game, info = line_to_info(line)
        all_games += game
        for result in info:
            for color, value in result.items():
                if color not in limits or value > limits[color]:
                    bad_games.add(game)
        total = 1
        for x in get_min_set(info).values():
            total *= x
        total_2 = total + total_2
    print(all_games - sum(bad_games))
    print(total_2)


if __name__ == "__main__":
    main()
