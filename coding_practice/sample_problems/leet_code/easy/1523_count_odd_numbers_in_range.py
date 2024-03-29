import typing as t


"""
Summary: Math focused problem. Given high and low number, we know that between
them there is high - low numbers. At least half of them is going to be odd.
If one of them is odd --> (high - low) // 2 + 1
_______________________________________________________________________________

https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/


Given two non-negative integers low and high. Return the count of odd numbers 
between low and high (inclusive).

Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
"""


class Solution:
    # Exceeded the memory limit
    def countOdds(self, low: int, high: int) -> int:
        return len(list(filter(lambda e: e % 2 != 0, range(low, high + 1))))

    # Exceeded the time limit
    def countOdds(self, low: int, high: int) -> int:
        def _generate_odd_numbers(low: int, high: int):
            for number in range(low, high + 1):
                if number % 2:
                    yield number

        counter = 0
        for _ in _generate_odd_numbers(low, high):
            counter += 1
        return counter

    # Still time limit exceeded - no calling function though
    def countOdds(self, low: int, high: int) -> int:
        counter = 0
        for number in range(low, high + 1):
            if number % 2:
                counter += 1
        return counter

    # Just math lol
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        else:
            return (high - low) // 2 + 1
