from typing import List


"""
Summary: BFS / recursive
    
    NOTE:
    2 ways to keep track of visited coords (change from 1 to 0, or a set)
    
    2 ways to avoid going out of bounds:
        - before the recursive call (_get_next_moves())
        - after, in the new call (if we're out of bounds check, return)
        
    In both solutions I DO NOT check if the next coord is 1 or 0, i just go
    there and if its 0 I return straight away. Could check that as well
_______________________________________________________________________________

https://leetcode.com/problems/max-area-of-island/

You are given an m x n binary matrix grid. An island is a group of 1's 
(representing land) connected 4-directionally (horizontal or vertical.) You 
may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""


class Solution:

    # My recursive. Checking out of bounds in advance. 1 to 0 to track visited
    # ~ 150ms
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # Check next possible move in advance
        def _get_next_moves(i: int, j: int) -> List[List[int]]:
            moves = []
            if i > 0:
                moves.append([i - 1, j])
            if j > 0:
                moves.append([i, j - 1])
            if i < rows - 1:
                moves.append([i + 1, j])
            if j < columns - 1:
                moves.append([i, j + 1])
            return moves

        def _find_island(i: int, j: int, area: int = 0) -> int:
            if grid[i][j] == 0:
                return 0

            area += 1
            grid[i][j] = 0
            for move in _get_next_moves(i, j):
                area += _find_island(*move)
            return area

        rows = len(grid)
        columns = len(grid[0])
        largest_island = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    continue

                # grid[i][j] = 0
                island_size = _find_island(i, j)
                largest_island = max(largest_island, island_size)

        return largest_island

    # My iterative BFS - much slower then ^ (approx 900ms)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from queue import Queue

        # Check next possible move in advance
        def _get_next_moves(i: int, j: int) -> List[List[int]]:
            moves = []
            if i > 0:
                moves.append([i - 1, j])
            if j > 0:
                moves.append([i, j - 1])
            if i < rows - 1:
                moves.append([i + 1, j])
            if j < columns - 1:
                moves.append([i, j + 1])
            return moves

        rows = len(grid)
        columns = len(grid[0])
        largest_island = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    continue

                queue = Queue()
                queue.put((i, j))
                current_island_size = 0
                while queue.qsize():
                    curr_i, curr_j = queue.get()

                    if grid[curr_i][curr_j] == 0:
                        continue

                    grid[curr_i][curr_j] = 0
                    current_island_size += 1
                    for next_i, next_j in _get_next_moves(curr_i, curr_j):
                        queue.put((next_i, next_j))

                largest_island = max(largest_island, current_island_size)

        return largest_island

    # My iterative DFS - faster than BFS (200 ms)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # Check next possible move in advance
        def _get_next_moves(i: int, j: int) -> List[List[int]]:
            moves = []
            if i > 0:
                moves.append([i - 1, j])
            if j > 0:
                moves.append([i, j - 1])
            if i < rows - 1:
                moves.append([i + 1, j])
            if j < columns - 1:
                moves.append([i, j + 1])
            return moves

        rows = len(grid)
        columns = len(grid[0])
        largest_island = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    continue

                stack = []
                stack.append((i, j))
                current_island_size = 0
                while len(stack):
                    curr_i, curr_j = stack.pop()

                    if grid[curr_i][curr_j] == 0:
                        continue

                    grid[curr_i][curr_j] = 0
                    current_island_size += 1
                    for next_i, next_j in _get_next_moves(curr_i, curr_j):
                        stack.append((next_i, next_j))

                largest_island = max(largest_island, current_island_size)

        return largest_island

    # DFS as ^ but using set of track processed coords - no modifying 1s to 0s
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # Check next possible move in advance
        def _get_next_moves(i: int, j: int) -> List[List[int]]:
            moves = []
            if i > 0:
                moves.append([i - 1, j])
            if j > 0:
                moves.append([i, j - 1])
            if i < rows - 1:
                moves.append([i + 1, j])
            if j < columns - 1:
                moves.append([i, j + 1])
            return moves

        rows = len(grid)
        columns = len(grid[0])
        largest_island = 0
        visited_coords = set()
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0 or (i, j) in visited_coords:
                    continue

                stack = []
                current_island_size = 0
                stack.append((i, j))
                visited_coords.add((i, j))
                while len(stack):
                    curr_i, curr_j = stack.pop()

                    if grid[curr_i][curr_j] == 0:
                        continue

                    current_island_size += 1
                    for next_i, next_j in _get_next_moves(curr_i, curr_j):
                        if (next_i, next_j) not in visited_coords:
                            stack.append((next_i, next_j))
                            visited_coords.add((next_i, next_j))

                largest_island = max(largest_island, current_island_size)

        return largest_island


def main():
    print(Solution().maxAreaOfIsland(
        grid=[
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1],
        ]
    ))


if __name__ == '__main__':
    main()
