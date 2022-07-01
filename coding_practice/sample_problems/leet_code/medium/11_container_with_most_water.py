from typing import List


"""
Summary:
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
