import typing as t


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/valid-parenthesis-string/

Given a string s containing only three types of characters: '(', ')' and '*', 
return true if s is valid.

The following rules define a valid string:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left 
  parenthesis '(' or an empty string "".
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true


((
))
(*
*)
((*))
"""


class Solution:

    def checkValidString(self, s: str) -> bool:
        from collections import defaultdict
        chars_frequency = defaultdict(int)
        for char in s:
            chars_frequency[char] += 1

        opening_brace = chars_frequency["("]
        closing_brace = chars_frequency[")"]
        astrix = chars_frequency["*"]

        greater = max(opening_brace, closing_brace)
        smaller = min(opening_brace, closing_brace)
        return astrix >= greater - smaller


    # def checkValidString(self, s: str) -> bool:
    #     stack = []
    #     for char in s:
    #         # if char is (, add to the stack
    #         # if its ), pop value off the stack - expect ( or *
    #         # if its *, check stack and the next item? decide what to do with it:
    #             # if next ) and in the stack (, cancel them, add * to the stack?
    #         if char == "(":
    #             stack.append(char)
    #
    #         elif char == ")":
    #             if not len(stack):
    #                 return False
    #             previous_value = stack.pop()
    #             if previous_value not in "(*":
    #                 return False
    #
    #         elif char == "*":
    #             stack.append(char)
    #
    #     return "(" not in stack and ")" not in stack



    # This is just wrong. Based on wrong assumptions. ((...() could be valid
    # def checkValidString(self, s: str) -> bool:
    #     length = len(s)
    #     if length == 1:
    #         return False
    #
    #     left, right = 0, length - 1
    #     while left <= right:
    #         left_char = s[left]
    #         right_char = s[right]
    #         if left_char == "(" and right_char not in "*)":
    #             return False
    #         elif right_char == ")" and left_char not in "(*":
    #             return False
    #         left += 1
    #         right -= 1
    #     return True


def main():
    s = "((((()(()()()*()(((((*)()*(**(("
    # s = "()"
    print(Solution().checkValidString(s))


if __name__ == '__main__':
    main()
