from typing import List


"""
Summary:
    Both solutions pick a number, then either pick the same number OR start
    picking other available numbers (tree structure). The second solution is
    easier to cache though because we are going right to left. The cache
    tells us if we can reach the amount required with the current sum and the
    remaining coins (curr_coins).
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

        def _generate_combinations(curr_index: int, curr_amount: int) -> None:
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
    def change(self, amount: int, coins: List[int]) -> int:

        # ! Cache tells us if we can reach the amount required with the current
        # sum and remaining coins
        def _cache(func):
            _cache = {}
            def wrapper(curr_amount: int, curr_coins: tuple[int]) -> int:
                if (curr_amount, curr_coins) not in _cache:
                    _cache[(curr_amount, curr_coins)] = func(
                        curr_amount, curr_coins
                    )
                return _cache[(curr_amount, curr_coins)]
            return wrapper

        @_cache
        def _generate_combinations(curr_amount: int, curr_coins: tuple[int]) -> int:

            # Base cases:

            # 1. Reached the desired amount
            if curr_amount == amount:
                return 1

            # 2. Overshoot
            if curr_amount > amount:
                return 0

            # 3. Run out of coins
            if len(curr_coins) == 0:
                return 0

            # Keep picking the same coin
            option_1 = _generate_combinations(curr_amount + curr_coins[-1], curr_coins)

            # Do not pick the current coin, pick the next one
            option_2 = _generate_combinations(curr_amount, curr_coins[:-1])

            return option_1 + option_2

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
