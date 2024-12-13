from iterations import iterations, get_matrix, get_matrix_from_tridiagonal
from numpy.linalg import eigvals

import matplotlib.pyplot as plt


def U(x: float) -> float:
    return 1/2 * x ** 2


def solution():
    l = -10
    r = 10
    n = 25_000
    matrix = get_matrix(U, (l, r), n)
    norm = get_matrix_from_tridiagonal(matrix[0], matrix[1], matrix[2])
    sol = iterations(matrix, [0.1 for i in range(len(matrix[0]))], 10 ** -8)
    print(sol[1] - 0.5)
    print()

    plt.plot([l + i * ((r - l) / n) for i in range(n)], sol[0][-1])
    plt.show()


if __name__ == "__main__":
    solution()
