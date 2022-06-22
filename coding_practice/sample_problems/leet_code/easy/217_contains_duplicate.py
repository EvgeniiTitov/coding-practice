from typing import List


'''
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers_seen = set()
        for num in nums:
            if num in numbers_seen:
                return True
            numbers_seen.add(num)

    # T: O(N); S: O(N)
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict

        numbers_seen = defaultdict(int)
        for num in nums:
            numbers_seen[num] += 1
        for num, times_seen in numbers_seen.items():
            if times_seen > 1:
                return True

    # T: O(N log N); S: O(1)
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # O(N log N)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
