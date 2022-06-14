from typing import List


'''
3Sum - https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not len(nums):
            return []
        if nums == [0]:
            return []

        triplets = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if (
                            nums[i] + nums[j] + nums[k] == 0
                            and i != j != k
                    ):
                        triplets.append([nums[i], nums[j], nums[k]])
        return triplets


def main():
    pass


if __name__ == '__main__':
    main()
