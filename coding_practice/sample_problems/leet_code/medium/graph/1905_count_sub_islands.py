from typing import List


"""
Summary:
    The simple logic is: 
        First - remove all non subislands (1 in grid2 but 0 in grid1), get rid
        of the whole thing from grid 2
        Then, iterate over remaining 1s in grid2 counting the number of left
        islands
_______________________________________________________________________________

https://leetcode.com/problems/count-sub-islands/description/

You are given two m x n binary matrices grid1 and grid2 containing only 0's 
(representing water) and 1's (representing land). An island is a group of 1's 
connected 4-directionally (horizontal or vertical). Any cells outside of the 
grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 
that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

Example 1:
Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], 
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid 
on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. 
There are three sub-islands.

Example 2:
Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], 
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid 
on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. 
There are two sub-islands.
"""


class Solution:

    def countSubIslands(
        self,
        grid1: List[List[int]],
        grid2: List[List[int]]
    ) -> int:

        def dfs(x: int, y: int) -> None:
            # Handle out of bounds
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return
            # Handle 0s
            if grid2[x][y] == 0:
                return

            grid2[x][y] = 0
            for x_delta, y_delta in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                dfs(x + x_delta, y + y_delta)

        rows = len(grid2)
        cols = len(grid2[0])

        # Remove all non-common sub islands (grid2 is 1 but grid1 is 0, so this
        # is not a valid subisland as grid1 needs to contain ALL 1s from grid2)
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)

        # Iterate again over the grid, pick remaining islands (valid subislands)
        # when processing one turn all its values to 0 and increment the count
        # by 1
        sub_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    dfs(i, j)
                    sub_islands += 1

        return sub_islands

    # Mine attempt - close but not quite
    # TODO: Instead of keeping track of visited, just change 1s to 0s ...
    def countSubIslands(
        self,
        grid1: List[List[int]],
        grid2: List[List[int]]
    ) -> int:

        def _check_if_sub_island(
            curr_x: int, curr_y: int, visited_coords: set[tuple[int, int]]
        ) -> bool:
            visited_coords.add((curr_x, curr_y))

            # If corresponding coordinate in grid1 is not 1 -> not subisland
            if grid1[curr_x][curr_y] != 1:
                return False

            for x_delta, y_delta in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                new_x = curr_x + x_delta
                new_y = curr_y + y_delta

                # Avoid going out of bounds
                if _check_if_out_of_bounds(new_x, new_y):
                    continue

                # Ignore water, we're looking for an island
                if grid2[new_x][new_y] == 0:
                    continue

                # Do not go back from where you came!
                if (new_x, new_y) in visited_coords:
                    continue

                is_subisland = _check_if_sub_island(
                    new_x, new_y, visited_coords
                )
                if not is_subisland:
                    return False

            return True

        def _check_if_out_of_bounds(x: int, y: int) -> bool:
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return True
            return False


        rows = len(grid2)
        cols = len(grid2[0])
        nb_of_subislands = 0
        processed_coords = set()
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 0:
                    continue

                if (i, j) in processed_coords:
                    continue

                # Process an island
                if _check_if_sub_island(i, j, processed_coords):
                    nb_of_subislands += 1

        return nb_of_subislands


def main():
    print(Solution().countSubIslands(
        # grid1=[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
        # grid2=[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
        grid1=[[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
        grid2=[[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    ))


if __name__ == '__main__':
    main()
