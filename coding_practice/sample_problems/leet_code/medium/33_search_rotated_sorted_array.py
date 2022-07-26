from typing import List


"""
Summary: The idea is to find the rotation index first using BS. Then, once
you know the rotation index you could consider 3 sub arrays: 0 to rotation_index,
rotation_index itself (single value), and rotation_index, length. To understand
which subarray to consider to search for the target, compare array[0] and target

      -
    - 
[ -           ]
             -
           -
         -
       -
^ Rotation index is the drop. From the drop you have left and right subarrays

_______________________________________________________________________________

https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown 
pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], 
nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and 
become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

! You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
"""


class Solution:

    # Cheating as its O(N)
    def search(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1

    def search(self, nums: List[int], target: int) -> int:

        def _find_rotation_index() -> int:
            left, right = 0, length - 1

            # No rotation, proper ascending array
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                middle = (left + right) // 2
                middle_val = nums[middle]
                next_val = nums[middle + 1]
                if middle_val > next_val:
                    return middle + 1
                else:
                    # We could be left or right of the *drop*, identify where
                    if middle_val < nums[left]:
                        right = middle - 1
                    else:
                        left = middle + 1

        def _find_target(left: int, right: int) -> int:
            while left <= right:
                middle = (left + right) // 2
                middle_val = nums[middle]
                if middle_val == target:
                    return middle
                elif target > middle_val:
                    left = middle + 1
                else:
                    right = middle - 1
            return -1

        length = len(nums)
        if not length:
            return -1
        elif length == 1:
            return 0 if nums[0] == target else -1

        pivot_index = _find_rotation_index()
        if nums[pivot_index] == target:
            return pivot_index
        elif pivot_index == 0:
            return _find_target(0, length - 1)
        elif target < nums[0]:
            return _find_target(pivot_index, length - 1)
        else:
            return _find_target(0, pivot_index)


def main():
    print(Solution().search(
        # nums=[4,5,6,7,8,9,0,1,2],
        # nums=[4,5,6,7,0,1,2],
        nums=[1,3],
        target=3
    ))


if __name__ == '__main__':
    main()
