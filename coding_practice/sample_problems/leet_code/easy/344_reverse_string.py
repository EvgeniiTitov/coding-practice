from typing import List


"""
Summary: Built-in or swap left and right in place till you reach the middle
_______________________________________________________________________________

https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an 
array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

        # OR this
        s.reverse()

    # T: O(N); S: O(1)
    def reverseString(self, s: List[str]) -> None:
        # In case built in methods are not allowed
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
