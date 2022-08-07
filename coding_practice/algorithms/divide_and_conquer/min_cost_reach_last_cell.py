import typing as t


"""
Min cost to reach the last cell 2D

2D matrix given
Each cell has a cost associated with it for accessing
Starting at 0,0 reach (n-1, m-1)
Could only move right or down from the current cell
"""


Matrix = t.List[t.List[int]]


# The problem is solved in reverse (from dest to source)
# Out of bounds is checked after the call
def find_min_cost_path_reverse(
    matrix: Matrix, i: int, j: int
) -> t.Union[float, int]:
    if i < 0 or j < 0:
        return float("inf")
    if i == 0 and j == 0:
        return matrix[i][j]

    path1 = find_min_cost_path_reverse(matrix, i - 1, j)
    path2 = find_min_cost_path_reverse(matrix, i, j - 1)

    return matrix[i][j] + min(path1, path2)


# Source - dest; Out of bounds if checked after the call
def find_min_cost_path(matrix: Matrix, i: int, j: int) -> t.Union[int, float]:
    rows = len(matrix)
    cols = len(matrix[0])

    if i >= rows or j >= cols:
        return float("inf")
    if i == rows - 1 and j == cols - 1:
        return matrix[i][j]

    path1 = find_min_cost_path(matrix, i + 1, j)
    path2 = find_min_cost_path(matrix, i, j + 1)

    return matrix[i][j] + min(path1, path2)


def main():
    grid = [
        [4, 7, 8, 6, 4],
        [6, 7, 3, 9, 2],
        [3, 8, 1, 2, 4],
        [7, 1, 7, 3, 7],
        [2, 9, 8, 9, 3]
    ]
    rows = len(grid)
    cols = len(grid[0])
    print("Reverse:", find_min_cost_path_reverse(grid, rows - 1, cols - 1))
    print("Direct:", find_min_cost_path(grid, 0, 0))


if __name__ == '__main__':
    main()
