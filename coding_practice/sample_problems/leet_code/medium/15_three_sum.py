from typing import List


"""
Summary:
    Pointers: Sort list, fix one number from the left, solve 2 sum problem for
    the remaining subset of the list (left + 1, len(list)); 
    ! No need to consider positive numbers, anything to the right is positive, 
    so wont add up to 0
    ! To avoid duplicates: Skip the same numbers for the pointer OR use set
    for triplets accumulation (less efficient though)
    
_______________________________________________________________________________

3Sum - https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []
"""


class Solution:

    # My brute force, ran out of time: 315 / 318 test cases passed.
    # T: O(N3); S: O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        triples = set()
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    num1 = nums[i]
                    num2 = nums[j]
                    num3 = nums[k]
                    if num1 + num2 + num3 == 0 and i != j != k:
                        triples.add(tuple(sorted([num1, num2, num3])))
        return [list(e) for e in triples]

    # T: O(N2); S: O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def _solve_two_sum_problem(i: int, out: List[List[int]]):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ == 0:
                    out.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Addressing same number to the left, it would get
                    # automatically address the same issue for the right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    left += 1

        nums.sort()
        out = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:  # !
                _solve_two_sum_problem(i, out)
        return out

    # Similar to ^ but hashset solution instead of pointers
    # Skipped avoiding duplicates, as I wouldnt have noticed that
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def _solve_two_sum_problem(start_i: int):
            numbers_seen = {}
            for j in range(start_i + 1, len(nums)):
                complement = 0 - (nums[start_i] + nums[j])
                if complement in numbers_seen:
                    triples.add(
                        tuple(sorted([nums[start_i], nums[j], complement]))
                    )
                numbers_seen[nums[j]] = j

        nums.sort()
        triples = set()
        for i, num in enumerate(nums):
            if num > 0:
                break

            if i == 0 or num != nums[i - 1]:  # !
                _solve_two_sum_problem(i)

        return [list(e) for e in triples]


def main():
    # numbers = [-1, 0, 1, 2, -1, -4]
    # numbers = [0, 0, 0, 0]
    numbers = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(numbers))


if __name__ == "__main__":
    main()
