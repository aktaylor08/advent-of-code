import numpy as np
from aoc import get_input
import math


def go(time, record):
    tarr = np.arange(0, time + 1)
    return ((time - tarr) * tarr > record).sum()


def thing(time, record):
    min_time = math.ceil((time / 2) - (math.sqrt(time**2 - 4 * record) / 2))
    max_time = math.floor((time / 2) + (math.sqrt(time**2 - 4 * record) / 2))
    return max_time - min_time + 1


times, distance = get_input(2023, 6).strip().split("\n")
tlong = ""
dlong = ""
part1 = 1
part1_2 = 1
for t, d in zip(
    (int(x) for x in times.split(":")[1].strip().split()),
    (int(x) for x in distance.split(":")[1].strip().split()),
):
    part1 *= go(t, d)
    part1_2 *= thing(t, d)
    tlong += str(t)
    dlong += str(d)
print(part1)
print(part1_2)
print(go(int(tlong), int(dlong)))
print(thing(int(tlong), int(dlong)))
