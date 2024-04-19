from typing import Tuple
from math import sin, pi, e, log
from scipy import integrate
import matplotlib.pyplot as plt


def evaluate(n: int, func, interval: Tuple[float, float]):
    N = 2 * n
    a, b = interval
    h = (b - a) / N

    integral = 0
    for i in range(1, N, 2):
        integral += func(a + (i - 1) * h) + 4 * \
            func(a + i * h) + func(a + (i + 1) * h)
    return h / 3 * integral


def func1(x: float):
    if x == 0:
        return pi
    if x == 1:
        return 5 * pi
    return sin(pi * x ** 5) / (x ** 5 * (1 - x))


def func2(x: float):
    return x ** 3


def func3(x: float):
    return e ** (-1 * (x / (1 - x))) * sin((x / (1 - x)) / 10) / (1 - x) ** 2


def get_order(func, interval: Tuple[float, float], n: int, r: int):
    return (evaluate(n, func, interval) - evaluate(n * r, func, interval)) / ((1 / r) ** 4 - 1)


if __name__ == "__main__":
    func = func2
    ax, fig = plt.subplots()

    x_values = []
    y_values = []

    # for i in range(4, 5):
    #     x_values.append(i)
    #     y_values.append(evaluate(10 ** i, func, (0, 1)))
    # fig.plot(x_values, y_values)

    print(integrate.quad(func, 0, 1))
    print(evaluate(10**4, func, (0, 1)))
    A = get_order(func, (0, 1), 10, 10)
    B = get_order(func, (0, 1), 100, 10)
    print(A)
    print(B)
    print(A/B)
    print(B/A)
    print(log(10, abs(B/A)))
    # plt.show()
