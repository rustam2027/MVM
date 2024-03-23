import math

import matplotlib.pyplot as plt


def newton(func, func_der, start: complex, root: float, delta: float, trace_need=False) -> float | None:
    def fi(x):
        return x - func(x)/func_der(x)

    trace = []

    x = [start, fi(start), 0]
    x[2] = fi(x[1])
    counter = 0

    while counter < 3 or abs(x[1] - x[2]) > delta:
        x = [x[1], x[2], fi(x[2])]
        trace.append(x[0])
        counter += 1

    if trace_need:
        return trace
    return x[2], counter


def func(x: float):
    return math.tan(x) - x


def func_der(x: float):
    return 1/((math.cos(x)) ** 2) - 1


if __name__ == "__main__":
    trace = newton(lambda x: x ** 3 - 1, lambda x: 3 *
                   x ** 2, -0.6 + 0.22j, 0, 0.0001, True)

    x_trace = []
    y_trace = []
    color = [0]
    size = []

    for z in trace:
        x_trace.append(z.real)
        y_trace.append(z.imag)
        color.append(color[-1] + 1)
        size.append(len(color) * 10)

    fig, ax = plt.subplots()

    ax.scatter(x_trace, y_trace, marker='o', c=color[1:], s=size)
    ax.grid(True)
    fig.tight_layout()

    plt.show()
