from Runge import get_solution_2
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.gridspec as gridspec


def func(t, x, y):
    return 10 * x - 2 * x * y


def gunc(t, x, y):
    return 2 * x * y - 10 * y


def plot(ax, ax1, ax2, ax4, x0, y0):
    values, dots = get_solution_2(100, (0, 2), x0, y0, func, gunc)
    x = np.array([x[0] for x in values])
    y = np.array([x[1] for x in values])
    ax.plot(dots, x, y)
    ax1.plot(dots, x)
    ax2.plot(dots, y)

    ax4.plot(dots, x, color="blue")
    ax4.plot(dots, y, color="red")


if __name__ == "__main__":
    fig = plt.figure(tight_layout=True)
    gs = gridspec.GridSpec(3, 2)

    ax1 = fig.add_subplot(gs[0, :], projection='3d')

    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[1, 1])

    ax4 = fig.add_subplot(gs[2, :])

    for x in range(10, 20):
        plot(ax1, ax2, ax3, ax4, x - 10, x)

    plt.show()
