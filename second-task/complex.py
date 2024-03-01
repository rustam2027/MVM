from newton import newton
import matplotlib.pyplot as plt


ROOTS = [-0.5 - 0.86602j, -0.5 + 0.86602j, 1]


def func(z: complex):
    return z ** 3 - 1


def der_func(z: complex):
    return 3 * z ** 2


def get_root_number(z: complex):
    for i in range(len(ROOTS)):
        if abs(ROOTS[i] - z) < 0.01:
            return i
    return None


COEFFICIENT = 100
X = 200
if __name__ == "__main__":
    x = []
    y = []
    c = []
    for t in range(-X, X):
        for p in range(-X, X):
            if t == 0 and p == 0:
                continue
            x.append(t / COEFFICIENT)
            y.append(p / COEFFICIENT)
            c.append(get_root_number(
                newton(func, der_func, complex(t / COEFFICIENT, p / COEFFICIENT), 0, 0.001)[0]))
    fig, ax = plt.subplots()

    ax.scatter(x, y, c=c)
    ax.grid(True)
    fig.tight_layout()

    plt.show()
