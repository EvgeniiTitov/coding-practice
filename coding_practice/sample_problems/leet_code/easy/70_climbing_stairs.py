import typing as t

from coding_practice.utils import timer


'''
https://leetcode.com/problems/climbing-stairs/
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can
you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Thoughts: 
Somewhat reminds the Fibo stuff. 

The formula at each step would be: 
climb_stairs(i, n) = climb_stairs(i + 1, n) + climb_stairs(i + 2, n)


! Dynamic programming is a good way to solve this problem as well considering
we know the formula:
public class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}
'''


class Solution:

    # Brute force ( O(2^N) ) + optimisation
    def climbStairs(self, n: int) -> int:
        '''
        Step size is 1 or 2

        '''

        def _cache(func):
            cache = {}
            def wrapper(n: int, stairs: int) -> int:
                if n in cache:
                    return cache[n]
                result = func(n, stairs)
                cache[n] = result
                return result
            return wrapper

        @_cache
        def _climb_stairs(current_step: int, stairs: int) -> int:
            if current_step > stairs:
                return 0
            elif current_step == stairs:
                return 1
            else:
                return (
                        _climb_stairs(current_step + 1, stairs)
                        + _climb_stairs(current_step + 2, stairs)
                )
        return _climb_stairs(0, n)



def cache(func: t.Callable) -> t.Callable:
    cache = {}
    def wrapper(n: int) -> int:
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper


@cache
def calculate_fibo(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return calculate_fibo(n - 1) + calculate_fibo(n - 2)


@timer
def main():
    print(calculate_fibo(35))  # 3 sec for n = 35 no cache


if __name__ == '__main__':
    main()