from typing import List


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Trees:

        1
    2       3
3               2

        2
    1       3
    
                
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def _generate_permutations(
            curr_index: int, curr_permutation: List[int]
        ) -> None:
            if len(curr_permutation) == len(nums):
                permutations.append(curr_permutation)

            if curr_index >= len(nums):
                return



        if len(nums) == 1:
            return [nums]

        permutations = []
        _generate_permutations(0, [])
        return permutations
