from typing import List


"""
Summary:
! Its fine iterating over an array while popping items off it as long as you
recalculate its length every WHILE iteration to know when to stop.

The pointers solution is self explanatory. But you need to keep track if arr's
length to know when to stop.
_______________________________________________________________________________


https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array nums sorted in non-decreasing order, remove the 
duplicates in-place such that each unique element appears only once. The 
relative order of the elements should be kept the same.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of 
nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements 
of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are 
underscores).
"""


class Solution:

    # I tried appending Nones when popping and breaking the loop when I've
    # reached None - stupid solution as for 1,2,3 there will be no None ->
    # out of range index error
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        p = 0
        k = 1
        last_seen_number = None
        while True:  # ! OR while p < len(nums)
            if p >= length:
                break

            if last_seen_number == None:
                last_seen_number = nums[p]
                p += 1
                continue

            if nums[p] == last_seen_number:
                nums.pop(p)  # O(N) as we need to shift (O(1) for end)
                length -= 1
            else:
                last_seen_number = nums[p]
                p += 1
                k += 1
        return k

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1
        return len(nums)


def main():
    print(Solution().removeDuplicates([1,1,1,2,2,3,4,5]))


if __name__ == '__main__':
    main()
