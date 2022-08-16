from coding_practice.utils import print_grid


"""
Summary:

Subproblems have natural size ordering - the largest subproblems come first, 
and then we deal with smaller and smaller subproblems till they are as simple
as a single char in every word. 
Each subproblem is represented as a pair of indices (p1, p2), --> there are
len(text1) * len(text2) such subproblems. 
We could iterate through subproblems starting from the smallest ones and store
the answer for each. When dealing with the larger subproblems, the smaller ones
they depend on will already have been solved. 
Could use a 2D array to do it. 



_______________________________________________________________________________

https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common 
subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string 
with some characters (can be none) deleted without changing the relative order 
of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to 
both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""


class Solution:

    # D&C
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def _find_lcs(s1: str, s2: str, p1: int, p2: int) -> int:
            # Base cases:
            # 1. Out of bounds
            if p1 >= len(s1):
                return 0
            if p2 >= len(s2):
                return 0

            if s1[p1] == s2[p2]:
                return 1 + _find_lcs(s1, s2, p1 + 1, p2 + 1)
            else:
                skip_char_s1 = _find_lcs(s1, s2, p1 + 1, p2)
                skip_char_s2 = _find_lcs(s1, s2, p1, p2 + 1)
                return max(skip_char_s1, skip_char_s2)

        return _find_lcs(text1, text2, 0, 0)

    # Top-down DP
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def _cache(func):
            _cache = {}
            def wrapper(s1: str, s2: str, p1: int, p2: int) -> int:
                if (p1, p2) not in _cache:
                    _cache[(p1, p2)] = func(s1, s2, p1, p2)
                return _cache[(p1, p2)]
            return wrapper

        @_cache
        def _find_lcs(s1: str, s2: str, p1: int, p2: int) -> int:
            # Base cases:
            # 1. Out of bounds
            if p1 >= len(s1):
                return 0
            if p2 >= len(s2):
                return 0

            if s1[p1] == s2[p2]:
                return 1 + _find_lcs(s1, s2, p1 + 1, p2 + 1)
            else:
                skip_char_s1 = _find_lcs(s1, s2, p1 + 1, p2)
                skip_char_s2 = _find_lcs(s1, s2, p1, p2 + 1)
                return max(skip_char_s1, skip_char_s2)

        return _find_lcs(text1, text2, 0, 0)

    # Bottom-up DP
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [
            [0] * (len(text2) + 1)
            for _ in range(len(text1) + 1)
        ]
        print_grid(grid)

        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                # If the corresponding chars are the same
                if text2[col] == text1[row]:
                    grid[row][col] = 1 + grid[row + 1][col + 1]
                else:
                    grid[row][col] = max(
                        grid[row + 1][col], grid[row][col + 1]
                    )
                print_grid(grid)

        return grid[0][0]


def main():
    print(Solution().longestCommonSubsequence(
        text1="attag",
        text2="gtgatcg"

        # text1="gtgatcg",
        # text2="attag"

    ))


if __name__ == '__main__':
    main()
