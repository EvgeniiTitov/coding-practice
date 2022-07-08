import typing as t


"""
Prime numbers are a positive integer that’s greater than 1 that also have no 
other factors except for 1 and the number itself
"""


def check_if_prime(n: int) -> bool:
    if n < 2:
        return False
    for num in range(2, n // 2 + 1):
        if n % num == 0:
            return False
    return True


def find_primes(start: int, end: int) -> t.List[int]:
    out = []
    for number in range(start, end + 1):
        if check_if_prime(number):
            out.append(number)
    return out


def main():
    start = 0
    end = 100
    print(find_primes(start, end))


if __name__ == "__main__":
    main()
