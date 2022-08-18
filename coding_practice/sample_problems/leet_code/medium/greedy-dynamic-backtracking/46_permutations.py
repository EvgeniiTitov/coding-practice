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

    # IN PLACE SOLUTION:
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

    # --- COPYING BASED recursive way ---
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self._generate_permutations(nums, [], permutations)
        return permutations

    def _generate_permutations(
        self,
        nums: List[int],
        curr_path: List[int],
        permutations: List[int]
    ) -> None:
        if not len(nums):
            permutations.append(curr_path)
        else:
            for i in range(len(nums)):
                new_curr_path = curr_path + [nums[i]]
                remaining_nums = nums[:i] + nums[i + 1:]
                self._generate_permutations(remaining_nums, new_curr_path,
                                            permutations)

    # --- COPYING BASED recursive way ---
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self._generate_permutations(nums, [], permutations)
        return permutations

    def _generate_permutations(
        self,
        nums: List[int],
        curr_path: List[int],
        permutations: List[int]
    ) -> None:
        if not len(nums):
            permutations.append(curr_path[:])
        else:
            for i, num in enumerate(nums):
                curr_path.append(num)
                remaining_nums = nums[:i] + nums[i + 1:]
                self._generate_permutations(
                    remaining_nums, curr_path, permutations
                )
                curr_path.pop()

    # --- COPYING BASED iterative way ---
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        stack = [(nums, [])]
        while len(stack):
            curr_nums, curr_path = stack.pop()
            if not len(curr_nums):
                permutations.append(curr_path)
            else:
                for i, num in enumerate(curr_nums):
                    new_curr_path = curr_path + [num]
                    remaining_nums = curr_nums[:i] + curr_nums[i + 1:]
                    stack.append((remaining_nums, new_curr_path))
        return permutations


def main():
    print(Solution().permute(
        nums=[1, 2, 3]
    ))


if __name__ == '__main__':
    main()
