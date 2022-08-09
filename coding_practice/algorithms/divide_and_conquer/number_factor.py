import typing as t
from functools import lru_cache


"""
Given number N, find the number of ways to express N as a sum of 1, 3 and 4.
The same number could be used multiple times

Example 1:
N = 4
Output: 4
There are 4 ways N could be expressed: [4], [1, 3], [3, 1], [1, 1, 1, 1]

_______________________________________________________________________________

First check if this problem ^ follows the optimal substructure property:

Let's say we want to solve the problem for N = 5. Then, if we could solve the
problem for N = 4, then by adding 1 to each case we could solve the problem for
5 as well.

Careful, we could use only 1, 3 and 4.

Solution for 5:
[4, 1], [1, 4], [1, 3, 1], [3, 1, 1], [1, 1, 3], [1, 1, 1, 1, 1]


f(4): [4], [1, 3], [3, 1], [1, 1, 1, 1]

f(4) + 1: [4, 1], [1, 3, 1], [3, 1, 1], [1, 1, 1, 1, 1]

As you need see, f(4) + 1 misses some solutions which will come from other
subproblems:

f(2): [1, 1]
f(2) + 3: [1, 1, 3]

f(1): [1]
f(1) + 4: [1, 4]

Combining all valid solutions from above:
[
    [1, 4],  # comes from f(1) + 4

    [1, 1, 3],  # comes from f(2) + 3

    [4, 1],  # comes from f(4) + 1
    [1, 3, 1],  # comes from f(4) + 1
    [3, 1, 1],  # comes from f(4) + 1
    [1, 1, 1, 1, 1],  # comes from f(4) + 1
]

How did we arrive at f(4), f(2) and f(1)?
N - 4 = 5 - 4 = 1
N - 3 = 5 - 3 = 2
N - 1 = 5 - 1 = 4
So, to find subproblems that we need to solve we just say N - M, where M is
the available numbers

This ^ could be seen as a tree, similar to the Fibonacci problem. We keep 
solving the same set of simple problems.

The constraint here is the available numbers: 1, 3, 4
"""


def cache(func: t.Callable) -> t.Callable:
    _cache = {}

    def wrapper(num: int) -> int:
        if num in _cache:
            return _cache.get(num)
        res = func(num)
        _cache[num] = res
        return res

    return wrapper


@cache
# @lru_cache()
def find_ways(n: int):
    print("Called with:", n)
    # BASE CASES:
    # If N = 0, 1 or 2. There is only 1 way to express this N using 1, 3, or 4
    # 0 []
    # 1: [1]
    # 2: [1, 1]
    if n in {0, 1, 2}:
        return 1
    # If N == 3, there are 3 ways to express it using 1, 3, 4:
    # [3], [1, 1, 1]
    elif n == 3:
        return 2

    sub1 = find_ways(n - 4)
    sub2 = find_ways(n - 3)
    sub3 = find_ways(n - 1)
    return sub1 + sub2 + sub3


def main():
    print(find_ways(7))


if __name__ == "__main__":
    main()
