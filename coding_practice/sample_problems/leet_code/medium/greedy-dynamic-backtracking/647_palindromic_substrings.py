import typing as t


"""
Thoughts:
    The solution needs pointers, how do we pick them?
        - Left, right (ends of the string)
        - Both at the start
        - Both at the middle and then expand from there
    

Summary:
_______________________________________________________________________________

https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""


class Solution:

    # Brute force. Passed the checks lol; T: O(N3); S: O(1)
    def countSubstrings(self, s: str) -> int:

        def _check_if_palindrom(string: str) -> bool:
            return string == string[::-1]

        counter = 0
        length = len(s)
        for i in range(length):
            for j in range(i, length):  # Could start from the same index
                substring = s[i: j + 1]
                if _check_if_palindrom(substring):
                    counter += 1

        return counter

    # D&C
    def countSubstrings(self, s: str) -> int:

        def _count_palindromic_substrings(
            string: str, left: int, right: int
        ) -> int:
            # TODO: Start from the centre - expand
            pass

        length = len(s)
        if length == 1:
            return 1

        return _count_palindromic_substrings(s, 0, length - 1)


def main():
    print(Solution().countSubstrings(
        s="aaa"
    ))


if __name__ == '__main__':
    main()
