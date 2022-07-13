from typing import List


"""
Summary: 
    - Brute force, brute force optimised: simple, optimised passed the tests
    - Take product of all numbers, then find product of each num except self
      by dividing the product by the num. BUT, can't use division as per descr
    
    - ! Left and right sub products. For each num in nums, we could calculate
      the product to the left and to the right of this number and then just
      multiple them
      
      TODO: There is constant space solution as well
_______________________________________________________________________________

https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


class Solution:
    # Brute force. T: O(N2); S: O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        length = len(nums)
        for i in range(length):
            product = 1
            for j in range(length):
                if j == i:
                    continue
                product *= nums[j]
            out.append(product)
        return out

    # Optimised brute force. T: worst case O(N2), best case ~ O(N); S: O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        length = len(nums)
        calculated_products = {}
        for i in range(length):
            if nums[i] in calculated_products:
                out.append(calculated_products[nums[i]])
                continue

            product = 1
            for j in range(length):
                if j == i:
                    continue
                product *= nums[j]

            calculated_products[nums[i]] = product
            out.append(product)

        return out

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # TODO: Fix me: division based
        # product = 1
        # for num in nums:
        #     if num == 0:
        #         continue
        #     product *= num
        #
        # out = []
        # for num in nums:
        #     if num != 0:
        #         out.append(product // num)
        #     else:
        #         out.append(product)
        # return out
        pass

    # Good one - T: O(N); S: O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        out = []
        product_left = [0] * length
        product_right = [0] * length

        # Element at index 0 is 1 as the leftmost element in nums doesn't have
        # any numbers to the left
        product_left[0] = 1
        for i in range(1, length):
            product_left[i] = nums[i - 1] * product_left[i - 1]

        product_right[length - 1] = 1
        for i in reversed(range(length - 1)):
            product_right[i] = nums[i + 1] * product_right[i + 1]

        for i in range(length):
            out.append(product_left[i] * product_right[i])
        return out
