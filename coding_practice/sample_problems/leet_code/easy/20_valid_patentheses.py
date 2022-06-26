import typing as t


"""
Summary: Single pass, iterate over the str, add opening braces to the stack,
for closing ones pop off the stack and check whether they match
------------------------------------------------------------------------------

https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

------------------------------------------------------------------------------
Solution with proper stack:
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False
    return stack.size()==0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
"""


class Solution:

    # T: O(N); S: O(N)
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
        return len(stack) == 0

    # T: O(N); S: O(N)
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

    # !NOTE: This one solves a slightly different problem - any order is allowed:
    # "([)]" returns True but Leetcode expects False
    def isValid(self, s: str) -> bool:
        braces_encountered = {"()": 0, "{}": 0, "[]": 0}
        opening_chars = {"(", "[", "{"}
        for char in s:
            if char in "()":
                if char in opening_chars:
                    braces_encountered["()"] += 1
                else:
                    braces_encountered["()"] -= 1
            elif char in "{}":
                if char in opening_chars:
                    braces_encountered["{}"] += 1
                else:
                    braces_encountered["{}"] -= 1
            elif char in "[]":
                if char in opening_chars:
                    braces_encountered["[]"] += 1
                else:
                    braces_encountered["[]"] -= 1

        return all(v == 0 for v in braces_encountered.values())


def main() -> None:
    s = "(((((())))))"
    print(Solution().isValid(s))


if __name__ == "__main__":
    main()
