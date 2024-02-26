import math


def bisect(func, range: tuple, delta: float):
    a, b = range
    c = (a + b) / 2
    if (func(a) * func(b) > 0):
        print("Ошибка в изоляции корня")
        return None
    if (b - a < delta):  # Проверям на достаточность точности
        return c
    if (func(c) == 0):  # Проверяем не попали ли в корень
        return c
    if (func(c) * func(b) < 0):  # Если с и b разных знаков, то корень где-то между ними
        return bisect(func, (c, b), delta)
    return bisect(func, (a, c), delta)  # Иначе корень между a и с


def f(x):
    return math.tan(x) - x


if __name__ == "__main__":
    print(bisect(f, (-1.25, 0.625), 0.001))
