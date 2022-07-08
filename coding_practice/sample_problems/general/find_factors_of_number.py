import typing as t


"""
In math, a factor is a number that divides another number evenly, 
that is with no remainder.
"""


def find_number_factors_lazy(n: int) -> t.Iterator[int]:
    for factor in range(1, n + 1):
        if n % factor == 0:
            yield factor


def find_number_factors(n: int) -> t.List[int]:
    factors = []
    for factor in range(1, n + 1):
        if n % factor == 0:
            factors.append(factor)
    return factors


def main():
    number = 320
    print(find_number_factors(number))

    for factor in find_number_factors_lazy(number):
        print(factor, end=" ")


if __name__ == "__main__":
    main()
