from matplotlib import pyplot as plt
from typing import Tuple, List
import math


def get_k_1(x: float, y: float, f, h: float) -> Tuple[float, float, float, float]:
    k1 = f(x, y)
    k2 = f(x + h/2, y + (h * k1) / 2)
    k3 = f(x + h/2, y + (h * k2) / 2)
    k4 = f(x + h, y + h * k3)

    return k1, k2, k3, k4


def get_k_2(t: float, x: float, y: float, f, g, h: float):
    k1 = (f(t, x, y), g(t, x, y))

    k2 = (f(t + h/2, x + (h * k1[0]) / 2, y + (h * k1[1]) / 2),
          g(t + h/2, x + (h * k1[0]) / 2, y + (h * k1[1]) / 2))

    k3 = (f(t + h/2, x + (h * k2[0]) / 2, y + (h * k2[1]) / 2),
          g(t + h/2, x + (h * k2[0]) / 2, y + (h * k2[1]) / 2))

    k4 = (f(t + h, x + h * k3[0], y + h * k3[1]),
          g(t + h, x + h * k3[0], y + h * k3[1]))

    return k1, k2, k3, k4


def get_k_3(t: float, x: float, y: float, z: float, f, g, q, h: float):
    k1 = (f(t, x, y, z), g(t, x, y, z), q(t, x, y, z))

    k2 = (f(t + h/2, x + (h * k1[0]) / 2, y + (h * k1[1]) / 2, z + (h * k1[2]) / 2),
          g(t + h/2, x + (h * k1[0]) / 2, y +
            (h * k1[1]) / 2, z + (h * k1[2]) / 2),
          q(t + h/2, x + (h * k1[0]) / 2, y + (h * k1[1]) / 2, z + (h * k1[2]) / 2))

    k3 = (f(t + h/2, x + (h * k2[0]) / 2, y + (h * k2[1]) / 2, z + (h * k2[2]) / 2),
          g(t + h/2, x + (h * k2[0]) / 2, y +
            (h * k2[1]) / 2, z + (h * k2[2]) / 2),
          q(t + h/2, x + (h * k2[0]) / 2, y + (h * k2[1]) / 2, z + (h * k2[2]) / 2))

    k4 = (f(t + h, x + h * k3[0], y + h * k3[1], z + h * k3[2]),
          g(t + h, x + h * k3[0], y + h * k3[1], z + h * k3[2]),
          q(t + h, x + h * k3[0], y + h * k3[1], z + h * k3[2]))

    return k1, k2, k3, k4


def draw_func(fig, ax, arr_values: List[float], arr_dots: List[float], name: str) -> None:
    ax.plot(arr_dots, arr_values, label=name)


def func(x: float, y: float):
    return y


def get_solution_1(n: int, bounds, y0, func):
    x0, xn = bounds

    h = (xn - x0) / n

    arr_value = [y0]
    arr_dots = [x0]

    while arr_dots[-1] < xn:
        k = get_k_1(arr_dots[-1], arr_value[-1], func, h)
        arr_value.append(arr_value[-1] + h/6 *
                         (k[0] + 2 * k[1] + 2 * k[2] + k[3]))
        arr_dots.append(arr_dots[-1] + h)

    return arr_value, arr_dots


def get_solution_2(n: int, bounds, x0, y0, f, g):
    t0, tn = bounds

    h = (tn - t0) / n

    arr_value = [(x0, y0)]
    arr_dots = [t0]

    while arr_dots[-1] < tn:
        k = get_k_2(arr_dots[-1], arr_value[-1][0], arr_value[-1][1], f, g, h)
        arr_value.append(((arr_value[-1][0] + h/6 * (k[0][0] + 2 * k[1][0] + 2 * k[2][0] + k[3][0])),
                         (arr_value[-1][1] + h/6 * (k[0][1] + 2 * k[1][1] + 2 * k[2][1] + k[3][1]))))
        arr_dots.append(arr_dots[-1] + h)

    return arr_value, arr_dots


def get_solution_3(n: int, bounds, x0, y0, z0, f, g, q):
    t0, tn = bounds

    h = (tn - t0) / n

    arr_value = [(x0, y0, z0)]
    arr_dots = [t0]

    while arr_dots[-1] < tn:
        k = get_k_3(arr_dots[-1], arr_value[-1][0],
                    arr_value[-1][1], arr_value[-1][2], f, g, q, h)
        arr_value.append(((arr_value[-1][0] + h/6 * (k[0][0] + 2 * k[1][0] + 2 * k[2][0] + k[3][0])),
                         (arr_value[-1][1] + h/6 * (k[0][1] +
                          2 * k[1][1] + 2 * k[2][1] + k[3][1])),
                         (arr_value[-1][2] + h/6 * (k[0][2] + 2 * k[1][2] + 2 * k[2][2] + k[3][2]))))
        arr_dots.append(arr_dots[-1] + h)

    return arr_value, arr_dots


def get_approx(n):
    arr_value1, arr_dots1 = get_solution_1(n, (0, 1), 1, func)
    arr_value2, arr_dots2 = get_solution_1(n * 2, (0, 1), 1, func)
    fig, ax = plt.subplots()


    max_error1 = [abs(arr_value1[i] - math.e ** arr_dots1[i])
                      for i in range(len(arr_value1))]
    ax.plot(arr_dots1, max_error1)
    plt.show()

    max_error2 = max([abs(arr_value2[i] - math.e ** arr_dots2[i])
                      for i in range(len(arr_value2))])

    print(math.log2(max_error1 / max_error2))


if __name__ == "__main__":

    arr_value, arr_dots = get_solution_1(10, (0, 1), 1, func)

    # fig, ax = plt.subplots()

    # draw_func(fig, ax, arr_value, arr_dots, "Численное решение")
    # draw_func(fig, ax, [math.e ** x for x in arr_dots],
              # arr_dots, "Aналитическое решение")

    print(arr_dots, arr_value)

    # plt.legend()
    # plt.grid()
    # plt.show()

    # get_approx(10)
    get_approx(100)
    # get_approx(200)
