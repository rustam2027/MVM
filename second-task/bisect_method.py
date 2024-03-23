import math


def bisect(func, range: tuple, delta: float, counter=0):
    counter += 1
    a, b = range
    c = (a + b) / 2
    if (func(a) * func(b) > 0):
        print("Ошибка в изоляции корня")
        return None
    if (b - a < delta):  # Проверям на достаточность точности
        return c, counter
    if (func(c) == 0):  # Проверяем не попали ли в корень
        return c, counter
    if (func(c) * func(b) < 0):  # Если с и b разных знаков, то корень где-то между ними
        return bisect(func, (c, b), delta, counter)
    return bisect(func, (a, c), delta, counter)  # Иначе корень между a и с


def f(x):
    return math.tan(x) - x


if __name__ == "__main__":
    print(bisect(f, (-1.25, 0.625), 0.001))
    print(bisect(lambda x: x - math.pi, (2, 4), 0.001))
    print(bisect(f, (4.4, 4.6), 0.001))
