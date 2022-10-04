from typing import List


"""
Summary:
    Brute force: For each element, max() the slice from the element to the right
    
    Single pass: Iterate in reverse order, for each item the greatest element to
    its right is either the element right to its right (index +1) OR some other 
    max value we've encountered to the right. 
_______________________________________________________________________________

https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Given an array arr, replace every element in that array with the greatest 
element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
"""


class Solution:

    # T: O(N); S: O(N)
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)

        if length == 0:
            return []
        elif length == 1:
            return [-1]

        max_values = []
        for i in range(length - 2, -1 , -1):  # O(N)
            if i == length - 2:
                max_values.append(arr[i + 1])
            else:
                prev_max = max_values[-1]
                curr_value = arr[i + 1]
                max_values.append(max(prev_max, curr_value))

        max_values.reverse()  # O(N)
        max_values.append(-1)
        return max_values

    # T: O(N2); S: O(N)
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)

        if length == 0:
            return []
        elif length == 1:
            return [-1]

        arr_out = []
        for i, element in enumerate(arr):  # O(N)
            if i == length - 1:
                arr_out.append(-1)
            else:
                max_on_right = max(arr[i + 1: length])  # O(N)
                arr_out.append(max_on_right)
        return arr_out


def main():
    print(Solution().replaceElements(
        arr=[17,18,5,4,6,1]
    ))


if __name__ == '__main__':
    main()
