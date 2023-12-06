import numpy as np
from aoc import get_input


def go(time, record):
    tarr = np.arange(0, time + 1)
    return ((time - tarr) * tarr > record).sum()


times, distance = get_input(2023, 6).strip().split("\n")
tlong = ""
dlong = ""
part1 = 1
for t, d in zip(
    (int(x) for x in times.split(":")[1].strip().split()),
    (int(x) for x in distance.split(":")[1].strip().split()),
):
    part1 *= go(t, d)
    tlong += str(t)
    dlong += str(d)
print(part1)
print(go(int(tlong), int(dlong)))
