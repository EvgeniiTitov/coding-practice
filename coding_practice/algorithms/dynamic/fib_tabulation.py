import typing as t


"""
Bottom-up
"""


def calculate_fibo(n: int) -> int:
    fibo_table = [0, 1]
    for i in range(2, n + 1):
        fibo_table.append(fibo_table[i - 1] + fibo_table[i - 2])
    return fibo_table[-1]


def main():
    print(calculate_fibo(7))
    print(calculate_fibo(500))


if __name__ == "__main__":
    main()
