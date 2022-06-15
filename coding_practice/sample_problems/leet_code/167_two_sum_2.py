from typing import List


'''
Two Sum || - Input Array Is Sorted (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

Given a 1-indexed array of integers numbers that is already sorted in 
non-decreasing order, find two numbers such that they add up to a specific 
target number. Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an 
integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not 
use the same element twice.

Your solution must use only constant extra space.

Thoughts:
2 pointers? Index 1 < index 2 ==> left pointer is at 0, the right one at 
len(numbers) - 1. Then we attempt to get the target


-> |
   |
   |
   |
   |
-> |


! The space complexity is constant as each iteration we store just 3 values:
left, right, and the sum (+ some other variables). The point is there are no
containers that grow or whatever
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)

        if length == 2 and numbers[0] + numbers[1] == target:
            return [1, 2]

        left, right = 0, length - 1
        while left < right:
            left_number = numbers[left]
            right_number = numbers[right]
            sum_ = left_number + right_number

            if sum_ == target:
                return [left + 1, right + 1]
            elif sum_ < target:
                left += 1
            elif sum_ > target:
                right -= 1


def main():
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))


if __name__ == '__main__':
    main()
