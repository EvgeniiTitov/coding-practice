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

"""


class Solution:

    """
    The idea is we first treat all * as left --> ensure left ( is always >= )
    If its the case and left brace + * >= right brace, it means some * could be
    empty strings instead of (, so the string is valid

    Then, we do the same from the right treating all * as ) and making sure
    right brace + * >= left brace, then the string is valid as some * could be
    turned into " "
    """
    def checkValidString(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "(*":
                stack.append(char)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False

        stack = []
        for char in s[::-1]:
            if char in "*)":
                stack.append(char)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False
        return True

    # Ugly ass Brutal Solution
    def checkValidString(self, s):
        if not s: return True
        A = list(s)
        self.ans = False

        def solve(i):
            if i == len(A):
                self.ans |= valid()
            elif A[i] == '*':
                for c in '() ':
                    A[i] = c
                    solve(i + 1)
                    if self.ans: return
                A[i] = '*'
            else:
                solve(i + 1)

        def valid():
            bal = 0
            for x in A:
                if x == '(': bal += 1
                if x == ')': bal -= 1
                if bal < 0: break
            return bal == 0

        solve(0)
        return self.ans

    # D & C like brute force approach - CLOSE yet fails. The idea is for each
    # * we consider 3 possibilities: " ", (, ). Like a tree.
    # T: O (N * 3 ^ N); S: O (N)
    def checkValidString(self, s: str) -> bool:

        # TODO: You could just generate a tree and then once you've reached
        #       the end validate the curr_stack, you tried to combine the two
        #       which overcomplicated the shit out of your solution its disgusting
        def _check_if_valid(
            string: str, curr_index: int, curr_stack: list[str]
        ) -> bool:

            # Base case - processed all string, if its valid, nothing on stack
            if curr_index >= length:
                return not len(curr_stack)

            # If stack's empty (just started), add the first char on it
            if not len(curr_stack):
                curr_char = string[curr_index]
                if curr_char == "*":
                    for char in " ()":
                        if char == " ":
                            is_valid = _check_if_valid(
                                string, curr_index + 1, curr_stack.copy()
                            )
                        else:
                            curr_stack.append(char)
                            is_valid = _check_if_valid(
                                string, curr_index + 1, curr_stack.copy()
                            )
                        if is_valid:
                            return True
                    return False
                else:
                    curr_stack.append(string[curr_index])
                    return _check_if_valid(
                        string, curr_index + 1, curr_stack.copy()
                    )

            # If stack is not empty:
            # If curr char ( -> add to the stack and continue
            # If curr char ) -> needs a closing brace to be valid
            # If curr char * ->
            #   It could be ( or ) or " ". Check whether each results in a
            #   valid string. What to do with " "?
            curr_char = string[curr_index]
            if curr_char == "(":
                curr_stack.append(curr_char)
                return _check_if_valid(
                    string, curr_index + 1, curr_stack.copy()
                )
            elif curr_char == ")":
                prev_char = curr_stack[-1]
                if prev_char == "(":
                    curr_stack.pop()
                    return _check_if_valid(
                        string, curr_index + 1, curr_stack.copy()
                    )
                else:
                    return False
            else:  # Its *
                for char in " ()":
                    if char == " ":
                        is_valid = _check_if_valid(
                            string, curr_index + 1, curr_stack.copy()
                        )
                    elif char == "(":
                        curr_stack.append(char)
                        is_valid = _check_if_valid(
                            string, curr_index + 1, curr_stack.copy()
                        )
                        curr_stack.pop()
                    else:  # )
                        prev = curr_stack[-1]
                        if prev == "(":
                            curr_stack.pop()
                            is_valid = _check_if_valid(
                                string, curr_index + 1, curr_stack.copy()
                            )
                        else:
                            is_valid = False

                    if is_valid:
                        return True
                return False

        length = len(s)
        if length == 0:
            return True  # Is it valid?

        return _check_if_valid(s, 0, [])


def main():
    # s = "((((()(()()()*()(((((*)()*(**(("
    s = "*****"
    print(Solution().checkValidString(s))


if __name__ == "__main__":
    main()
