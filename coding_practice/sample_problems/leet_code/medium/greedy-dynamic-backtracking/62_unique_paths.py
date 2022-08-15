import typing as t


"""
Summary: Top-down and bottom-up dps are clean and simple - read the code
_______________________________________________________________________________

https://leetcode.com/problems/unique-paths/

There is a robot on an m x n grid. The robot is initially located at the 
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right 
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or 
right at any point in time.

Given the two integers m and n, return the number of possible unique paths 
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal 
to 2 * 10^9.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach 
the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""


class Solution:

    # D&C
    def uniquePaths(self, m: int, n: int) -> int:

        def _find_paths(m: int, n: int, i: int, j: int) -> int:
            # Base cases
            # 1. Out of bounds
            if i >= m or j >= n:
                return 0

            # 2. Reached the end
            if i == m - 1 and j == n - 1:
                return 1

            path1 = _find_paths(m, n, i + 1, j)
            path2 = _find_paths(m, n, i, j + 1)

            return path1 + path2

        return _find_paths(m, n, 0, 0)

    # Top-down DP
    def uniquePaths(self, m: int, n: int) -> int:

        def _cache(func):
            _cache = {}
            def wrapper(m: int, n: int, i: int, j: int) -> int:
                if (i, j) not in _cache:
                    _cache[(i, j)] = func(m, n, i, j)
                return _cache[(i, j)]
            return wrapper

        @_cache
        def _find_paths(m: int, n: int, i: int, j: int) -> int:
            # Base cases
            # 1. Out of bounds
            if i >= m or j >= n:
                return 0

            # 2. Reached the end
            if i == m - 1 and j == n - 1:
                return 1

            # Sum paths when going right and bottom
            path1 = _find_paths(m, n, i + 1, j)
            path2 = _find_paths(m, n, i, j + 1)
            return path1 + path2

        return _find_paths(m, n, 0, 0)

    # Bottom-up DP
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for _ in range(n)] for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] = grid[row - 1][col] + grid[row][col - 1]

        return grid[-1][-1]


def main():
    print(Solution().uniquePaths(3, 7))


if __name__ == '__main__':
    main()
