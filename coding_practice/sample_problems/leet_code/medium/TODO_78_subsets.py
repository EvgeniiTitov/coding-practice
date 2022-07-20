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
        def _backtrack(start, cur_list):
            ans.append(cur_list[:])

            for j in range(start, n):
                cur_list.append(nums[j])
                _backtrack(j + 1, cur_list)
                cur_list.pop()

        n = len(nums)
        ans = []
        _backtrack(0, [])
        return ans


def main():
    print(Solution().subsets(nums=[1, 2, 3]))


if __name__ == "__main__":
    main()
