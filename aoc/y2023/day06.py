import numpy as np


def go(time, record):
    tarr = np.arange(0, time + 1)
    return ((time - tarr) * tarr > record).sum()


a = go(44, 283) * go(70, 1134) * go(70, 1134) * go(80, 1491)
b = go(44707080, 283113411341491)
print(a)
print(b)
