import typing as t


"""
Given number N, find the number of ways to express N as a sum of: 1, 3, 4

Example 1:
N = 4
Output: 4
There are 4 ways N could be expressed: [4], [1, 3], [3, 1], [1, 1, 1, 1]

_______________________________________________________________________________

The challenging part is to come up with the formula:
We know the formula: NF(N) = NF(N - 1) + NF(N - 3) + NF(N - 4), example:
NF(7) = NF(6) + NF(4) + NF(3)

And the base cases:
If N == 0 --> 1 ()
If N == 1 --> 1 (1)
If N == 2 --> 1 (1, 1)
If N == 3 --> 2 (1, 1, 1; 3)

Then, we could solve it top-down OR bottom-up


"""


# ------------------------------- BOTTOM UP -----------------------------------
def find_factors_bottom_up(n: int) -> int:
    factors = [1, 1, 1, 2]
    for i in range(4, n + 1):
        factors.append(
            factors[i - 1] + factors[i - 3] + factors[i - 4]
        )
    return factors[n]


# -------------------------------- TOP DOWN -----------------------------------
def cache(func: t.Callable) -> t.Callable:
    _cache = {}

    def wrapper(num: int) -> int:
        if num not in _cache:
            _cache[num] = func(num)
        return _cache[num]

    return wrapper


@cache
def find_factors(n: int):
    if n in {0, 1, 2}:
        return 1
    elif n == 3:
        return 2

    sub1 = find_factors(n - 4)
    sub2 = find_factors(n - 3)
    sub3 = find_factors(n - 1)
    return sub1 + sub2 + sub3


def main():
    print(find_factors(7))
    print(find_factors_bottom_up(7))


if __name__ == '__main__':
    main()
