from typing import List


'''
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

Thoughts:
2 pointers, left and right. We check what they add up to. Then, we know what
number we need to find, so that we get 0 once summed up. The third complement
number will be somewhere in between the 2 points, how do we find it? Binary 
search? A function that once given an array finds the number / index of the 
number in it? 
'''


class Solution:

    # # My brute force, ran out of time
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     if not len(nums):
    #         return []
    #     if nums == [0]:
    #         return []
    #
    #     triplets = set()
    #     for i in range(len(nums) - 2):
    #         for j in range(i + 1, len(nums) - 1):
    #             for k in range(j + 1, len(nums)):
    #                 if (
    #                         nums[i] + nums[j] + nums[k] == 0
    #                         and i != j != k
    #                 ):
    #                     triplets.add(
    #                         ",".join(
    #                             map(str, sorted([nums[i], nums[j], nums[k]]))
    #                             )
    #                     )
    #     return [
    #         list(map(int, triplet.split(","))) for triplet in triplets
    #     ]

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def _get_complement(left: int, right: int, complement: int):
            # TODO: Could do binary search here
            for index in range(left + 1, right):  # don't include pointers
                number = nums[index]
                if number == complement:
                    return index
            return None


        if not len(nums):
            return []
        if nums == [0]:
            return []

        nums.sort()  # O(n log n)
        length = len(nums)
        left, right = 0, length - 1
        triplets = []
        while left < right:
            number_left = nums[left]
            number_right = nums[right]
            complement = 0 - (number_left + number_right)

            complement_index = _get_complement(left, right, complement)
            if complement_index:
                triplets.append([number_left, complement, number_right])

            if complement >= number_right:
                left += 1
            else:
                right -= 1
        return triplets


def main():
    numbers = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(numbers))


if __name__ == '__main__':
    main()
