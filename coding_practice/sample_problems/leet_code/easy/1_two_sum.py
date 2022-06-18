from typing import List

"""
Two Sum - https://github.com/qiyuangong/leetcode/blob/master/python/001_Two_Sum.py

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


"""


class Solution:

    # -- Brute force solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # Interesting using pointers
    def twoSum(self, nums, target):
        # two point
        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()
        start, end = 0, len(nums) - 1
        while start < end:
            curr = nums_index[start][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[start][1], nums_index[end][1]]
            elif curr < target:
                start += 1
            else:
                end -= 1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Just a single pass - iterate over all numbers on the list using their
        indices. For each number, we can calculate the complement required, so
        they would add up to target. This complement number could be in the
        dictionary if we encountered it before, then we just use the current
        number's index and the complement's index from the dictionary. Else,
        we just add the current number of the dictionary, it could become the
        complement later down the line.
        """
        hash_map = {}
        for i in range(len(nums)):
            number = nums[i]
            complement = target - number
            if complement in hash_map:
                return [i, hash_map[complement]]
            hash_map[number] = i


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))


if __name__ == "__main__":
    main()
