import math


def get_isolation(n: int):
    if n == 0:
        return (-0.5, 0.5)
    if n > 0:
        return (math.pi * n + 1, math.pi * (n + 1) - 1)
    if n < 0:
        return (math.pi * (n - 1) + 1, math.pi * n - 1)


def func(x):
    return math.tan(x) - x


def get_aprox(func, isolation: tuple):
    l, r = isolation
    shift = 0.001
    while (func(l + shift) > 0):
        l += shift
    while (func(l + shift) < -2):
        l += shift

    while (func(r - shift) < 0):
        r -= shift
    while (func(r - shift) > 2):
        r -= shift
    return (l, r)


def f(x):
    return math.tan(x) - x


if __name__ == "__main__":
    print(get_aprox(f, get_isolation(-1)))
