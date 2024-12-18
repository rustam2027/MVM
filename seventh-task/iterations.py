import numpy as np
from typing import List, Tuple, Callable
from numpy.linalg import eig

from tridiagonal import solve_tridioganal



def iterations(M: List[List[float]], x: np.ndarray, eps: float) -> Tuple[List[np.matrix], float]:
    y_k: List[np.ndarray] = []
    x_k: List[np.ndarray] = [x]
    lamd_prev = 0
    lamd = 1
    while abs(lamd - lamd_prev) > eps:
        y_k.append(solve_tridioganal(M[0], M[1], M[2], x_k[-1]))
        lamd, lamd_prev = np.dot(x_k[-1], y_k[-1]) / (np.linalg.norm(y_k[-1]) ** 2), lamd
        x_k.append(y_k[-1] / np.linalg.norm(y_k[-1]))
        x_k[-1][-1] = 0
        x_k[-1][0] = 0
        print(lamd - 0.5)
    return y_k, lamd


def get_matrix(func: Callable, interval: Tuple[float, float], n: int) -> List[List[float]]:
    # <-- initial values on left border
    return_arr: List[List[float]] = [[0], [1], [0]]
    l, r = interval
    h = (r - l) / (n - 1)
    c = -1/2

    for i in range(1, n - 1):
        return_arr[0].append(c / h ** 2)
        return_arr[1].append((-c * 2) / h ** 2 + func(l + h * i))
        return_arr[2].append(c / h ** 2)

    return_arr[0].append(0)  # |
    return_arr[1].append(1)  # | <-- initial values on right border
    return_arr[2].append(0)  # |

    return return_arr


def get_matrix_from_tridiagonal(left: List[float], center: List[float], right: List[float]):
    n = len(left)
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if i > 0:
            arr[i][i - 1] = left[i]
        arr[i][i] = center[i]
        if i != n - 1:
            arr[i][i + 1] = right[i]
    return arr


if __name__ == "__main__":
    def potential_function(x): return 0.5 * x ** 2
    interval = (-4, 4)
    n_points = 10

    M1 = get_matrix(potential_function, interval, n_points)
    mat = np.array(get_matrix_from_tridiagonal(M1[0], M1[1], M1[2]))

    initial_guess = np.ones(len(M1[0]))
    initial_guess /= np.linalg.norm(initial_guess)

    yk, lambd = iterations(M1, initial_guess, 10**-10)
    print(yk[-1])
    print(lambd)
    print(eig(mat))
