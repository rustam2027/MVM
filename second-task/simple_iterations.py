import math


def simple_iterations(func, initial: float, amount: int) -> float | None:
    previous = initial
    for _ in range(amount):
        new = func(previous)
        previous = new
    return previous


if __name__ == "__main__":
    # Используется atan так как вблизи нуля у тангенса производная положительная
    print(simple_iterations(math.atan, 1.25, 100000000))
