from typing import List, Set, Tuple


"""
Summary:

Instead of picking a 0 on the grid (Solution 1,2) and then trying to understand
if it borders with unflippable 0s (trying to get to an edge from this 0), you
should flip/reverse the problem - pick all zeros on edges and then propagate 
from them (DFS/BFS) into the grid changing 0s to any other letter. This allows
to avoid keeping track of visited cells by marking them in place.

_______________________________________________________________________________

https://leetcode.com/problems/surrounded-regions/

Given an m x n matrix board containing 'X' and 'O', capture all regions that 
are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]
Output: [
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","O","X","X"]
]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
"""


# Solution 1. Passes 37/58 - slightly incorrect assumption. If a coord is 0
# and is adjacent to another 0, I just keep probing this direction (vector)
# to check if it ends with 0 (4 directional), but its incorrect!
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#
#         def _determine_if_coord_needs_flipping(i: int, j: int) -> bool:
#             on_edge = _check_if_on_edge(i, j)
#             if on_edge:
#                 return False
#             must_be_flipped = True
#             for direction in directions:
#                 next_i = i + direction[0]
#                 next_j = j + direction[1]
#                 if board[next_i][next_j] == "X":
#                     continue
#                 ends_with_zero = _does_end_with_zero(next_i, next_j, direction)
#                 if ends_with_zero:
#                     must_be_flipped = False
#             return must_be_flipped
#
#         def _does_end_with_zero(
#                 i: int, j: int, direction: tuple[int, int]
#         ) -> bool:
#             # TODO: There is a mistake, no need to go till the edge, if
#             #       found X on the way, already return True
#             is_on_edge = _check_if_on_edge(i, j)
#             if is_on_edge and board[i][j] == "O":
#                 return True
#             elif is_on_edge and board[i][j] == "X":
#                 return False
#             next_i = i + direction[0]
#             next_j = j + direction[1]
#             return _does_end_with_zero(next_i, next_j, direction)
#
#         def _check_if_on_edge(i: int, j: int) -> bool:
#             if i == 0 or j == 0 or i == rows - 1 or j == columns - 1:
#                 return True
#             return False
#
#         rows = len(board)
#         columns = len(board[0])
#         if rows == 1 and columns == 1:
#             return
#
#         directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
#         for i in range(rows):
#             for j in range(columns):
#                 if board[i][j] == "X":
#                     continue
#
#                 needs_flipping = _determine_if_coord_needs_flipping(i, j)
#                 if needs_flipping:
#                     board[i][j] = "X"


# Solution 2 works, passed 57 / 58 test cases passed - Time Limit Exceeded.
# The problem with the solution below is that every iteration for a 0, you
# find those 0s that are not flippable and yet you do not remember them, so
# later you might do the same shit again rather than checking cache and
# realising we've already solved this subproblem
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def _determine_if_coord_needs_flipping(
            i: int, j: int, processed: set
        ) -> bool:
            on_edge = _check_if_on_edge(i, j)
            if on_edge:
                unflippable.add((i, j))
                return False

            processed.add((i, j))

            must_be_flipped = True
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]

                if board[next_i][next_j] == "X":
                    continue

                if (next_i, next_j) in processed:
                    continue

                needs_flipping = _determine_if_coord_needs_flipping(
                    next_i, next_j, processed
                )
                if not needs_flipping:
                    must_be_flipped = False
                    break

            return must_be_flipped

        def _does_end_with_zero(
            i: int, j: int, direction: tuple[int, int]
        ) -> bool:
            is_on_edge = _check_if_on_edge(i, j)
            if is_on_edge and board[i][j] == "O":
                return True
            elif is_on_edge and board[i][j] == "X":
                return False
            next_i = i + direction[0]
            next_j = j + direction[1]
            return _does_end_with_zero(next_i, next_j, direction)

        def _check_if_on_edge(i: int, j: int) -> bool:
            if i == 0 or j == 0 or i == rows - 1 or j == columns - 1:
                return True
            return False

        rows = len(board)
        columns = len(board[0])
        if rows == 1 and columns == 1:
            return

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        unflippable = set()
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == "X":
                    continue

                if (i, j) in unflippable:
                    continue

                needs_flipping = _determine_if_coord_needs_flipping(
                    i, j, set()
                )
                if needs_flipping:
                    board[i][j] = "X"


# Optimised solutions starting from the edges instead of checking all 0 cells
class Solution:

    # # DFS. T: O(N) - all cells are traversed. S: O(N) - border cells, recursion
    def solve(self, board: List[List[str]]) -> None:
        def _retrieve_border_cells() -> Set[Tuple[int, int]]:
            border_cells = set()
            for i in range(rows):
                border_cells.add((i, 0))
                border_cells.add((i, columns - 1))
            for j in range(columns):
                border_cells.add((0, j))
                border_cells.add((rows - 1, j))
            return border_cells

        def _check_if_out_of_bounds(i: int, j: int) -> bool:
            if i < 0 or j < 0 or i > rows - 1 or j > columns - 1:
                return True
            return False

        def _perform_dfs(i: int, j: int, char: str) -> None:
            board[i][j] = char
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                if _check_if_out_of_bounds(next_i, next_j):
                    continue
                if board[next_i][next_j] != "O":
                    continue
                _perform_dfs(next_i, next_j, char)

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        rows = len(board)
        columns = len(board[0])
        if rows == 1 and columns == 1:
            return

        border_cells = _retrieve_border_cells()

        # Propagate from each bordering 0 flipping all adjacent 0s to escape ch
        escaped_char = "E"
        for i, j in border_cells:
            if board[i][j] == "O":
                _perform_dfs(i, j, escaped_char)

        for i in range(rows):
            for j in range(columns):
                # Captured, could be flipped to X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # Return to the original value
                elif board[i][j] == escaped_char:
                    board[i][j] = "O"

    # BFS. T: O(N) - all cells are traversed. S: O(N) - border cells, recursion
    def solve(self, board: List[List[str]]) -> None:

        from queue import Queue

        def _retrieve_border_cells() -> Set[Tuple[int, int]]:
            border_cells = set()
            for i in range(rows):
                border_cells.add((i, 0))
                border_cells.add((i, columns - 1))
            for j in range(columns):
                border_cells.add((0, j))
                border_cells.add((rows - 1, j))
            return border_cells

        def _check_if_out_of_bounds(i: int, j: int) -> bool:
            if i < 0 or j < 0 or i > rows - 1 or j > columns - 1:
                return True
            return False

        def _perform_bfs(i: int, j: int, char: str) -> None:
            queue = Queue()
            queue.put((i, j))
            while queue.qsize():
                curr_i, curr_j = queue.get()

                # Weird why I need this check, hmmmmmmmmmmmmmm
                if board[curr_i][curr_j] != "O":
                    continue

                board[curr_i][curr_j] = char

                for direction in directions:
                    next_i = curr_i + direction[0]
                    next_j = curr_j + direction[1]

                    if _check_if_out_of_bounds(next_i, next_j):
                        continue
                    if board[next_i][next_j] != "O":
                        continue
                    queue.put((next_i, next_j))

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        rows = len(board)
        columns = len(board[0])
        if rows == 1 and columns == 1:
            return

        border_cells = _retrieve_border_cells()

        # Propagate from each bordering 0 flipping all adjacent 0s to escape ch
        escaped_char = "E"
        for i, j in border_cells:
            if board[i][j] == "O":
                _perform_bfs(i, j, escaped_char)

        for i in range(rows):
            for j in range(columns):
                # Captured, could be flipped to X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # Return to the original value
                elif board[i][j] == escaped_char:
                    board[i][j] = "O"


def main():
    # board = [
    #     ["X","X","X","X"],
    #     ["X","O","O","X"],
    #     ["X","X","O","X"],
    #     ["X","O","X","X"]
    # ]
    board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]

    print("BOARD BEFORE:")
    for row in board:
        print(row)

    Solution().solve(board=board)

    print("\nBOARD AFTER:")
    for row in board:
        print(row)


if __name__ == "__main__":
    main()
