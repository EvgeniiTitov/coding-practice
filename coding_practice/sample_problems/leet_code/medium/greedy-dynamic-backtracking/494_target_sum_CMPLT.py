from typing import List


# TODO: Memoization (Top-Down). Bottom-up


"""
Summary: 
    Backtracking: Here base case is when we've processed all numbers, we can't
    end earlier like in a task when search for all combinations that add up to 
    the target. 
_______________________________________________________________________________

https://leetcode.com/problems/target-sum/

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' 
and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 
and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1
"""


class Solution:

    # Brute force. T: O(2 ^ N)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def _evaluate_expression(expression: List[str]) -> int:
            evaluated_sum = 0
            for sign, number in zip(expression, nums):
                evaluated_sum += eval(f"{sign}{number}")
            return evaluated_sum

        def _build_expression(curr_expression: List[str]) -> None:
            nonlocal evaluated_to_target

            # Base case(s)
            if len(curr_expression) == nums_length:
                if _evaluate_expression(curr_expression) == target:
                    evaluated_to_target += 1
                return

            for sign in "+-":
                curr_expression.append(sign)
                _build_expression(curr_expression)
                curr_expression.pop()

        # nums = [num for num in nums if num != 0]  # Os don't contribute
        nums_length = len(nums)
        evaluated_to_target = 0
        _build_expression([])
        return evaluated_to_target

    # T: O(2 ^ N); S: O(N)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def build_expression(
            nums: List[int],
            curr_index: int,
            curr_sum: int,
            target: int
        ) -> None:
            nonlocal evaluated_to_target

            if curr_index >= len(nums):
                if curr_sum == target:
                    evaluated_to_target += 1
                return

            build_expression(
                nums, curr_index + 1, curr_sum + nums[curr_index], target
            )
            build_expression(
                nums, curr_index + 1, curr_sum - nums[curr_index], target
            )

        evaluated_to_target = 0
        build_expression(nums, 0, 0, target)
        return evaluated_to_target


def main():
    print(Solution().findTargetSumWays(
        nums=[2, 1],
        target=1
    ))


if __name__ == '__main__':
    main()
