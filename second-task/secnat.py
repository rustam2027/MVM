import math


def secnat(func, start1: float, start2: float, delta: float):
    previous = start1
    pre_previous = start2
    counter = 0
    while abs(pre_previous - previous) > delta:
        new = previous - func(previous) * (previous - pre_previous) / \
            (func(previous) - func(pre_previous))
        previous, pre_previous = new, previous
        counter += 1
    return new, counter


def func(x: float):
    return math.tan(x) - x
