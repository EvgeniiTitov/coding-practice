from typing import List


# TODO: Dijkstra's solution: Dutch National Flag Problem

"""
Summary:
    Cheesy ones: Sorting (in place, not in place and then reassigning the arr)
    
    Dijkstra's solution: TODO: Dutch National Flag Problem
_______________________________________________________________________________

https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue, sort them 
in-place so that objects of the same color are adjacent, with the colors in 
the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, 
and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
"""


class Solution:

    # Passes but cheating.
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

    # Passes but slow. T: O(N^2); S: O(1)
    def sortColors(self, nums: List[int]) -> None:
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

    # TODO: One pass, constant space?
    def sortColors(self, nums: List[int]) -> None:
        pass

    # Passes but not in place
    def sortColors(self, nums: List[int]) -> None:

        def _quick_sort(nums: List[int]) -> List[int]:
            # Base case
            if len(nums) <= 1:
                return nums

            pivot = nums[0]
            greater = [num for num in nums if num > pivot]
            smaller = [num for num in nums if num < pivot]
            equal = [num for num in nums if num == pivot]

            return _quick_sort(smaller) + equal + _quick_sort(greater)

        nums[:] = _quick_sort(nums)


def main():
    nums = [2, 0, 2, 1, 1, 0]
    print(Solution().sortColors(nums=nums))
    print(nums)


if __name__ == '__main__':
    main()
