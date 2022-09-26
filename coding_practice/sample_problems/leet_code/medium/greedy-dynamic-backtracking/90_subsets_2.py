from typing import List


"""
Summary:
    Backtracking: Sorting is the key to prevent duplicates. Then generate sets
    storing them in a set to further prevent duplicates
_______________________________________________________________________________

https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in 
any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""


class Solution:

    # T: O(N * 2 ^ N); S: O(N)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def _generate_subset(
            len_needed: int,
            curr_index: int,
            curr_subset: List[int],
            subsets: set[tuple[int]]
        ) -> None:
            # Base cases
            if len(curr_subset) == len_needed:
                curr_subset = tuple(curr_subset)
                if curr_subset not in subsets:
                    subsets.add(curr_subset)
                return

            for index in range(curr_index + 1, length):
                curr_subset.append(nums[index])
                _generate_subset(len_needed, index, curr_subset, subsets)
                curr_subset.pop()

        nums.sort()  # ! Fixed the issue of having duplicates: [4, 1], [1, 4]
        length = len(nums)
        if not length:
            return []
        elif length == 1:
            return [[], nums]

        subsets = set()
        for length_required in range(length + 1):
            _generate_subset(length_required, -1, [], subsets)

        return [list(subset) for subset in subsets]

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # TODO: Another backtracking approach without the outer FOR loop
        #       (generating all lengths in a single call without calling for
        #       each length)
        pass


def main():
    print(Solution().subsetsWithDup(
        nums=[1, 2, 2]
    ))


if __name__ == '__main__':
    main()
