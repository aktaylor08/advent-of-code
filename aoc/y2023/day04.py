import math

from aoc import get_input


def parse_line(line: str) -> tuple[int, set[int], set[int]]:
    game_split = line.strip().split(":")
    game = int(game_split[0].split()[1])
    win_lose_split = game_split[1].split("|")
    winners = {int(x) for x in win_lose_split[0].strip().lstrip().split()}
    numbers = {int(x) for x in win_lose_split[1].strip().lstrip().split()}
    return game, winners, numbers


def work():
    sum1 = 0
    card_count = {}
    sum2 = 0
    for line in get_input(2023, 4).split("\n"):
        if line == "":
            continue
        game, win, num = parse_line(line)
        match_count = len(win & num)
        sum1 += int(math.pow(2, match_count - 1))
        num_cards = card_count.get(game, 1)
        sum2 += num_cards
        for x in range(game + 1, match_count + game + 1):
            card_count[x] = card_count.get(x, 1) + num_cards
    print(sum1)
    print(sum2)


if __name__ == "__main__":
    work()
