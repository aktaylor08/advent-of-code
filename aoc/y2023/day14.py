from aoc import get_input


def tilt_up(rocks: list[list[str]]) -> list[list[str]]:
    for col in range(len(rocks[0])):
        for row in range(len(rocks)):
            if rocks[row][col] in ["O", "#"]:
                continue
            for up in range(row + 1, len(rocks)):
                if rocks[up][col] == "#":
                    break
                if rocks[up][col] == "O":
                    rocks[row][col] = "O"
                    rocks[up][col] = "."
                    break
    return rocks


def tilt_down(rocks: list[list[str]]) -> list[list[str]]:
    rocks.reverse()
    tilt_up(rocks)
    rocks.reverse()
    return rocks

def pr(rest);
    for x in rest:
        print(x)

if __name__ == "__main__":
    input = [
        [c for c in "O....#...."],
        [c for c in "O.OO#....#"],
        [c for c in ".....##..."],
        [c for c in "OO.#O....O"],
        [c for c in ".O.....O#."],
        [c for c in "O.#..O.#.#"],
        [c for c in "..O..#O..O"],
        [c for c in ".......O.."],
        [c for c in "#....###.."],
        [c for c in "#OO..#...."],
    ]
    # input = [[c for c in x] for x in get_input(2023, 14).split("\n")][:-1]
    rest = tilt_up(input)
    pr(rest)
    sum1 = 0
    for i, x in enumerate(rest):
        sum1 += sum([r == "O" for r in x]) * (len(rest) - i)
    print(sum1)
