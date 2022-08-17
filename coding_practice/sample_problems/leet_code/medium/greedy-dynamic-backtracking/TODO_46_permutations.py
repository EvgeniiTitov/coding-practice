from typing import List


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]          
"""


class Solution:

    # curr_index - from which index generate permutations, if, say, =1, then
    # we get just 2 permutations
    def permute(self, nums: List[int]) -> List[List[int]]:

        def _generate_permutations(curr_index: int = 0) -> None:
            # Base case:
            if curr_index >= length:
                output.append(nums[:])
                return

            for i in range(curr_index, length):
                # Place ith int first in the current permutation
                nums[curr_index], nums[i] = nums[i], nums[curr_index]

                # Use next integers to complete the permutations
                _generate_permutations(curr_index + 1)

                # Backtrack
                nums[curr_index], nums[i] = nums[i], nums[curr_index]

        length = len(nums)
        output = []
        _generate_permutations()
        return output


def main():
    print(Solution().permute(
        nums=[1, 2, 3]
    ))


if __name__ == '__main__':
    main()
