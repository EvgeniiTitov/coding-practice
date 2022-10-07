from typing import List


"""
Summary:
    Backtracking: typical grid search, just make sure you don't go out of bounds,
    keep track of visited coords, prune those branches that result in invalid
    solutions!
_______________________________________________________________________________

https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word 
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where 
adjacent cells are horizontally or vertically neighboring. The same letter cell 
may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
word = "ABCB"
Output: false
"""


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        def _find_starting_coords(
            char: str, board: List[List[str]]
        ) -> tuple[List[tuple[int, int]], set]:
            coords = []
            unique_chars = set()
            for i in range(rows):
                for j in range(cols):
                    unique_chars.add(board[i][j])
                    if board[i][j] == char:
                        coords.append((i, j))
            return coords, unique_chars

        def _search_word(i: int, j: int, word: str) -> bool:
            if not len(word):
                return True

            # Out of bounds
            if i < 0 or i == rows or j < 0 or j == cols:
                return False

            # Prune subtrees that won't lead to a valid solution
            if board[i][j] != word[0]:
                return False

            found = False
            board[i][j] = "#"  # ! To keep track of visited coords
            for next_coord in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                found = _search_word(
                    i + next_coord[0], j + next_coord[1], word[1:]
                )
                if found:
                    break

            board[i][j] = word[0]  # ! revert the change from char to #
            return found

        rows = len(board)
        cols = len(board[0])

        starting_coords, board_chars = _find_starting_coords(word[0], board)
        word_chars = set(word)
        if len(word_chars.intersection(board_chars)) != len(word_chars):
            return False

        for i, j in starting_coords:
            if _search_word(i, j, word):
                return True

        return False


    # Passes but its dump - we build the whole solution tree without pruning
    # those branches that result in incorrect solutions (intermediate chars
    # do not match).
    def exist(self, board: List[List[str]], word: str) -> bool:

        def _find_starting_coords(
            char: str, board: List[List[str]]
        ) -> tuple[List[tuple[int, int]], set]:
            coords = []
            unique_chars = set()
            for i in range(rows):
                for j in range(cols):
                    unique_chars.add(board[i][j])
                    if board[i][j] == char:
                        coords.append((i, j))
            return coords, unique_chars

        def _is_out_of_bounds(i: int, j: int) -> bool:
            if i < 0 or i >= rows:
                return True
            if j < 0 or j >= cols:
                return True
            return False

        def _search_word(
            curr_coord: tuple[int, int],
            visited_coords: set,
            curr_word: List[str]
        ) -> bool:
            # Base case
            if len(curr_word) == word_length:
                return True if "".join(curr_word) == word else False

            for next_move in next_moves:
                next_i = curr_coord[0] + next_move[0]
                next_j = curr_coord[1] + next_move[1]

                # Do not visit the coords we've already visited
                if (next_i, next_j) in visited_coords:
                    continue

                # Do not go out of bounds
                if _is_out_of_bounds(next_i, next_j):
                    continue

                # TODO: Check if the next char is what we expect, else don't go

                # ! Backtrack cache as well, since this path didn't result in
                # a solution, we could potentially go there from another branch
                curr_word.append(board[next_i][next_j])
                visited_coords.add((curr_coord))

                found = _search_word(
                    (next_i, next_j), visited_coords, curr_word
                )
                if found:
                    return True

                curr_word.pop()
                visited_coords.remove(curr_coord)

            # Not found the word
            return False

        next_moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

        word_length = len(word)
        if word_length == 0:
            return True

        rows = len(board)
        cols = len(board[0])
        starting_coords, board_chars = _find_starting_coords(word[0], board)
        word_chars = set(word)
        if len(word_chars.intersection(board_chars)) != len(word_chars):
            return False

        for i, j in starting_coords:
            if _search_word((i, j), set(), [board[i][j]]):
                return True

        return False


def main():
    print(Solution().exist(
        board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
        word="ABCCED"
    ))


if __name__ == '__main__':
    main()
