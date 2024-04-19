import numpy as np
from scipy import integrate
from simpson import evaluate, func3


def approximation_degree(func, a, b, n):
    integral_n = evaluate(n, func, (a, b))
    n *= 2
    integral_2n = evaluate(n, func, (a, b))
    approximation_degree = np.log2(abs(integral_n - 2) / abs(integral_2n - 2))

    return approximation_degree


def func(x):
    return np.sin(x)


a = 0
b = np.pi
n = 10000

degree_of_approximation = approximation_degree(func, a, b, n)
print(f"Степень аппроксимации: {degree_of_approximation}")
print(evaluate(100, func, (a, b)))
