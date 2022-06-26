import typing as t


'''
Summary: Just remember the formula f(n) = f(n-1) + f(n-2); Caching helps heaps
------------------------------------------------------------------------------

https://leetcode.com/problems/fibonacci-number/


06/23/2022 14:05	Accepted	1333 ms	13.8 MB	python3  - without cache
06/23/2022 14:05	Accepted	42 ms	14 MB	python3
'''


class Solution:
    def fib(self, n: int) -> int:

        def _cache(func):
            cache = {}

            def wrapper(n: int) -> int:
                if n in cache:
                    return cache[n]
                result = func(n)
                cache[n] = result
                return result

            return wrapper

        @_cache
        def _calculate_fibo(n: int) -> int:
            if n == 0:
                return 0
            elif n == 1:
                return 1
            return _calculate_fibo(n - 1) + _calculate_fibo(n - 2)

        return _calculate_fibo(n)
