from typing import List, Iterable


"""
Summary:
    Brute force: A bit of fuckery with loops. Iterate over quadrants/squares,
    for each validate its content and the rows/cols that it includes. Caching
    could be added to avoid revalidating the same rows/cols for adjacent 
    squares
_______________________________________________________________________________

https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the ! filled cells need to be 
validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 
   without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 
Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""


class Solution:

    # Passes all tests, rather slow though
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def _get_sub_box() -> Iterable:
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    box_coord = []
                    unique_xs = set()
                    unique_ys = set()
                    for i_i in range(i, i + 3):
                        unique_xs.add(i_i)
                        for j_j in range(j, j + 3):
                            box_coord.append((i_i, j_j))
                            unique_ys.add(j_j)
                    yield box_coord, unique_xs, unique_ys

        def _validate_box(coords: List[tuple[int, int]]) -> bool:
            seen_numbers = set()
            for x, y in coords:
                value = board[x][y]
                if value == ".":
                    continue
                if value in seen_numbers:
                    return False
                seen_numbers.add(value)
            return True

        def _validate_row(x: int) -> bool:
            row_values = board[x][:]
            seen_numbers = set()
            for row_value in row_values:
                if row_value == ".":
                    continue
                if row_value in seen_numbers:
                    return False
                seen_numbers.add(row_value)
            return True

        def _validate_col(y: int) -> bool:
            col_values = [row[y] for row in board]
            seen_numbers = set()
            for col_value in col_values:
                if col_value == ".":
                    continue
                if col_value in seen_numbers:
                    return False
                seen_numbers.add(col_value)
            return True

        # TODO: Could add a bit of caching to avoid revalidating the same rows/
        #       cols for the adjacent squares

        # validated_xs = {}
        # validated_ys = {}
        for i, box_data in enumerate(_get_sub_box()):
            box_coords, unique_xs, unique_ys = box_data
            print(f"{i}. Coords: {box_coords}")

            if not _validate_box(box_coords):
                return False

            for unique_x in unique_xs:
                is_valid = _validate_row(unique_x)
                if not is_valid:
                    return False

            for unique_y in unique_ys:
                is_valid = _validate_col(unique_y)
                if not is_valid:
                    return False

        return True


def main():
    print(Solution().isValidSudoku(
        board=[
            [".",".","4",".",".",".","6","3","."],
            [".",".",".",".",".",".",".",".","."],
            ["5",".",".",".",".",".",".","9","."],
            [".",".",".","5","6",".",".",".","."],
            ["4",".","3",".",".",".",".",".","1"],
            [".",".",".","7",".",".",".",".","."],
            [".",".",".","5",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."]
        ]
    ))


if __name__ == '__main__':
    main()
