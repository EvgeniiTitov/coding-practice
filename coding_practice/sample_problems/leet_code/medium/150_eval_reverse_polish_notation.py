from typing import List


"""
Summary: The idea is to use a stack. You iterate over tokens pushing them on
the stack if its not an operator. When you found an operator, pop 2 items off
the stack, apply operator towards them and push result onto the stack.

!
"/": lambda a, b: a // b if a > 0 and b > 0 else math.ceil(a / b)
is not quite correct, use just
"/": lambda a, b: int(a / b)
for trancating towards zero
_______________________________________________________________________________

https://leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or 
another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means 
the expression would always evaluate to a result, and there will not be any 
division by zero operation.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        stack = []
        for token in tokens:
            if token in operators:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                operator = operators[token]
                result = operator(operand_1, operand_2)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]


def main():
    print(
        Solution().evalRPN(
            # tokens=["2","1","+","3","*"]
            # tokens=["4","13","5","/","+"],
            tokens=[
                "10",
                "6",
                "9",
                "3",
                "+",
                "-11",
                "*",
                "/",
                "*",
                "17",
                "+",
                "5",
                "+",
            ]
        )
    )


if __name__ == "__main__":
    main()
