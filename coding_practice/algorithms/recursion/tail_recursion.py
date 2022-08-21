

"""
Bloody hell its ugly I wanna puke
"""


# -----------------------------------------------------------------------------

class Recurse(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


def recurse(*args, **kwargs):
    raise Recurse(*args, **kwargs)


def tail_recursive(f):
    def decorated(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except Recurse as r:
                args = r.args
                kwargs = r.kwargs
                continue

    return decorated

# -----------------------------------------------------------------------------


@tail_recursive
def get_factorial_tailed(n: int, accumulator: int = 1) -> int:
    if n == 0:
        return accumulator
    recurse(n - 1, accumulator * n)


# def get_factorial(n: int) -> int:
#     # Doesn't work, even with the decorator
#     if n == 1:
#         return 1
#     return n * get_factorial(n - 1)


def main():
    # print(get_factorial(1000))
    print(get_factorial_tailed(10000))


if __name__ == '__main__':
    main()
