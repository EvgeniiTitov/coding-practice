from typing import List, MutableMapping


"""
Summary: From each position either current + the one after the next OR the next
one could be robbed. Consider both options and pick the max. The base case
is when we could beyond all houses (index >= len(houses))
_______________________________________________________________________________

https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from 
robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken 
into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the 
police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob 
house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""


class Solution:

    # D&C
    def rob(self, nums: List[int]) -> int:

        def _rob_houses(house_index: int, houses: List[int]) -> int:
            if house_index >= len(houses):
                return 0

            rob_current = (
                    houses[house_index] + _rob_houses(house_index + 2, houses)
            )
            rob_next = _rob_houses(house_index + 1, houses)

            return max(rob_current, rob_next)

        return _rob_houses(0, nums)

    # Top-down DP
    def rob(self, nums: List[int]) -> int:

        Cache = MutableMapping[int, int]

        def _rob_houses(
            house_index: int, houses: List[int], cache: Cache
        ) -> int:
            if house_index >= len(houses):
                return 0

            if house_index in cache:
                return cache[house_index]

            rob_current = (
                    houses[house_index] +
                    _rob_houses(house_index + 2, houses, cache)
            )
            rob_next = _rob_houses(house_index + 1, houses, cache)

            max_steal = max(rob_current, rob_next)
            cache[house_index] = max_steal

            return max_steal

        return _rob_houses(0, nums, {})

    # Bottom-up DP
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        robbed_amounts = [0] * (length + 1)

        robbed_amounts[-2] = nums[-1]
        for i in range(length - 2, -1, -1):
            robbed_amounts[i] = max(
                robbed_amounts[i + 1],
                nums[i] + robbed_amounts[i + 2]
            )

        return robbed_amounts[0]


def main():
    pass


if __name__ == '__main__':
    main()
