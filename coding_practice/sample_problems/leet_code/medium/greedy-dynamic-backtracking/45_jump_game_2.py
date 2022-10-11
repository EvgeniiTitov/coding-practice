from typing import List


# TODO: Bottom-up DP + Greedy


"""
Summary:
    Brute force - D&C pretty much or a top-down DP variation. 
_______________________________________________________________________________

https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers nums, you are initially positioned at 
the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps. (MIN JUMPS)

You can assume that you can always reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
"""


class Solution:

    # def jump(self, nums: List[int]) -> int:
    #     length = len(nums)
    #     destination = length - 1
    #
    #     jumps_count = [None] * length
    #     jumps_count[-1] = 0
    #
    #     for i in range(length - 2, -1, -1):
    #         if i + nums[i] == destination:
    #             jumps_count[i] = 1
    #         else:
    #             # Find next min jump
    #             steps_till_end = nums[i + 1: nums[i] + 1]
    #             if len(steps_till_end):
    #                 min_jumps_till_end = min(steps_till_end)
    #                 jumps_count[i] = 1 + min_jumps_till_end
    #             else:
    #                 jumps_count[i] = 1
    #
    #     return jumps_count[0]


    # My optimised yet incorrect backtracking. Passes 80/109 and then fails
    def jump(self, nums: List[int]) -> int:

        def _find_shortest_path_up(
            curr_index: int, curr_jumps: int, cache: dict
        ) -> int:
            # Base case
            if curr_index == destination:
                return curr_jumps

            if curr_index in cache:
                return (curr_jumps - 1) + cache.get(curr_index)

            # Avoid out of bounds jumps
            furthest_jump = min(curr_index + nums[curr_index], length - 1)

            min_jumps = float("inf")
            for i in range(furthest_jump, curr_index, -1):
                jumps_took = _find_shortest_path_up(
                    curr_index=i,
                    curr_jumps=curr_jumps + 1,
                    cache=cache
                )
                min_jumps = min(min_jumps, jumps_took)

            cache[curr_index] = min_jumps

            return min_jumps

        length = len(nums)
        if length == 1:
            return 0

        destination = length - 1
        return _find_shortest_path_up(0, 0, {})

    # My backtracking, Time Limit Exceeded: 73/109 tests.
    # T: O(2 ^ N); S: O(N)
    def jump(self, nums: List[int]) -> int:

        def _find_shortest_path_up(
            curr_index: int = 0, curr_jumps: int = 0
        ) -> int:
            # Base case
            if curr_index == destination:
                return curr_jumps

            # Avoid out of bounds jumps
            furthest_jump = min(curr_index + nums[curr_index], length - 1)

            # Greedily start from jumping as far as possible
            min_jumps = float("inf")
            for i in range(furthest_jump, curr_index, -1):
                jumps_took = _find_shortest_path_up(
                    curr_index=i,
                    curr_jumps=curr_jumps + 1
                )
                min_jumps = min(min_jumps, jumps_took)

            return min_jumps

        length = len(nums)
        if length == 1:
            return 0

        destination = length - 1
        return _find_shortest_path_up()


def main():
    print(Solution().jump(
        nums=[9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5]
        # nums=[2, 3, 1, 1, 4]
    ))


if __name__ == '__main__':
    main()
