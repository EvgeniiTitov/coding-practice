from typing import List


"""
Summary:
    Thoughts: 2 options: 
        1) Pick curr number + go to the next greater one
        2) Ignore curr number, consider all remaining numbers
    ^ This turned out to be incorrect, passes only 30% of tests
        
_______________________________________________________________________________

https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly 
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting 
some or no elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], 
therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""


class Solution:
    # This SHIT is WRONG (quite close though, something's slightly off)
    def lengthOfLIS(self, nums: List[int]) -> int:

        def _find_longest_subseq(
            nums: List[int], curr_index: int, curr_subseq_len: int, cache: dict
        ) -> int:
            # Base case
            if curr_index >= length:
                return curr_subseq_len

            if curr_index in cache:
                return cache[curr_index] + curr_subseq_len

            # Options:
            # 1. Ignore current number, consider all remaining ones
            option1 = _find_longest_subseq(
                nums, curr_index + 1, curr_subseq_len + 0, cache
            )

            # 2. Pick current number, find next greatest one to do go if any
            curr_value = nums[curr_index]
            next_index = None
            for i in range(curr_index + 1, length):
                if nums[i] > curr_value:
                    next_index = i
                    break

            if next_index is not None:
                option2 = _find_longest_subseq(
                    nums, next_index, curr_subseq_len + 1, cache
                )
            else:
                option2 = curr_subseq_len + 1

            max_val = max(option1, option2)
            cache[curr_index] = max_val

            return max_val

        length = len(nums)
        if length == 1:
            return 1

        return _find_longest_subseq(nums, 0, 0, {})

    # T: O(N2); S: O(N)
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


def main():
    print(Solution().lengthOfLIS(
        # nums=[10,9,2,5,3,7,101,18]
        # nums=[0,1,0,3,2,3]
        # nums=[7,7,7,7,7,7,7]
        # nums=[4,10,4,3,8,9]
        # nums=[8,7,6,5,1,3,4]
        nums=[8, 1, 6, 2, 3, 10]
    ))


if __name__ == '__main__':
    main()
