from typing import List
import heapq


"""
Summary: Multiple ways. Single sort, heap, etc
_______________________________________________________________________________

https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element 
in the array.

Note that it is the kth largest element in the sorted order, not the kth 
distinct element. 

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""


class Solution:
    # KEKL
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()  # O(N log N)
        return nums[-k]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        for _ in range(k - 1):
            heapq._heappop_max(nums)
        return heapq._heappop_max(nums)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


def main():
    print(Solution().findKthLargest(nums=[3, 1, 2, 5, 6, 4], k=2))


if __name__ == "__main__":
    main()
