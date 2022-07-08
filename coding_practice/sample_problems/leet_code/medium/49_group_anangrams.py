from typing import List


"""
Summary: Single pass. Dict key as sorted anangram chars, value is a list for
all anangrams
_______________________________________________________________________________

https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return 
the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""


class Solution:
    # Time Complexity: O(N KlogK), where N is the length of strs, and K is the
    # maximum length of a string in strs. The outer loop has complexity O(N)
    # as we iterate through each string. Then, we sort each string in O(KlogK) time.
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        length = len(strs)
        if length == 1:
            return [strs]

        def _get_key_from_string(s: str) -> str:
            return "".join(sorted(s))

        from collections import defaultdict

        seen_anangrams = defaultdict(list)
        for string in strs:
            key = _get_key_from_string(string)
            seen_anangrams[key].append(string)

        return list(seen_anangrams.values())  # list() is not required actually
