from typing import List

'''
Two Sum - https://github.com/qiyuangong/leetcode/blob/master/python/001_Two_Sum.py

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


--> Another interesting solution:

If current value is smaller, we need to grow, start --> right, else end <- left

def twoSum(self, nums, target):
    # two point
    nums_index = [(v, index) for index, v in enumerate(nums)]
    nums_index.sort()
    begin, end = 0, len(nums) - 1
    while begin < end:
        curr = nums_index[begin][0] + nums_index[end][0]
        if curr == target:
            return [nums_index[begin][1], nums_index[end][1]]
        elif curr < target:
            begin += 1
        else:
            end -= 1
'''


class Solution:

    # -- Brute force solution
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums) - 1):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    # -- Doesn't work as [3, 3] results in unique_numbers = [3] but could add
    # up to 6
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     unique_numbers = list(set(nums))
    #     for i in range(len(unique_numbers) - 1):
    #         for j in range(i + 1, len(unique_numbers)):
    #             num_1 = unique_numbers[i]
    #             num_2 = unique_numbers[j]
    #             if num_1 + num_2 == target:
    #                 return [nums.index(num_1), nums.index(num_2)]

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


if __name__ == '__main__':
    main()
