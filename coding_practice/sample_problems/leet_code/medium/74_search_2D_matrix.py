from typing import List


"""
Summary: 2D matrix is sorted, so you could think of it as a flat array. The 
only difficulty is translating index in a 1D array to an i, j in the 2D matrix
_______________________________________________________________________________

https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value target in an m x n 
integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""


class Solution:
    # T: O(log N); S: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        items_per_row = len(matrix[0])
        left, right = 0, n_rows * items_per_row - 1
        while left <= right:
            middle_index = (left + right) // 2
            middle_index_value = self._get_item_at_index(
                matrix, items_per_row, middle_index
            )
            if middle_index_value == target:
                return True
            elif middle_index_value < target:
                left = middle_index + 1
            else:
                right = middle_index - 1
        return False

    def _get_item_at_index(
        self, matrix: List[List[int]], items_per_row: int, index: int
    ) -> int:
        return matrix[index // items_per_row][index % items_per_row]


def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(Solution().searchMatrix(matrix, target))


if __name__ == "__main__":
    main()
