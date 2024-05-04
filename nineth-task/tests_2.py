from Runge import get_solution_3
import matplotlib.pyplot as plt


def f(t, x, y, z):
    return 10 * (y - x)


def g(t, x, y, z):
    global r
    return x * (r - z) - y


def q(t, x, y, z):
    return x * y - 8/3 * z


if __name__ == "__main__":
    r = 26
    values, _ = get_solution_3(2000, (-15, 15), 0, 1, 1.05, f, g, q)
    print(values)

    ax = plt.figure().add_subplot(projection='3d')

    x = [i[0] for i in values]
    y = [i[1] for i in values]
    z = [i[2] for i in values]

    ax.plot(x, y, z, lw=0.5)

    plt.show()

