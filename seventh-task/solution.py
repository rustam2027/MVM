from iterations import iterations, get_matrix, get_matrix_from_tridiagonal
from numpy.linalg import eigvals

import matplotlib.pyplot as plt


def U(x: float) -> float:
    return 1/2 * x ** 2


def solution():
    l = -1000
    r = 1000
    matrix = get_matrix(U, (l, r), 1000)
    norm = get_matrix_from_tridiagonal(matrix[0], matrix[1], matrix[2])
    sol = iterations(matrix, [1 for i in range(len(matrix[0]))], 1000)
    print()

    plt.plot([l + i * ((r - l) / 1000) for i in range(1001)], sol[0][-1])
    plt.show()


if __name__ == "__main__":
    solution()
