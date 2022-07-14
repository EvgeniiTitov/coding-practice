from typing import List


"""
Summary:
    My head on: You start looking for an island from every possible point (i,j)
    Use a set of track what coordinates have been visited, i.e. island already
    found
    From each point I start, check if its already been counted or if its the sea,
    i.e grid[i][j] = "0"
    If not, add the coordinate to visited, and then from this coordinate try
    recursively visit all adjacent land marking it as visited.
    That way, even if I start on the same island, I can see its coordinates have
    already been visited, i.e the island counted
    Whenever I find a new island, all its land gets added to visited as I 
    recursively call the function for all possible directions at every point on
    the island
    
_______________________________________________________________________________

https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's 
(water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. You may assume all four edges of the grid are 
all surrounded by water. 

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""


class Solution:
    # My head of brute force: Recursion
    def numIslands(self, grid: List[List[str]]) -> int:

        def _search_islands(i: int, j: int) -> bool:
            if grid[i][j] == "0" or (i, j) in visited_coordinates:
                return False

            visited_coordinates.add((i, j))
            possible_directions = []
            if i > 0:
                possible_directions.append([i - 1, j])
            if j > 0:
                possible_directions.append([i, j - 1])
            if i < rows - 1:
                possible_directions.append([i + 1, j])
            if j < columns - 1:
                possible_directions.append([i, j + 1])

            for next_move in possible_directions:
                # If next move is the sea or was already visited (attempt to go
                # back from where we just came), skip
                if (
                        grid[next_move[0]][next_move[1]] == "0"
                        or tuple(next_move) in visited_coordinates
                ):
                    continue
                _search_islands(*next_move)

            return True

        total_islands = 0
        visited_coordinates = set()
        rows = len(grid)
        columns = len(grid[0])
        for i in range(rows):
            for j in range(columns):
                found  = _search_islands(i, j)
                if found:
                    total_islands += 1

        return total_islands

    # DFS
    def numIslands(self, grid: List[List[str]]) -> int:

        # Here we call first, then check if we're out of bounds. ^ you check
        # first
        def _perform_dfs(i: int, j: int):
            """
            Sets all visited island points from 1 to 0
            """
            # Check for out of bounds
            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] == "0":
                return

            grid[i][j] = "0"
            _perform_dfs(i - 1, j)
            _perform_dfs(i + 1, j)
            _perform_dfs(i, j - 1)
            _perform_dfs(i, j + 1)

        total_islands = 0
        rows = len(grid)
        columns = len(grid[0])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "0":
                    continue
                _perform_dfs(i, j)
                total_islands += 1
        return total_islands

    # # TODO: Complete me BFS
    def numIslands(self, grid: List[List[str]]) -> int:
        from queue import Queue

        total_islands = 0
        rows = len(grid)
        columns = len(grid[0])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "0":
                    continue

                # Mark as visited and process all adjacent land
                total_islands += 1
                queue = Queue()
                queue.put((i, j))
                while queue.qsize():
                    i, j = queue.get()
                    grid[i][j] = "0"

                    if i > 0 and grid[i - 1][j] != "0":
                        queue.put((i - 1, j))
                    if j > 0 and grid[i][j - 1] != "0":
                        queue.put((i, j - 1))
                    if i < rows - 1 and grid[i + 1][j] != "0":
                        queue.put((i + 1, j))
                    if j < columns - 1 and grid[i][j + 1] != "0":
                        queue.put((i, j + 1))



def main():
    print(Solution().numIslands(
        grid=[
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
    ))


if __name__ == '__main__':
    main()
