from typing import List


'''
Summary: 
    Single pass approach: iterate over items, add items to a set and remove if 
    its there. At the end, there will be only 1 item in the set - the one
    that appeared just once. 
    Bits manipulation: TBA
------------------------------------------------------------------------------

https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice 
except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use 
only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''


class Solution:

    # Space requirements not met. T complexity is O(n)
    def singleNumber(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]

        no_duplicates = set()
        for num in nums:
            if num not in no_duplicates:  # O(1)
                no_duplicates.add(num)
            else:
                no_duplicates.remove(num)
        return no_duplicates.pop()

    # Requirements not met - its O(n2)
    def singleNumber(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]

        no_duplicate = []
        for num in nums:
            if num not in no_duplicate:  # O(N)
                no_duplicate.append(num)
            else:
                no_duplicate.remove(num)
        return no_duplicate.pop()

    # Space requirements not met. T complexity is as above
    def singleNumber(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]

        from collections import defaultdict
        nums_seen = defaultdict(int)
        for num in nums:
            nums_seen[num] += 1

        for num, seen_times in nums_seen.items():
            if seen_times == 1:
                return num

    # Bits manipulation
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a


def main():
    numbers = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(numbers))


if __name__ == '__main__':
    main()
