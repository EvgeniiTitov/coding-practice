from typing import List


"""
Summary:
    The trick is to keep strings state as dicts and then compare them. Avoid
    regenerating string char count from scratch after every step, its too 
    expensive, rather use two pointers and update the state after moving them
_______________________________________________________________________________

https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices of p's 
anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


class Solution:

    # Brute force. T ~ O(N2). Time Limit Exceeded
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import defaultdict

        def _get_chars_count(string: str) -> dict:
            char_counts = defaultdict(int)
            for char in string:  # O(N)
                char_counts[char] += 1
            return char_counts

        indices = []
        p_chars = _get_chars_count(p)
        for i in range(len(s) - len(p) + 1):  # O(N)
            s_substring = s[i: i + len(p)]
            if p_chars == _get_chars_count(s_substring):
                indices.append(i)

        return indices

    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import defaultdict

        def _get_chars_count(string: str) -> dict:
            char_counts = defaultdict(int)
            for char in string:  # O(N)
                char_counts[char] += 1
            return char_counts

        indices = []
        p_counts = _get_chars_count(p)
        s_subset_counts = _get_chars_count(s[: len(p) - 1])

        left, right = 0, len(p) - 1
        while right < len(s):
            s_subset_counts[s[right]] += 1

            if p_counts == s_subset_counts:
                indices.append(left)

            s_subset_counts[s[left]] -= 1
            if s_subset_counts[s[left]] == 0:
                del s_subset_counts[s[left]]

            left += 1
            right += 1

        return indices


def main():
    print(Solution().findAnagrams(
        s="abab",
        p="ab"
    ))


if __name__ == '__main__':
    main()
