from typing import List


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets 
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self._generate_subsets(nums, 0, len(nums), [], subsets)
        return subsets

    def _generate_subsets(
        self,
        nums: List[int],
        start: int,
        end: int,
        curr_subset: List[int],
        subsets: List[int]
    ) -> None:
        subsets.append(curr_subset[:])  # copy
        for i in range(start, end):
            curr_subset.append(nums[i])
            self._generate_subsets(
                nums, i + 1, end, curr_subset, subsets
            )
            curr_subset.pop()


    # --- THIS IS SLIGHTLY INCORRECT AS IT GENERATES COPIES AS WELL ---
    # [[], [1], [1, 2], [1, 3], [2], [2, 1], [2, 3], [3], [3, 1], [3, 2]]
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     subsets = []
    #     self._generate_subsets(nums, [], subsets)
    #     return subsets
    #
    # def _generate_subsets(
    #     self,
    #     nums: List[int],
    #     curr_path: List[int],
    #     subsets: List[int]
    # ) -> None:
    #     # Base case
    #     if not len(nums):
    #         return
    #
    #     subsets.append(curr_path)
    #
    #     for i, num in enumerate(nums):
    #         new_curr_path = curr_path + [num]
    #         remaining_nums = nums[:i] + nums[i + 1:]
    #         self._generate_subsets(remaining_nums, new_curr_path, subsets)


def main():
    print(Solution().subsets(
        nums=[1, 2, 3]
    ))


if __name__ == '__main__':
    main()
