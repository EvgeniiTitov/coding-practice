from typing import List


"""
Summary: Array is sorted, got a target: good clue we could do it in O(log N) 
-> BS. Start looking for the target, if not found, the left pointer shows the
index. 
------------------------------------------------------------------------------

https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, return the 
index if the target is found. If not, return the index where it would be if 
it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""


class Solution:
    # T: O(log N); S: O(1)
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)

        if target > nums[-1]:
            return length
        elif target < nums[0]:
            return 0

        left_i, right_i = 0, length - 1
        while left_i <= right_i:  # !
            middle_i = (left_i + right_i) // 2
            number = nums[middle_i]

            if number == target:
                return middle_i
            elif number < target:
                left_i = middle_i + 1
            else:
                right_i = middle_i - 1
        return left_i  # ! IMPORTANT


def main():
    numbers = [1, 3, 5, 6]
    target = 2
    print(Solution().searchInsert(numbers, target))


if __name__ == "__main__":
    main()
