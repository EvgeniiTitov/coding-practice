from typing import List


# TODO: Proper solution: BS, D&C etc


"""
Summary: Dummy solution O(N2) - find the shortest str, then for each char in
the shortest string, check whether chars in other strings at the same index 
match
------------------------------------------------------------------------------

https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of 
strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:

    # T: O(n2), S: O(n)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""

        strs.sort(key=len)  # O(n log n)
        shortest_word = strs.pop(0)
        str_out = []
        for i in range(len(shortest_word)):
            char = shortest_word[i]
            for word in strs:
                if word[i] != char:
                    return "".join(str_out)
            str_out.append(char)
        return "".join(str_out)

    # T: O(n2), S: O(1)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]
        return shortest


def main():
    pass


if __name__ == "__main__":
    main()
