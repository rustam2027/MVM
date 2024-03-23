from typing import List
from math import cos, pi


def omega(roots: List[float], x):
    result = 1
    for root in roots:
        result *= x - root
    return result


def omega_num(roots: List[float], root: float):
    result = 1
    for root_i in roots:
        if (root == root_i):
            continue
        result *= (root - root_i)
    return result


def get_lagrange(roots: List[float], values: List[float]):
    def f(x):
        result = 0
        for index in range(len(roots)):
            result += values[index] * omega(roots, x) / (
                (x - roots[index]) * omega_num(roots, roots[index]))
        return result
    return f


if __name__ == "__main__":
    n = int(input("Введите число точек интерполяции: "))
    distrib = int(input(
        "Введите 1 для равномерного распределение узлов и 2 для распределения по корням Чебышева\n"))

    if distrib == 1:
        roots = [((2 * i / n) - 1) for i in range(n)]
    else:
        roots = [cos(((2 * k + 1) / (2 * n)) * pi) for k in range(n)]

    values = [1 / (1 + 25 * root ** 2) for root in roots]

    f = get_lagrange(roots, values)

    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    x = np.linspace(-1, 1, 200)

    interpolate_values = [f(i) for i in x]
    function_values = [1 / (1 + 25 * i ** 2) for i in x]
    difference_values = [abs(interpolate_values[i] - function_values[i])
                         for i in range(len(interpolate_values))]

    ax.plot(x, interpolate_values, label="Полином Лагранжа")
    ax.plot(x, function_values, label="Функция")
    ax.plot(x, difference_values, label="Разность")
    ax.scatter(roots, values)

    if distrib == 1:
        ax.set_title("Равномерное")
    else:
        ax.set_title("Чебышев")

    plt.legend()
    plt.show()
