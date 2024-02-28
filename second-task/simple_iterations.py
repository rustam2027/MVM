import math


def get_iterations(start_delta, delta, der: float) -> int:
    return math.ceil(math.log(start_delta/delta)/(-math.log(der)))


def simple_iterations(func, initial: float, amount: int) -> float | None:
    previous = initial
    for _ in range(amount):
        new = func(previous)
        previous = new
    return previous


def func(x: float) -> float:
    return math.tan(x) - x


if __name__ == "__main__":
    print(get_iterations(2, 0.001, 0.2))
    print(simple_iterations(func, 0.785, get_iterations(2, 0.001, 0.2)))
