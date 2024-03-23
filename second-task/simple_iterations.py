import math


def simple_iterations(isol: tuple, delta: float, root_num: int) -> float | None:
    delta *= 0.1  # Так лучше
    if (isol[0] <= 0):
        initial = isol[0]
    else:
        initial = isol[1]

    lamb = 1 / (1 / math.cos(initial) ** 2 - 1)

    def fi(x):
        if root_num == 0:
            return math.tan(x) * 0.0001
        return x - lamb * (math.tan(x) - x)

    previous = initial
    next = fi(initial)

    counter = 0
    while abs(previous - next) > delta:
        previous, next = next, fi(next)
        counter += 1

    return previous, counter


if __name__ == "__main__":
    print(simple_iterations(-4.56, 0.00001, -1))
