import math


def newton(func, func_der, start: float, root: float, delta: float) -> float | None:
    previous = start
    counter = 0
    while abs(previous - root) > delta:
        previous = previous - func(previous)/func_der(previous)
        counter += 1
        print(previous)
    return previous, counter


def func(x: float):
    return math.tan(x) - x


def func_der(x: float):
    return 1/((math.cos(x)) ** 2) - 1


if __name__ == "__main__":
    print(newton(func, func_der, 1, 0, 0.0001))
