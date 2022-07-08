from typing import List


"""
Summary: School book like addition with carry over. Or cheeky python only one
_______________________________________________________________________________

https://leetcode.com/problems/plus-one/

You are given a large integer represented as an integer array digits, where 
each digits[i] is the ith digit of the integer. The digits are ordered from 
most significant to least significant in left-to-right order. The large 
integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        incremented_rightmost_number = digits.pop() + 1
        value = incremented_rightmost_number % 10
        carry_over = incremented_rightmost_number // 10
        number_out = [value]

        while len(digits):
            last_digit = digits.pop()
            summed = last_digit + carry_over
            value = summed % 10
            carry_over = summed // 10
            number_out.append(value)

        if carry_over:
            number_out.append(carry_over)

        return reversed(number_out)

    # Cheeky one that works only in Python
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num += 1
        return list(str(num))


def main():
    out = Solution().plusOne([9, 9])
    print(out)


if __name__ == "__main__":
    main()
