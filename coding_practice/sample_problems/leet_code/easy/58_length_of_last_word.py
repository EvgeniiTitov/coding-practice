import typing


"""
Summary:
    Linear time looping from right to left looking only for the first word
    
    Python's built-in .split()
_______________________________________________________________________________

https://leetcode.com/problems/length-of-last-word/

Given a string s consisting of words and spaces, return the length of the 
last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


class Solution:

    # T: O(N)
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        word_length = 0
        word_started = False
        for i in range(length - 1, -1, -1):
            if s[i] == " " and not word_started:
                continue
            elif s[i] == " " and word_started:
                return word_length
            else:
                if not word_started:
                    word_started = True

                word_length += 1

        return word_length

    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])