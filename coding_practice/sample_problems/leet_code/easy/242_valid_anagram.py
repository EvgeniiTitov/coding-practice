import typing as t


"""
Summary:
Multiple ways, some allow constant space!
_______________________________________________________________________________

https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false 
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""


class Solution:
    # Suuuuper slow. T: O(N2); S: O(N)
    def isAnagram(self, s: str, t: str) -> bool:
        t_letters = list(t)
        for char in s:
            if char not in t_letters:
                return False
            t_letters.remove(char)
        return not len(t_letters)

    # A bit quicker. T: O(N log N); S: O(N)
    def isAnagram(self, s: str, t: str) -> bool:

        def _get_numerical_representation(s: str) -> int:
            numbers = []
            for char in s:
                numbers.append(ord(char))
            numbers.sort()
            return int("".join(map(str, numbers)))
        return _get_numerical_representation(s) == _get_numerical_representation(t)

    # Substantially quicker. T: O(N log N); S: O(N), maybe O(1)?
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_l = list(s)
        s_t = list(t)
        s_l.sort()
        s_t.sort()
        return s_l == s_t

    # T: O(N log N); S: O(1)
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        from collections import defaultdict

        counts_s = defaultdict(int)
        counts_t = defaultdict(int)
        for i in range(len(s)):
            counts_s[s[i]] += 1
            counts_t[t[i]] += 1

        for char_s, value_s in counts_s.items():
            value_t = counts_t.get(char_s)
            if value_s != value_t:
                return False
        return True
