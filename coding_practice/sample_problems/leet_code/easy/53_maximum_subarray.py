from typing import List
import math


'''
Given an integer array nums, find the contiguous subarray (containing at 
least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23


Thoughts:
Sliding window? No! Hard to identify the logic when to move the left and right
pointers that both start at the beginning. 


Dynamic programming solution:
Let's focus on one important part: where the optimal subarray begins. We'll use the following example.

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

We can see that the optimal subarray couldn't possibly involve the first 3 
values - the overall sum of those numbers would always subtract from the total. 
Therefore, the subarray either starts at the first 4, or somewhere further to the right.

What if we had this example though?

nums = [-2,1000000000,-3,4,-1,2,1,-5,4]

We need a general way to figure out when a part of the array is worth keeping.

As expected, any subarray whose sum is positive is worth keeping. Let's start 
with an empty array, and iterate through the input, adding numbers to our array 
as we go along. Whenever the sum of the array is negative, we know the entire 
array is not worth keeping, so we'll reset it back to an empty array.

However, we don't actually need to build the subarray, we can just keep an 
integer variable current_subarray and add the values of each element there. 
When it becomes negative, we reset it to 0 (an empty array).
'''


class Solution:

    # My dumb way O(N3)
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        length = len(nums)
        largest_sum = -math.inf  # !
        for i in range(length):
            for j in range(i, length):  # Fine to start from the same i
                subarray = nums[i: j + 1]
                subarray_sum = sum(subarray)  # ! That's linear time!
                largest_sum = max(largest_sum, subarray_sum)
        return largest_sum

    # Dumb way optimized O(N2) - avoid calculating sum for a subarray, just add
    # each value (nested loop) to the subarray sum
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        length = len(nums)
        largest_sum = -math.inf  # !
        for i in range(length):
            subarray_sum = 0
            for j in range(i, length):
                subarray_sum += nums[j]
                largest_sum = max(largest_sum, subarray_sum)
        return largest_sum

    # Dynamic programming approach O(N) - wow!
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]
        for num in nums[1:]:
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray


def main():
    numbers = [5,4,-1,7,8]
    # numbers = [-2, 1]
    print(Solution().maxSubArray(numbers))


if __name__ == '__main__':
    main()
