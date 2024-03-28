import numpy as np
import matplotlib.pyplot as plt

from typing import List
from math import cos, pi, log


def omega(roots: List[float], x):
    result = 1
    for root in roots:
        result *= x - root
    return result


def omega_num(roots: List[float], root: float):
    result: float = 1
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


def get_results(n: int, distrib: int) -> tuple:
    match distrib:
        case 1:
            roots = [((2 * i / n) - (n - 1)/n) for i in range(n)]
        case 2:
            roots = [cos(((2 * k + 1) / (2 * n)) * pi) for k in range(n)]

    values = [1 / (1 + 25 * root ** 2) for root in roots]

    f = get_lagrange(roots, values)

    x = np.linspace(-1, 1, 200)

    interpolate_values = [f(i) for i in x]
    function_values = [1 / (1 + 25 * i ** 2) for i in x]
    difference_values = [abs(interpolate_values[i] - function_values[i])
                         for i in range(len(interpolate_values))]
    return interpolate_values, function_values, difference_values


def get_single():
    n = int(input("Введите число точек интерполяции: "))
    distrib = int(input(
        "Введите 1 для равномерного распределение узлов и 2 для распределения по корням Чебышева\n"))

    fig, ax = plt.subplots()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    x = np.linspace(-1, 1, 200)

    interpolate_values, function_values, difference_values = get_results(
        n, distrib)

    ax.plot(x, interpolate_values, label="Полином Лагранжа")
    ax.plot(x, function_values, label="Функция")
    ax.plot(x, difference_values, label="Разность")

    if distrib == 1:
        ax.set_title("Равномерное")
    else:
        ax.set_title("Чебышев")

    plt.legend()
    plt.show()


def get_graph():
    max_nodes = int(
        input("Введите максимальное количество узлов интерполяции: "))
    step = int(input("Введите шаг между узлами: "))
    distrib = int(input(
        "Введите 1 для равномерного распределение узлов и 2 для распределения по корням Чебышева\n"))

    nodes_range = range(2, max_nodes+1, step)
    max_errors = []

    for nodes in nodes_range:
        max_errors.append(log(max(get_results(nodes, distrib)[2]), 10))

    plt.plot(nodes_range, max_errors)
    plt.xlabel('Количество узлов интерполяции')
    plt.ylabel('Максимальная погрешность')
    plt.title(
        'Зависимость максимальной погрешности от количества узлов интерполяции')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    get_graph()
