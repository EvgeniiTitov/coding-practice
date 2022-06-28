import typing as t


"""
Summary: Replicate how you would add numbers by hand
_______________________________________________________________________________

https://leetcode.com/problems/add-strings/

Given two non-negative integers, num1 and num2 represented as string, return 
the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling 
large integers (such as BigInteger). You must also not convert the inputs to 
integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"
"""


class Solution:
    # Mine
    def addStrings(self, num1: str, num2: str) -> str:
        num1_len = len(num1)
        num2_len = len(num2)
        longest = max(num1_len, num2_len)
        carry_over = 0
        number_out = []
        ascii_zero = ord("0")
        for i in range(1, longest + 1):
            try:
                number_1 = ord(num1[-i]) - ascii_zero
            except:
                number_1 = 0
            try:
                number_2 = ord(num2[-i]) - ascii_zero
            except:
                number_2 = 0
            sum_ = number_1 + number_2 + carry_over
            value = sum_ % 10
            carry_over = sum_ // 10
            number_out.append(str(value))  # !
        if carry_over:
            number_out.append(str(carry_over))
        return "".join(reversed(number_out))

    # From solutions
    def addStrings(self, num1: str, num2: str) -> str:
        res = []

        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            p1 -= 1
            p2 -= 1

        if carry:
            res.append(carry)

        return ''.join(str(x) for x in res[::-1])


def main():
    num1 = "1"
    num2 = "9"
    print(Solution().addStrings(num1, num2))


if __name__ == '__main__':
    main()
