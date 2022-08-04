from typing import List


"""
Summary: Sliding window approach - we look at 3 elements at once: i - 1, i and 
i + 1. If current == left == right ==  0, counter +1, we can plant a flower,
l[current] = 1 and move on. 
Smart to add 0s to both sides of the list to avoid complicated edge cases
_______________________________________________________________________________

https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and some are
not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty
and 1 means not empty, and an integer n, return if n new flowers can be 
planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        count = 0
        for i in range(1, len(flowerbed) - 1):
            left = flowerbed[i - 1]
            current = flowerbed[i]
            right = flowerbed[i + 1]
            if left == current == right == 0:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True

        return count >= n

    # Without adding padding to both sides
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (
                    flowerbed[i + 1] == 0
                )

                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n


def main():
    l = [1, 0, 0, 0, 1]
    print(Solution().canPlaceFlowers(l, 1))


if __name__ == "__main__":
    main()
