from functools import reduce


def calculate_special_sum(n: int) -> int:
    return sum(i * (i + 1) for i in range(1, n))
    # return reduce(lambda x, y: x + y, (i * (i + 1) for i in range(1, n))) if n != 1 else 0
