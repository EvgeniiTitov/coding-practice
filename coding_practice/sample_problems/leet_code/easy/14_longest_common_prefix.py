from typing import List


'''
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


class Solution:

    # T: O(n2), S: O(n)
    def longestCommonPrefix(self, strs: List[str]) -> str:
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


def main():
    pass


if __name__ == '__main__':
    main()
