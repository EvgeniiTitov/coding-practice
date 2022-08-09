from typing import List


"""
Summary: Sorting is a simple O(N log N) solution. The Floyd's algorithm on
steroids is quicker. 
_______________________________________________________________________________

https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer 
is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only 
constant extra space.
"""


class Solution:
    # Brute force. T: O(N2); S: N(1)
    def findDuplicate(self, nums: List[int]) -> int:
        """
        nums length is n + 1
        each num [1, n]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] == nums[j]:
                    return nums[i]

    # Slight optimisation. T: O(N log N); S: O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]

    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        def _get_next_number(index: int) -> int:
            return nums[index]

        # Find the intersection point of the two runners.
        while True:
            slow = _get_next_number(slow)
            fast = _get_next_number(_get_next_number(fast))
            if slow == fast:
                break

        # Find the "entrance" to the cycle.
        slow = nums[0]
        while slow != fast:
            slow = _get_next_number(slow)
            fast = _get_next_number(fast)

        return slow


def main():
    numbers = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
    print(Solution().findDuplicate(numbers))


if __name__ == "__main__":
    main()
