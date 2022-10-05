import typing


"""
Summary:
    Brute force: Iterate over T while keeping track of S chars we expect to find
    it T. 
    
    Two pointers: Iterate over 2 strings in a while loop incrementing S pointer
    every time we find the char we expect in T. If reached the end of S, then
    we cool
    
    D&C: For fun, exceptionally slow, recursively remove an element until T
    becomes the same length as S and then check if they match. 
_______________________________________________________________________________

https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original 
string by deleting some (can be none) of the characters without disturbing the 
relative positions of the remaining characters. (i.e., "ace" is a subsequence
of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "mahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution:

    # Brute force. Accepted but T: O(N^2); S: O(N)
    def isSubsequence(self, s: str, t: str) -> bool:

        if not len(s):
            return True

        s_chars = list(s)
        curr_char = s_chars.pop(0)
        found = False
        for char in t:  # O(N)
            if curr_char == char:
                if not len(s_chars):
                    found = True
                    break
                else:
                    curr_char = s_chars.pop(0)  # O(N)

        return found

    # Two pointers. T: O(N); S: O(1)
    def isSubsequence(self, s: str, t: str) -> bool:
        s_length, t_length = len(s), len(t)
        if not s_length:
            return True

        pointer_1, pointer_2 = 0, 0
        while pointer_2 < t_length and pointer_1 < s_length:
            s_char = s[pointer_1]
            t_char = t[pointer_2]

            if s_char == t_char:
                pointer_1 += 1

            pointer_2 += 1

        return pointer_1 == s_length

    # Not greedy D&C. Obnoxiously slow haha. T: ~ O(2 ^ N).
    def isSubsequence(self, s: str, t: str) -> bool:

        def _find_if_subsequence(s: str, t: str) -> bool:
            # Base case
            if len(t) == len(s):
                return s == t

            for i in range(len(t)):
                new_t = t[:i] + t[i + 1:]  # !
                if _find_if_subsequence(s, new_t):
                    return True

            return False

        if not len(s):
            return True

        return _find_if_subsequence(s, t)


def main():
    print(Solution().isSubsequence(
        s="abc",
        t="ahbjckd"
    ))


if __name__ == '__main__':
    main()
