from typing import List
import heapq


"""
Summary: Heap is the way to go.
_______________________________________________________________________________

https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the kth largest element in a stream. Note that it is 
the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and 
the stream of integers nums.

int add(int val) Appends the integer val to the stream and returns the element 
representing the kth largest element in the stream.
"""


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        # Pop any extra items, we care only about K ones
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Alternative
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)  # add elements using the function below

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # if after adding the new item causes the heap size to increase
        # beyond k, then pop out the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


def main():
    print(KthLargest(k=3, nums=[4, 5, 8, 2]).add(3))


if __name__ == '__main__':
    main()
