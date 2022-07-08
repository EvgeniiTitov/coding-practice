from typing import List


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets 
(the power set).

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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def _generate_subsets(index: int, current: List[int]) -> None:
            subsets.append(current[:])
            # Taking and not taking each number at the index position
            for i in range(index, length):
                current.append(nums[i])
                _generate_subsets(i + 1, current)
                current.pop()

        length = len(nums)
        subsets = []
        _generate_subsets(0, [])
        return subsets

    # OR without using closure
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     subsets = []
    #     self.generate_subsets(
    #         index=0, nums=nums, current=[], subset=subsets
    #     )
    #     return subsets
    #
    # def generate_subsets(
    #     self,
    #     index: int,
    #     nums: List[int],
    #     current: List[int],
    #     subset: List[List[int]]
    # ) -> None:
    #     subset.append(current[:])
    #     for i in range(index, len(nums)):
    #         current.append(nums[i])
    #         self.generate_subsets(i + 1, nums, current, subset)
    #         current.pop()


def main():
    print(Solution().subsets(nums=[1, 2, 3]))


if __name__ == "__main__":
    main()
