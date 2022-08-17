from typing import List, MutableMapping


"""
Summary: The trick is - the problem is the duplicate of the original except for
if you steal from the first house, you can't steal from the last. So, 2 cases:
stole from the first or not. Then, the problem is identical to the original one
_______________________________________________________________________________

https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each 
house has a certain amount of money stashed. All houses at this place are 
arranged in a circle. That means the first house is the neighbor of the last 
one. Meanwhile, adjacent houses have a security system connected, and it will 
automatically contact the police if two adjacent houses were broken into on 
the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the 
police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 
(money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
"""


class Solution:

    # D&C
    def rob(self, nums: List[int]) -> int:

        def _rob_houses(
            house_index: int, houses: List[int], first_stolen: bool
        ) -> int:
            if first_stolen:
                if house_index >= length - 1:
                    return 0
            else:
                if house_index >= length:
                    return 0

            steal_current = (
                    houses[house_index]
                    + _rob_houses(house_index + 2, houses, first_stolen)
            )
            steal_next = _rob_houses(house_index + 1, houses, first_stolen)

            return max(steal_current, steal_next)

        length = len(nums)
        if length == 1:
            return nums[0]

        return max(_rob_houses(0, nums, True), _rob_houses(1, nums, False))

    # Top-down DP
    def rob(self, nums: List[int]) -> int:

        Cache = MutableMapping[tuple, int]

        def _rob_houses(
            house_index: int,
            houses: List[int],
            first_stolen: bool,
            cache: Cache
        ) -> int:
            if first_stolen:
                if house_index >= length - 1:
                    return 0
            else:
                if house_index >= length:
                    return 0

            if (house_index, first_stolen) in cache:
                return cache[(house_index, first_stolen)]

            steal_current = (
                    houses[house_index]
                    + _rob_houses(house_index + 2, houses, first_stolen, cache)
            )
            steal_next = (
                _rob_houses(house_index + 1, houses, first_stolen, cache)
            )
            max_steal = max(steal_current, steal_next)

            cache[(house_index, first_stolen)] = max_steal
            return max_steal

        length = len(nums)
        if length == 1:
            return nums[0]

        cache = {}
        return max(
            _rob_houses(0, nums, True, cache),
            _rob_houses(1, nums, False, cache)
        )

    # Bottom-up DP
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums: List[int]) -> int:
        t1 = 0
        t2 = 0
        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)
            t2 = temp

        return t1


def main():
    pass


if __name__ == '__main__':
    main()
