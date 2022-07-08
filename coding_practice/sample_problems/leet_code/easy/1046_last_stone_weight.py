from typing import List
import heapq


"""
Summary: Heapq allows to always get access to the 2 heaviest stones in O(1).
The resulting stone gets added to the heap. Iterate until nothing or just 1 
stone is left
_______________________________________________________________________________

https://leetcode.com/problems/last-stone-weight/

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest 
two stones and smash them together. Suppose the heaviest two stones have 
weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has 
new weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, 
return 0.


Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last 
"""


class Solution:
    # T: O(N log N); Actually could be O(N2) cuz you heapify in the loop. Yet
    # faster than 99.58% submissions?
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)  # O(N)
        while True:  # O(N)

            if len(stones) == 1:
                return stones[0]
            elif not len(stones):
                return 0

            heaviest_1 = heapq._heappop_max(stones)  # O(log N)
            heaviest_2 = heapq._heappop_max(stones)  # O(log N)
            if heaviest_1 == heaviest_2:
                continue

            remains = heaviest_1 - heaviest_2
            heapq.heappush(stones, remains)  # O(log N)
            heapq._heapify_max(stones)

    # From the solutions
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Make all the stones negative. We want to do this *in place*, to keep the
        # space complexity of this algorithm at O(1). :-)
        for i in range(len(stones)):
            stones[i] *= -1

        # Heapify all the stones.
        heapq.heapify(stones)

        # While there is more than one stone left, remove the two
        # largest, smash them together, and insert the result
        # back into the heap if it is non-zero.
        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)

        # Check if there is a stone left to return. Convert it back
        # to positive.
        return -heapq.heappop(stones) if stones else 0
