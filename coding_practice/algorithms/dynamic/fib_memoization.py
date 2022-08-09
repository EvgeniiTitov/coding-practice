import typing as t
from functools import wraps


"""
Top-down approach using Memoization
"""


# ------------------------------ FIRST APPROACH -------------------------------
def calculate_fibo_1(n: int, memo: t.MutableMapping[int, int]) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1

    if n not in memo:
        memo[n] = calculate_fibo_1(n - 1, memo) + calculate_fibo_1(n - 2, memo)
    return memo[n]


# ------------------------------ SECOND APPROACH ------------------------------
def cache(func: t.Callable) -> t.Callable:
    _cache = {}

    @wraps(func)
    def wrapper(n: int) -> int:
        if n not in _cache:
            _cache[n] = func(n)
        return _cache[n]

    return wrapper


@cache
def calculate_fibo_2(n: int):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return calculate_fibo_2(n - 1) + calculate_fibo_2(n - 2)


# ------------------------------- THIRD APPROACH ------------------------------


def calculate_fibo_3(n: int, memo: list[int]) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1

    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = calculate_fibo_3(n - 1, memo) + calculate_fibo_3(n - 2, memo)
        return memo[n]


def main():
    n = 10

    print(calculate_fibo_1(n, {}))

    print(calculate_fibo_2(n))

    print(calculate_fibo_3(n, [0] * (n + 1)))


if __name__ == "__main__":
    main()
