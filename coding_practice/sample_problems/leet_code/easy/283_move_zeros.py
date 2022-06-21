from typing import List


'''
Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''


class Solution:


    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        iteration = 0
        pointer = 0
        while iteration < length:
            if nums[pointer] == 0:
                nums.append(nums.pop(pointer))
            else:
                pointer += 1
            iteration += 1

    # Interesting solution
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                count += 1
            elif count != 0:
                nums[i - count] = nums[i]
                nums[i] = 0

    # Cheesy one haha
    def moveZeroes(self, nums: List[int]) -> None:
        nums[:] = [num for num in nums if num] + [0] * nums.count(0)


def main():
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    print(nums)


if __name__ == '__main__':
    main()
