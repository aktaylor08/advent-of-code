from aoc import get_input
import numpy as np
import matplotlib.pyplot as plt


def parse_hail(inputs):
    positions = []
    velocites = []
    for x in inputs.split("\n"):
        pos, vel = x.split(" @ ")
        positions.append([int(n.strip().lstrip()) for n in pos.split(",")])
        velocites.append([int(n.strip().lstrip()) for n in vel.split(",")])
    return np.array(positions), np.array(velocites)


def collide(start_one, start_two, end_one, end_two):
    p0_x = start_one[0]
    p1_x = end_one[0]
    p2_x = start_two[0]
    p3_x = end_two[0]

    p0_y = start_one[1]
    p1_y = end_one[1]
    p2_y = start_two[1]
    p3_y = end_two[1]

    s1_x = p1_x - p0_x
    s1_y = p1_y - p0_y
    s2_x = p3_x - p2_x
    s2_y = p3_y - p2_y

    s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / (-s2_x * s1_y + s1_x * s2_y)
    t = (s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / (-s2_x * s1_y + s1_x * s2_y)
    if s >= 0 and s <= 1 and t >= 0 and t <= 1:
        # Collision detected
        i_x = p0_x + (t * s1_x)
        i_y = p0_y + (t * s1_y)
        return True, i_x, i_y
    return False, None, None


def main():
    pos, vel = parse_hail(get_input(2023, 24).strip())
    start_pos = np.copy(pos)
    max_val = 400000000000000
    min_val = 200000000000000
    sim_go = True
    cycles = 0
    multiplier = (max_val - min_val) / 100_000
    multiplier = (max_val - min_val) / 100_000
    vel_multi = vel * multiplier
    while sim_go:
        cycles += 1
        xlow = min_val <= pos[:, 0]
        xhigh = pos[:, 0] <= max_val
        ylow = min_val <= pos[:, 1]
        yhigh = pos[:, 1] <= max_val
        sim_go = np.any(xlow & xhigh & ylow & yhigh)
        pos = pos + vel_multi
    print(cycles)
    cx = []
    cy = []
    for l_one in range(len(pos)):
        start_one = start_pos[l_one]
        end_one = pos[l_one]
        for l_two in range(l_one, len(pos)):
            start_two = start_pos[l_two]
            end_two = pos[l_two]
            c, x, y = collide(start_one, start_two, end_one, end_two)
            if c and min_val <= x <= max_val and min_val <= y <= max_val:
                cx.append(x)
                cy.append(y)
    stone_one = start_pos[1] - start_pos[0]
    vel_one = vel[1] - vel[0]
    stone_two = start_pos[2] - start_pos[0]
    vel_two = vel[2] - vel[0]
    time_two = solve_time(stone_one, stone_two, vel_one, vel_two)
    time_one = solve_time(stone_two, stone_one, vel_two, vel_one)
    pos_col_one = [
        stone_one[0] + time_one * vel_one[0],
        stone_one[1] + time_one * vel_one[1],
        stone_one[2] + time_one * vel_one[2],
    ]
    pos_col_two = [
        stone_two[0] + time_two * vel_two[0],
        stone_two[1] + time_two * vel_two[1],
        stone_two[2] + time_two * vel_two[2],
    ]
    dt = time_two - time_one
    dp = [
        pos_col_two[0] - pos_col_one[0],
        pos_col_two[1] - pos_col_one[1],
        pos_col_two[2] - pos_col_one[2],
    ]
    rock_vel = [
        dp[0] / dt,
        dp[1] / dt,
        dp[2] / dt,
    ]
    pos_start = [
        pos_col_one[0] - int(rock_vel[0] * time_one),
        pos_col_one[1] - int(rock_vel[1] * time_one),
        pos_col_one[2] - int(rock_vel[2] * time_one),
    ]
    print(pos_start)
    global_start = [
        pos_start[0] + int(start_pos[0][0]),
        pos_start[1] + int(start_pos[0][1]),
        pos_start[2] + int(start_pos[0][2]),
    ]
    print(global_start)
    print(sum(global_start))


def solve_time(stone_one, stone_two, vel_one, vel_two):
    stone_one = [int(x) for x in stone_one]
    stone_two = [int(x) for x in stone_two]
    vel_one = [int(x) for x in vel_one]
    vel_two = [int(x) for x in vel_two]
    other_stone_one = [a + b for a, b in list(zip(stone_one, vel_one))]
    N_vect = [
        stone_one[1] * other_stone_one[2] - stone_one[2] * other_stone_one[1],
        stone_one[2] * other_stone_one[0] - stone_one[0] * other_stone_one[2],
        stone_one[0] * other_stone_one[1] - stone_one[1] * other_stone_one[0],
    ]
    print(N_vect)
    top = sum(-a * b for a, b in list(zip(stone_two, N_vect)))
    bottom = sum(a * b for a, b in list(zip(vel_two, N_vect)))
    return int(top / bottom)


if __name__ == "__main__":
    main()
