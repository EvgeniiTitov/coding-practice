
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
'''


class Solution:

    # This one solves a slightly different problem - any order is allowed:
    # "([)]" returns True but Leetcode expects False
    # def isValid(self, s: str) -> bool:
    #     braces_encountered = {
    #         "()": 0, "{}": 0, "[]": 0
    #     }
    #     opening_chars = {"(", "[", "{"}
    #     for char in s:
    #         if char in "()":
    #             if char in opening_chars:
    #                 braces_encountered["()"] += 1
    #             else:
    #                 braces_encountered["()"] -= 1
    #         elif char in "{}":
    #             if char in opening_chars:
    #                 braces_encountered["{}"] += 1
    #             else:
    #                 braces_encountered["{}"] -= 1
    #         elif char in "[]":
    #             if char in opening_chars:
    #                 braces_encountered["[]"] += 1
    #             else:
    #                 braces_encountered["[]"] -= 1
    #
    #     return all(v == 0 for v in braces_encountered.values())

    # My solution
    def isValid(self, s: str) -> bool:
        stack = []
        braces_mapping = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in braces_mapping:
                if not len(stack):
                    return False
                opening_brace_expected = braces_mapping[char]
                actual_brace = stack.pop(-1)
                if opening_brace_expected != actual_brace:
                    return False
            else:
                stack.append(char)
        return True if not len(stack) else False

    # Solution from comments
    def isValid(self, s: str) -> bool:
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []


def main() -> None:
    s = "(((((())))))"
    print(Solution().isValid(s))


if __name__ == '__main__':
    main()
