import typing as t


"""
Summary: The trick is to avoid multiplying the number N times O(N) and do it
in O(log N) by using some math. We know that x ^ (a + b) = (x ^ a) * (x ^ b). 
So, we operate on N itself, halving it till its <= 0. 

TODO: Read about the math behind it + LSB/MSB related solution
_______________________________________________________________________________

https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n (i.e., x ^ n).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
"""


class Solution:

    # T: O(N); Passes 291 / 305 tests then fails with Time Limit Exceeded
    def myPow(self, x: float, n: int) -> float:
        def _calculate_nth_power(num: float, n: int) -> float:
            res = 1
            for _ in range(n):
                res *= num
            return res

        if n == 0:
            return 1.0
        elif n > 0:
            return _calculate_nth_power(x, n)
        else:
            return 1 / _calculate_nth_power(x, -n)

    # T: O(log N);
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n:
            if n % 2:
                res *= x
            x *= x
            n //= 2
        return res
