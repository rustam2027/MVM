from typing import List, Tuple
import matplotlib.pyplot as plt
import math


def solve_tridioganal(lower_line: List[float], middle_line: List[float], upper_line: List[float], right_side: List[float]):
    a, b, c, d = lower_line.copy(), middle_line.copy(
    ), upper_line.copy(), right_side.copy()
    if not (len(a) == len(b) == len(c) == len(d)):
        raise TypeError()

    for i in range(len(a) - 1):
        b_i, c_i, d_i = b[i], c[i], d[i]
        d[i + 1] = d[i + 1] - (d_i / b_i) * a[i + 1]
        b[i + 1] = b[i + 1] - (c_i / b_i) * a[i + 1]
    # print(b, c)

    b[len(a) - 1] = d[len(a) - 1]/b[len(a) - 1]

    for i in range(len(a) - 2, -1, -1):
        b[i] = (d[i] - c[i] * b[i + 1]) / b[i]

    return b


def get_tridioganal(func, n: int, bounds: Tuple[float, float]):
    a, b, c = [0], [], []
    l, r = bounds
    h = (r - l) / n

    for i in range(1, n):
        a.append(1 / h ** 2)
        b.append(-2 / h ** 2)
        c.append(1 / h ** 2)
    c.append(0)

    d, grid = get_values(func, n, bounds)

    return a, b, c, d, grid


def get_values(func, n: int, bounds: Tuple[float, float]):
    l, r = bounds
    return [func(l + i * (r - l) / n) for i in range(1, n)], [l + i * (r - l) / n for i in range(1, n)]


def get_bound_values():
    print("Задайте краевые условия:")
    choice_l = int(input(
        "Чтобы задать левые граничные условия через производную введите 0 иначе введите 1: "))
    if choice_l == 0:
        left = float(input("Задайте значение производной в левой точке: "))
        left_array = [-1, 1, left]
    else:
        left = float(input("Задайте значение функции в левой точке: "))
        left_array = [1, 0, left]

    choice_r = int(input(
        "Чтобы задать правые граничные условия через производную введите 0 иначе введите 1: "))
    if choice_r == 0:
        right = float(input("Задайте значение производной в правой точке: "))
        right_array = [1, -1, right]
    else:
        right = float(input("Задайте значение функции в правой точке: "))
        right_array = [0, 1, right]

    return left_array, right_array


def test_1():
    A = [0, 6, 2]
    B = [2, 4, 8]
    C = [2, 8, 0]
    D = [1, 2, 3]
    assert solve_tridioganal(A, B, C, D) == [-0.5, 1, 0.125]


if __name__ == "__main__":
    test_1()
    n = int(input("Введите количество узлов: "))
    a, b, c, d, grid = get_tridioganal(math.cos, n, (-math.pi/2, math.pi/2))

    left_array, right_array = get_bound_values()

    b.insert(0, left_array[0])
    c.insert(0, left_array[1])
    d.insert(0, left_array[2])

    a.append(right_array[0])
    b.append(right_array[1])
    d.append(right_array[2])

    print(a)
    print(b)
    print(c)
    print(d)

    print(len(a), len(b), len(c), len(d))
    print(d)
    print(grid)

    result = solve_tridioganal(a, b, c, d)

    fig, ax = plt.subplots()
    print(result)
    grid = [-math.pi / 2] + grid + [math.pi / 2]

    # grid = [-math.pi / 2] + grid + [math.pi / 2]

    ax.plot(grid, [x - math.cos(x) - math.pi / 2 + 1 for x in grid])

    ax.plot(grid, result)
    ax.grid(True)
    fig.tight_layout()

    plt.show()
