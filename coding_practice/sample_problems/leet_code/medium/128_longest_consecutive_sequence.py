from typing import List


"""
Summary:
    Brute force: sorting
    
    Single pass: Turn nums into a set to eliminate duplicates AND allow O(1) 
    lookups. Start iterating through the nums, for each num check if num - 1 is 
    in the set. 
        If yes - skip it, it belongs to a larger ascending sequence
        If no - we found a new potential start for the ascending sequence,
        start going up from this number (incrementing it) while checking whether
        the increments are in the set (constant lookup times). SO, this solution
        is based on a FOR loop BUT we do not necessarily iterate through the 
        numbers left -> right. Rather, we find *starts* for the ascending 
        sequences and then check how far they go!
        
    IMPORTANT ^
_______________________________________________________________________________

https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest 
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""


class Solution:

    # Cheat solution, not O(N) + it doesn't work as expected: [1, 2, 0, 1] must
    # return 3, it returns 2. It's okay if consecutive nums are not adjacent
    # T: O(N log N)
    def longestConsecutive(self, nums: List[int]) -> int:

        length = len(nums)
        if length in {0, 1}:
            return length

        nums.sort()
        longest_global = 0
        longest_current = 0
        for i, num in enumerate(nums):
            # First iteration of the loop
            if longest_current == 0:
                longest_current += 1
                continue

            prev_num = nums[i - 1]
            if num - prev_num == 1:
                longest_current += 1
                continue
            else:
                longest_global = max(longest_global, longest_current)
                longest_current = 1

        longest_global = max(longest_global, longest_current)

        return longest_global

    # T: O(N); S: O(N)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)  # O(N)
        longest_global = 0

        for num in nums:
            # Found a new potential start for the ascending sequence
            if num - 1 not in nums:
                current_num = num
                longest_current = 1

                while current_num + 1 in nums:
                    current_num += 1
                    longest_current += 1

                longest_global = max(longest_global, longest_current)

        return longest_global


def main():
    print(Solution().longestConsecutive(
        # nums=[100, 4, 200, 1, 3, 2]
        nums=[1, 2, 0, 1]
    ))


if __name__ == '__main__':
    main()
