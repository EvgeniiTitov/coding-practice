from typing import List


"""
Summary:

_______________________________________________________________________________

https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array cost where cost[i] is the cost of ith step on a 
staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""


class Solution:

    # D&C
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def _climb_stairs(step_index: int, cost: List[int]) -> int:
            if step_index >= len(cost):
                return 0

            option1 = _climb_stairs(step_index + 1, cost)
            option2 = _climb_stairs(step_index + 2, cost)

            return cost[step_index] + min(option1, option2)


        if len(cost) == 1:
            return cost[0]

        option1 = _climb_stairs(0, cost)
        option2 = _climb_stairs(1, cost)

        return min(option1, option2)

    # Top-down DP
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def _cache(func):
            _cache = {}
            def wrapper(num: int, *args, **kwargs):
                if num not in _cache:
                    _cache[num] = func(num, *args, **kwargs)
                return _cache[num]
            return wrapper

        @_cache
        def _climb_stairs(step_index: int, cost: List[int]) -> int:
            if step_index >= len(cost):
                return 0

            option1 = _climb_stairs(step_index + 1, cost)
            option2 = _climb_stairs(step_index + 2, cost)

            return cost[step_index] + min(option1, option2)


        if len(cost) == 1:
            return cost[0]

        option1 = _climb_stairs(0, cost)
        option2 = _climb_stairs(1, cost)

        return min(option1, option2)

    # Bottom-up DP
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        min_cost = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            take_one_step = min_cost[i - 1] + cost[i - 1]
            take_two_steps = min_cost[i - 2] + cost[i - 2]
            min_cost[i] = min(take_one_step, take_two_steps)

        return min_cost[-1]


def main():
    print(Solution().minCostClimbingStairs(
        # cost=[10,15,20]
        cost=[1,100,1,1,1,100,1,1,100,1]
    ))


if __name__ == '__main__':
    main()
