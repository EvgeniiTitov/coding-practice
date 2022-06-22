from typing import List


'''
https://leetcode.com/problems/unique-number-of-occurrences/

Given an array of integers arr, return true if the number of occurrences of 
each value in the array is unique, or false otherwise.

 
Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values
have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import defaultdict

        occurrences = defaultdict(int)
        for number in arr:
            occurrences[number] += 1
        unique_numbers = set(occurrences.values())
        return len(occurrences.keys()) == len(unique_numbers)
