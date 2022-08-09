import typing as t


"""
Number of paths to reach the last cell with given cost

Given 2D matrix
Each cell has a cost associated with it for accessing
Starting from 0,0 need to reach n-1,m-1
We can only go down and right
We're given the total cost to reach the last cell
Find the total N of paths to reach the end with the given total cost (=)

Base cases:
    - Out of bounds - Could be check before the call or after
    - Ran out of cost
"""


Matrix = t.List[t.List[int]]


def find_paths(
    matrix: Matrix, cost: int, i: int = 0, j: int = 0
) -> t.Union[int, float]:
    # Base cases
    rows = len(matrix)
    cols = len(matrix[0])
    if i >= rows or j >= cols:
        return 0

    remaining_cost = cost - matrix[i][j]
    if remaining_cost < 0:
        return 0

    if i == rows - 1 and j == cols - 1:
        return 1 if remaining_cost == 0 else 0

    path1 = find_paths(matrix, remaining_cost, i + 1, j)
    path2 = find_paths(matrix, remaining_cost, i, j + 1)

    return path1 + path2


def main():
    grid = [[4, 7, 1, 6], [5, 7, 3, 9], [3, 2, 1, 2], [7, 1, 6, 3]]
    cost = 25
    print(find_paths(grid, cost))


if __name__ == "__main__":
    main()
