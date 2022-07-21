from typing import List


"""
Summary: Much easier to start from the ocean (edges). Use queues for BFSs. 
For each ocean you get a set of coords that could be reached. Then just take
intersection
_______________________________________________________________________________

https://leetcode.com/problems/pacific-atlantic-water-flow/

There is an m x n rectangular island that borders both the Pacific Ocean and 
Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and 
the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n 
integer matrix heights where heights[r][c] represents the height above sea 
level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring 
cells directly north, south, east, and west if the neighboring cell's height 
is less than or equal to the current cell's height. Water can flow from any 
cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes 
that rain water can flow from cell (ri, ci) to both the Pacific and 
Atlantic oceans.
"""


class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from queue import Queue

        def _check_if_out_of_bounds(i: int, j: int) -> bool:
            if i < 0 or j < 0:
                return True
            if i > rows - 1 or j > columns - 1:
                return True
            return False

        def _perform_dfs(queue: Queue) -> set:
            reachable = set()
            while queue.qsize():
                coord = queue.get()
                curr_i, curr_j = coord[0], coord[1]
                if coord in reachable:
                    continue

                reachable.add(coord)
                for possible_move in possible_moves:
                    next_i = curr_i + possible_move[0]
                    next_j = curr_j + possible_move[1]
                    if _check_if_out_of_bounds(next_i, next_j):
                        continue

                    current_height = heights[curr_i][curr_j]
                    if (
                        (next_i, next_j) not in reachable
                        and current_height <= heights[next_i][next_j]
                    ):
                        queue.put((next_i, next_j))
            return reachable

        rows = len(heights)
        columns = len(heights[0])
        possible_moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        pacific_queue = Queue()
        atlantic_queue = Queue()

        # Collect edges of each ocean
        for i in range(rows):
            pacific_queue.put((i, 0))
            atlantic_queue.put((i, columns - 1))
        for j in range(columns):
            pacific_queue.put((0, j))
            atlantic_queue.put((rows - 1, j))

        reachable_from_pacific = _perform_dfs(pacific_queue)
        reachable_from_atlantic = _perform_dfs(atlantic_queue)
        return list(
            reachable_from_atlantic.intersection(reachable_from_pacific)
        )

    # My attempt - better start from the ocean
    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #
    #     Pacific = "P"
    #     Atlantic = "A"
    #
    #     def _check_if_in_ocean(row: int, column: int) -> tuple:
    #         if row > rows - 1:
    #             return True, Atlantic
    #         elif row < 0:
    #             return True, Pacific
    #
    #         if column > columns - 1:
    #             return True, Atlantic
    #         elif column < 0:
    #             return True, Pacific
    #
    #         return False, ""
    #
    #     def _find_ocean(row: int, column: int) -> None:
    #         current_height = heights[row][column]
    #         for next_move in possible_moves:
    #             next_row, next_column = row + next_move[0], column + next_move[1]
    #
    #             if (next_row, next_column) in processed_coordcinates:
    #                 continue
    #
    #             # If out of bounds - check what ocean we ended up in, update data
    #             in_ocean, ocean_type = _check_if_in_ocean(next_row, next_column)
    #             if in_ocean:
    #                 water_flow_data[(i, j)].add(ocean_type)
    #                 continue
    #
    #             processed_coordcinates.add((i, j))
    #             if heights[next_row][next_column] <= current_height:
    #                 _find_ocean(next_row, next_column)
    #
    #     rows = len(heights)
    #     columns = len(heights[0])
    #     water_flow_data = {}
    #     processed_coordcinates = set()
    #     possible_moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    #     for i in range(rows):
    #         for j in range(columns):
    #             water_flow_data[(i, j)] = set()
    #             _find_ocean(i, j)
    #
    #     out = []
    #     for coord, oceans_flown_into in water_flow_data.items():
    #         if len(oceans_flown_into) == 2:
    #             out.append(list(coord))
    #     return out


def main():
    print(Solution().pacificAtlantic(
        heights=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    ))


if __name__ == '__main__':
    main()
