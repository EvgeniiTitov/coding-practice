from typing import List


'''
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

Given an integer n, return any array containing n unique integers such that 
they add up to 0.

Example 1:
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:
Input: n = 3
Output: [-1,0,1]

Example 3:
Input: n = 1
Output: [0]


Thoughts:
Some examples:
n = 1: ans = [0]
n = 2: ans = [-1,1]
n = 3: ans = [-1,0,1]
n = 4: ans = [-2,-1,1,2]
n = 5: ans = [-2,-1,0,1,2]

So, we should return an array where the values are symmetric.
If n%2 is not equal to zero (n is odd), we append 0 to the answer list.
The maximum value is equal to n//2; and the minimum value is equal to -n//2.
So, we use a for loop; and each time we add -i and i to the answer list.
'''


class Solution:
    def sumZero(self, n: int) -> List[int]:
        half_n = n // 2
        out = []
        if n % 2:
            out.append(0)
        for i in range(1, half_n + 1):
            out.append(i)
            out.append(-i)
        return out
