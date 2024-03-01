import math


def simple_iterations(func, initial: float, root: float, delta: float) -> float | None:
    previous = initial
    counter = 0
    while abs(previous - root) > delta:
        counter += 1
        new = func(previous)
        previous = new

    return previous, counter


def func(x: float) -> float:
    return math.tan(x)


if __name__ == "__main__":
    print(simple_iterations(func, 1, 0, 0.001))
