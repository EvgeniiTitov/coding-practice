from typing import List


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/coin-change-ii/

You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of 
money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
"""


class Solution:

    # Brute force. T: O(2 ^ N); Time Limit Exceeded: 14/28
    def change(self, amount: int, coins: List[int]) -> int:

        def _generate_combinations(curr_index: int, curr_amount: int):
            nonlocal nb_combinations

            # Base cases:

            # 1. Reached the desired amount
            if curr_amount == amount:
                nb_combinations += 1
                return

            # 2. Overshoot
            if curr_amount > amount:
                return

            # 3. Run out of coins
            if curr_index >= length:
                return

            # Probe the solution space
            for i in range(curr_index, length):
                _generate_combinations(
                    curr_index=i,
                    curr_amount=curr_amount + coins[i]
                )

        length = len(coins)
        if length == 1 and coins[0] == amount:
            return 1

        nb_combinations = 0
        _generate_combinations(0, 0)
        return nb_combinations

    # Top-down
    # TODO: Complete me, I am failing
    def change(self, amount: int, coins: List[int]) -> int:

        def _cache(func):
            _cache = {}
            def wrapper(index: int, coins: tuple[int]) -> int:
                if (index, coins) not in _cache:
                    _cache[(index, coins)] = func(index, amount)
                return _cache[(index, coins)]
            return wrapper

        @_cache
        def _generate_combinations(curr_amount: int, curr_coins: tuple[int]) -> int:

            # Base cases:

            # 1. Reached the desired amount
            if curr_amount == amount:
                return 1

            # 2. Overshoot
            if curr_amount > amount or len(curr_coins) == 0:
                return 0

            # Probe the solution space
            return (
                _generate_combinations(curr_amount + coins[-1], curr_coins)
                + _generate_combinations(curr_amount, curr_coins[:-1])
            )

        length = len(coins)
        if length == 1 and coins[0] == amount:
            return 1

        return _generate_combinations(0, tuple(coins))


def main():
    print(Solution().change(
        amount=5,
        coins=[1, 2, 5]
    ))


if __name__ == '__main__':
    main()
