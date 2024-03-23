import math

from isolation import get_aprox, get_isolation
from newton import func, func_der

from newton import newton
from bisect_method import bisect
from secnat import secnat
from simple_iterations import simple_iterations


def get_numbers():
    left = int(input("Введите левый край: "))
    right = int(input("Введите правый край: ")) + 1

    return left, right


def get_delta():
    delta = float(input("Введите точность: "))

    return delta


if __name__ == "__main__":
    roots_range = get_numbers()
    # roots_range = (-1, 2)
    delta = get_delta()
    # delta = 0.0001
    print(f"Точность: {delta}")

    for num in range(*roots_range):
        print()
        isol = get_aprox(func, get_isolation(num))
        print(f"Корень номер {num}, изоляция {isol}")

        print("Метод ньютона: ".ljust(25), newton(func, func_der, isol[1], 0, delta))
        print("Метод биссекции: ".ljust(25), bisect(func, isol, delta))
        print("Метод секущих: ".ljust(25), secnat(func, isol[1], isol[1] + 0.01, delta))
        print("Метод простых итераций: ".ljust(25), simple_iterations(isol, delta, num))
