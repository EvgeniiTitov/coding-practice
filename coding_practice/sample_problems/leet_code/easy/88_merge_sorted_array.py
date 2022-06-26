from typing import List


'''
Summary: 
    Pointers: 2 pointers at the beginning of each array, get values, compare, 
    move the pointer only of the array from which you got the smaller value, 
    there could be more smaller ones. Iterate until one of them reaches the 
    end. Don't forget to append the remaining values of the other one.
------------------------------------------------------------------------------

https://leetcode.com/problems/merge-sorted-array/

You are given two integer arrays nums1 and nums2, sorted in non-decreasing 
order, and two integers m and n, representing the number of elements in 
nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be 
stored inside the array nums1. To accommodate this, nums1 has a length of 
m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a 
length of n.

 
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements 
coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there 
to ensure the merge result can fit in nums1.
'''


class Solution:

    # T: O(n + m); S: O(n)
    def merge(
        self,
        nums1: List[int],
        m: int,
        nums2: List[int],
        n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        out = []
        start_1 = start_2 = 0
        while start_1 < m and start_2 < n:
            value_1 = nums1[start_1]
            value_2 = nums2[start_2]
            if value_1 <= value_2:
                out.append(value_1)
                start_1 += 1
            elif value_1 > value_2:
                out.append(value_2)
                start_2 += 1

        if start_1 < m:
            out.extend(nums1[start_1:m])  # Upper boundary, beyond 0s
        elif start_2 < n:
            out.extend(nums2[start_2:n])  # Upper boundary, beyond 0s

        nums1[:] = out  # ! Modifying the original array

    def merge(
        self,
        nums1: List[int],
        m: int,
        nums2: List[int],
        n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # TODO: Understand this boring ass constant space solution
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1


def main():
    print(Solution().merge(nums1=[2, 0], m=1, nums2=[1], n=1))


if __name__ == '__main__':
    main()
