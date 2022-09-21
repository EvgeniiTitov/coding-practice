from typing import List


"""
Summary:
    Backtracking: 
    
        1. Subsets contains sets of length from 0 to len(nums). The trick is to
        call your subset generation callable from a function determining the 
        length of a subset we're trying to generate. Doing it this way makes
        sure that in the solution tree we pick only those solutions that
        satisfy our constraint. Quite slow though. 
_______________________________________________________________________________

https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in 
any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""


class Solution:

    # Backtracking solution 1. T: O (N * 2 ^ N)
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def _generate_subset(
            curr_index: int,
            curr_subset: List[int],
            subsets: List[List[int]],
            required_length: int
        ) -> None:
            # Base case
            if len(curr_subset) == required_length:
                subsets.append(curr_subset.copy())
                return

            for i in range(curr_index, length):
                curr_subset.append(nums[i])
                _generate_subset(i + 1, curr_subset, subsets, required_length)
                curr_subset.pop()

        subsets = []
        length = len(nums)
        for l in range(length + 1):
            # Always start at 0 - the head of the solution tree and then get
            # those solutions that satisfy the length constraint
            _generate_subset(0, [], subsets, l)
        return subsets

    # Backtracking solution 2.
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # TODO: Another backtracking approach without the outer FOR loop
        pass


def main():
    print(Solution().subsets(nums=[1, 2, 3]))


if __name__ == '__main__':
    main()
