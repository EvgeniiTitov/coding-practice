import typing


"""
Summary: Weird problem fr
_______________________________________________________________________________

https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same 
character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
"""


class Solution:

    # 42 / 44 - not sure why it's not working though
    def isIsomorphic(self, s: str, t: str) -> bool:

        def _get_unique_chars_order(string: s) -> str:
            if not string:
                return ""

            unique_char_counts = []
            prev_char = string[0]
            count = 1
            for char in string[1:]:
                if char == prev_char:
                    count += 1
                else:
                    unique_char_counts.append(str(count))
                    prev_char = char
                    count = 1

            unique_char_counts.append(str(count))
            return "".join(unique_char_counts)

        def _get_number_of_unique_chars(string: s) -> int:
            return len(set(string))

        return (
                _get_unique_chars_order(s) == _get_unique_chars_order(t)
                and _get_number_of_unique_chars(s) == _get_number_of_unique_chars(t)
        )

    # Smart
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))




def main():
    print(Solution().isIsomorphic("bbbaaaba", "aaabbbba"))


if __name__ == '__main__':
    main()
