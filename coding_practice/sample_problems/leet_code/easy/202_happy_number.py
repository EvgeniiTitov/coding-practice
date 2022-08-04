import typing as t


"""
Summary: 
    - Heavily underestimated the problem. 4 could result in 16, 16 -> 37 etc
    So, keep track of numbers we've seen so far. If a number != 1 but we've 
    already seen it --> cycle!
    - Use Floyd's Cycle Finding Algorithm as we're dealing with implicit LL 
    where each number points to the next one
_______________________________________________________________________________

https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the 
  squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it 
  loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.


Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false


Floyd's Cycle Finding Algorithm:
The chain we get by repeatedly calling getNext(n) is an implicit LinkedList. 
Implicit means we don't have actual LinkedNode's and pointers, but the data 
does still form a LinkedList structure. The starting number is the head "node" 
of the list, and all the other numbers in the chain are nodes. The next pointer 
is obtained with our getNext(n) function above.
"""


class Solution:

    def isHappy(self, n: int) -> bool:
        char_numbers = [int(char) for char in str(n)]
        seen = set()
        while True:
            summed = sum(num ** 2 for num in char_numbers)
            if summed == 1:
                return True

            if summed in seen:
                return False
            seen.add(summed)
            char_numbers = [int(char) for char in str(summed)]

    # Alternative: Floyd's Cycle-Finding Algorithm
    def isHappy(self, n: int) -> bool:
        def _get_next(n: int) -> int:
            if n == 0 or n == 1:
                return n
            return sum(int(char) ** 2 for char in str(n))

        slow_runner = n
        fast_runner = _get_next(n)
        while True:
            if slow_runner == 1 or fast_runner == 1:
                return True
            if slow_runner == fast_runner:
                return False
            slow_runner = _get_next(slow_runner)
            fast_runner = _get_next(_get_next(fast_runner))


def main():
    print(Solution().isHappy(19))


if __name__ == "__main__":
    main()
