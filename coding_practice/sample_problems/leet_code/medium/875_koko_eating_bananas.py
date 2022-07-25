from typing import List


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/koko-eating-bananas/

Koko loves to eat bananas. There are n piles of bananas, the ith pile has 
piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses 
some pile of bananas and eats k bananas from that pile. If the pile has less 
than k bananas, she eats all of them instead and will not eat any more bananas 
during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas 
before the guards return.

Return the minimum integer k such that she can eat all the bananas within 
h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Say, pile is 5 bananas. Koko's speed (S) is 1 ban/hour. Total time: 5 / S = 5
"""


class Solution:
    # Iteratively finding the solution. The problem we start with very slow
    # speed and check every one on our way up -> optimise with BS
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        speed = 1
        while True:
            time_spent = 0
            for pile in piles:
                time_spent += math.ceil(pile / speed)

            if time_spent <= h:
                return speed
            else:
                speed += 1

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        left, right = 1, max(piles)
        while left < right:
            mid_speed = (left + right) // 2
            time_spent = 0
            for pile in piles:
                time_spent += math.ceil(pile / mid_speed)

            if time_spent <= h:
                right = mid_speed
            else:
                left = mid_speed + 1

        return right


def main():
    print(Solution().minEatingSpeed(
        piles=[30,11,23,4,20],
        h=6
    ))


if __name__ == '__main__':
    main()
