from typing import Tuple


"""
Summary: Proper DP way is not complete. Other brute force approaches are
possible.
_______________________________________________________________________________

https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""


class Solution:

    # My brute force - slow (O(n2))
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if len(s) == 1:
            return s

        def is_string_a_palindrom(s: str) -> bool:
            return s == s[::-1]

        s_length = len(s)
        longest_poli_substr = s[0]  # fair to assume that
        for i in range(s_length):
            for j in range(i + 1, s_length):
                substring = s[i : j + 1]
                substring_length = len(substring)

                if substring_length < len(longest_poli_substr):
                    continue

                if is_string_a_palindrom(substring):
                    longest_poli_substr = substring

        return longest_poli_substr

    # Expand around centre
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return s
        if len(s) == 1:
            return s

        def expand_around_centre(s: str, left: int, right: int) -> int:
            """
            Move pointers left and right as long as the values of left and
            right are the same
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start, end = 0, 0
        for i in range(len(s)):
            len_1 = expand_around_centre(s, i, i)
            len_2 = expand_around_centre(s, i, i + 1)
            length = max(len_1, len_2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start : end + 1]

    # Top-down DP
    # TODO: Complete me - cannot come up with an idea how to return a string
    #       as we keep shrinking it down when left and right chars match. Return
    #       2 values? An extra argument? Current longest?
    def longestPalindrome(self, s: str) -> str:

        def _find_longest_pali(
            s: str, left: int, right: int
        ) -> Tuple[int, int]:
            if left > right:
                return None, None
            elif left == right:
                return left, right

            if s[left] == s[right]:
                return _find_longest_pali(s, left + 1, right - 1)
            else:
                option1 = _find_longest_pali(s, left + 1, right)
                option2 = _find_longest_pali(s, left, right - 1)
                return max(option1, option2, key=len)

        return _find_longest_pali(s, 0, len(s) - 1)[0]

    # SOLVES SIMILAR PROBLEM BUT RETURNS THE MAX SIZE INSTEAD OF AN ACTUAL STR
    def longestPalindrome(self, s: str) -> int:

        def _find_longest_pali(
            s: str, left: int, right: int
        ) -> int:
            if left > right:
                return 0
            elif left == right:
                return 1

            if s[left] == s[right]:
                return 2 + _find_longest_pali(s, left + 1, right - 1)
            else:
                option1 = _find_longest_pali(s, left + 1, right)
                option2 = _find_longest_pali(s, left, right - 1)
                return max(option1, option2)

        return _find_longest_pali(s, 0, len(s) - 1)


def main():
    s = "ccccaabbaabbddd"
    print(Solution().longestPalindrome(s))


if __name__ == "__main__":
    main()
