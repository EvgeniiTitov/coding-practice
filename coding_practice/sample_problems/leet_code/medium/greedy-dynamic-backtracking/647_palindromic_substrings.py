import typing as t


"""
Summary: Brute force is a good start, expanding around center (2N - 1) centres
is a good solution. DP bottom-up is hard to come up with, slow and takes a lot of
space anyways
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

    # T: O(N2); S: O(1)
    def countSubstrings(self, s: str) -> int:

        def _expand_around_centre(centre: int) -> int:
            counter = 0
            left = centre // 2  # // 2 because i [0, 2N - 1]
            right = left + centre % 2
            while left >= 0 and right <= length - 1 and s[left] == s[right]:
                counter += 1
                left -= 1
                right += 1
            return counter

        length = len(s)
        if length == 1:
            return 1

        counter = 0
        for i in range(2 * length - 1):
            counter += _expand_around_centre(i)

        return counter

    # Recursive Brute Force, Time Limit Exceeded, super slow haha
    def countSubstrings(self, s: str) -> int:

        def _is_palindrome(left: int, right: int) -> int:
            if left >= right:
                return 1
            if s[left] != s[right]:
                return 0
            else:
                return _is_palindrome(left + 1, right - 1)

        length = len(s)
        if length == 1:
            return 1
        counter = 0
        for i in range(length):
            for j in range(i, length):
                if _is_palindrome(i, j):
                    counter += 1
        return counter

    # DP bottom-up - the fuck am I doing with my life dude
    # T: O(N2); S: O(N2)
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        if length == 1:
            return 1

        arr = [[0] * length for _ in range(length)]
        counter = 0
        for i in range(length - 1, -1, -1):
            for j in range(i, length):
                arr[i][j] = (
                        s[i] == s[j]
                        and ((j - i + 1) < 3 or arr[i + 1][j - 1])
                )
                counter += arr[i][j]
        return counter


def main():
    print(Solution().countSubstrings(
        s="aaa"
    ))


if __name__ == '__main__':
    main()
