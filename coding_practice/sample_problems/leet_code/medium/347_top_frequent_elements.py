from typing import List


"""
Summary: Calculate how many times each element appears. To pick N most frequent
ones: a) sort the array (slow) or b) use a heap!
_______________________________________________________________________________

https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""


class Solution:

    # T: O(N log N);
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        if length == 1:
            return nums

        from collections import defaultdict
        elements_count = defaultdict(int)
        for num in nums:
            elements_count[num] += 1

        popularity_pairs = []
        for num, count in elements_count.items():
            popularity_pairs.append((num, count))

        popularity_pairs.sort(key=lambda e: e[1], reverse=True)  # Slow N log N

        return [
            pair[0] for pair in popularity_pairs[:k]
        ]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        if length == 1:
            return nums

        from collections import defaultdict
        elements_count = defaultdict(int)
        for num in nums:
            elements_count[num] += 1

        popularity_pairs = []
        for num, count in elements_count.items():
            popularity_pairs.append((-count, num))

        import heapq
        heapq.heapify(popularity_pairs)  # in-place heapify -> cost O(N) time
        out = []
        for _ in range(k):
            out.append(heapq.heappop(popularity_pairs)[1])  # log N!

        # ! OR use heapq.nlargest()
        return out
