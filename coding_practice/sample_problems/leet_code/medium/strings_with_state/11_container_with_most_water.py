from typing import List


"""
Summary: Start at both end. The trick is not to prioritise the next larger bar
(trying to move the pointer that would result in a larger one), but you need to
move the smaller pointer in the hopes to get the taller one -> increase area
_______________________________________________________________________________

https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines 
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the 
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array 
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the 
container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Container:
S = a * b
______
|    |
|    | b
|____|
  a
"""


class Solution:
    # Brute force. Time limit exceeded: 48 / 60 test cases passed; T: O(N2)
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        max_amount_water = 0
        for i in range(length):
            for j in range(i + 1, length):
                min_height = min(height[i], height[j])
                length_container = j - i
                max_amount_water = max(
                    max_amount_water, min_height * length_container
                )
        return max_amount_water

    # T: O(N), S: O(1)
    def maxArea(self, height: List[int]) -> int:
        def _calculate_area(left: int, right: int) -> int:
            width = right - left
            min_height = min(height[left], height[right])
            return min_height * width

        length = len(height)
        left, right = 0, length - 1
        max_area = 0
        while left < right:
            temp_max_area = _calculate_area(left, right)
            max_area = max(max_area, temp_max_area)

            # Move the shorter one hoping to get a higher bar -> larger area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

            # ! That's quite the opposite logic, no point trying to get a
            # larger bar on either side if the other one is tiny! Move the smaller
            # if height[left + 1] > height[left]:
            #     left += 1
            # elif height[right - 1] > height[right]:
            #     right -= 1
            # else:
            #     left += 1
            #     right -= 1

        return max_area


def main():
    height = [1, 3, 2, 5, 25, 24, 5]
    print(Solution().maxArea(height))


if __name__ == "__main__":
    main()
