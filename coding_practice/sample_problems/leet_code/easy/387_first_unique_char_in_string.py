import typing as t


"""
Summary: Find out how many times each char appears. Collect all chars that
are unique (aka appear once only). Then find the first unique char in the str
_______________________________________________________________________________

https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string s, find the first non-repeating character in it and return its 
index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
"""


class Solution:

    # T: O(N); S: (N)
    def firstUniqChar(self, s: str) -> int:
        from collections import defaultdict

        char_counts = defaultdict(int)
        for char in s:
            char_counts[char] += 1

        # If defaultdict is not allowed
        # char_counts = {}
        # for char in s:
        #     if char in char_counts:
        #         char_counts[char] += 1
        #     else:
        #         char_counts[char] = 1

        unique_chars = set()
        for char, times_seen in char_counts.items():
            if times_seen == 1:
                unique_chars.add(char)

        for i, char in enumerate(s):
            if char in unique_chars:
                return i
        return -1


