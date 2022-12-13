from typing import List
from __future__ import annotations


"""
Summary: Optimised brute force is fine. Do not forget that skipping a coin 
entirely is a valid option! Apart from them, D&C approach (tree structure)
_______________________________________________________________________________

https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If 
that amount of money cannot be made up by any combination of the coins, 
return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
"""


class Solution:

    """
    This is similar to your D&C with one important difference - you assumed
    you always want to pick the largest coin at least ONCE, what if we skip it
    all together? The skip logic is crucial to make top down work
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        import math

        def _cache(func):
            _cache = {}
            def wrapper(index: int, amount: int) -> int | float:
                if (index, amount) not in _cache:
                    _cache[(index, amount)] = func(index, amount)
                return _cache[(index, amount)]
            return wrapper

        @_cache
        def _reach_amount(curr_index: int, amount_left: int) -> int | float:
            # Base cases
            if amount_left == 0:
                return 0
            if curr_index < 0:  # we've run out of coins
                return math.inf

            # Skip current coin
            coins_needed = _reach_amount(curr_index - 1, amount_left)

            # Use current coin
            if amount_left >= coins[curr_index]:
                coins_needed = min(
                    coins_needed,
                    _reach_amount(
                        curr_index, amount_left - coins[curr_index]
                    ) + 1  # Used a coin, try again the same one (curr_index)
                )

            return coins_needed

        length = len(coins)
        coins_required = _reach_amount(length - 1, amount)
        return coins_required if coins_required != math.inf else -1

    # Brute force D&C, EXCEEDED TIME LIMIT
    def coinChange(self, coins: List[int], amount: int) -> int:

        def _reach_amount(
            curr_denomination_idx: int,
            curr_amount: int,
            curr_coins_used: int
        ) -> tuple[bool, int]:
            # Base cases
            if curr_denomination_idx >= total_coins or curr_amount > amount:
                return False, curr_coins_used

            if curr_amount == amount:
                return True, curr_coins_used

            has_reached, coins_took = False, float("inf")
            for denomination_index in range(curr_denomination_idx, total_coins):
                is_reached, nb_coins = _reach_amount(
                    curr_denomination_idx=denomination_index,
                    curr_amount=curr_amount + coins[denomination_index],
                    curr_coins_used=curr_coins_used + 1
                )
                if is_reached:
                    has_reached = True
                    coins_took = min(coins_took, nb_coins)
                    #  break This just break the solution

            return (True, coins_took) if has_reached else (False, 0)

        if amount == 0:
            return 0

        coins.sort(reverse=True)
        total_coins = len(coins)

        is_reached, nb_coins = _reach_amount(0, 0, 0)
        return nb_coins if is_reached else -1

    # Approach 1 - greedy. DOESNT WORK BECAUSE YOU DONT CONSIDER COMBINATIONS!
    # You cant reach a certain amount if you follow the greedy approach all
    # the time
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Edge cases
        if amount == 0:
            return 0

        # Sort the list, starting with the largest denominations
        coins.sort(reverse=True)

        nb_coins = len(coins)
        total_coins = 0
        current_amount = 0
        current_denomination_index = 0
        while current_denomination_index < nb_coins:
            current_denomination = coins[current_denomination_index]
            if current_amount + current_denomination < amount:
                current_amount += current_denomination
                total_coins += 1
            elif current_amount + current_denomination > amount:
                current_denomination_index += 1
            else:
                return total_coins + 1

        return total_coins if current_amount == amount else -1


def main():
    print(Solution().coinChange(
        # coins=[186,419,83,408],
        # amount=6249
        coins=[1, 2, 5],
        amount=18
    ))


if __name__ == '__main__':
    main()
