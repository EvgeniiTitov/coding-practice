from typing import List


"""
Summary: TICKs separate cycles (within one cycle adjacent oranges get infected)
of the BFS.
Every iter/cycle we infect new oranges (1 to 2), at the end of check if all 
oranges have been infected or not. <- instead of 
using visited set to keep track of coordinates visited (linear space), we 
modify the grid in place.
_______________________________________________________________________________

https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of three values:

- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten 
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a 
fresh orange. If this is impossible, return -1.
"""


class Solution:
    # In this approach we keep track of processed oranges by changing them from
    # 1 to 2 (rotten)
    # T: O(N), where N is size of the grid
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from queue import Queue

        fresh_oranges = 0
        queue = Queue()
        rows, columns = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    queue.put((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        TICK = "tick"
        queue.put(TICK)

        minutes_elapsed = -1  # ! Why -1?
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while queue.qsize():
            item = queue.get()
            if item == TICK:
                minutes_elapsed += 1
                if queue.qsize():
                    queue.put(TICK)
            else:
                i, j = item
                for direction in directions:
                    next_i = i + direction[0]
                    next_j = j + direction[1]
                    if 0 <= next_i <= rows - 1 and 0 <= next_j <= columns - 1:
                        if grid[next_i][next_j] == 1:
                            grid[next_i][next_j] = 2
                            fresh_oranges -= 1
                            queue.put((next_i, next_j))

        return minutes_elapsed if fresh_oranges == 0 else -1

# ----- My solution (close but bugged somewhere dealing with edge cases) ------

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         import heapq
#
#         graph, rotten_coord = self._build_undirected_graph_from_grid(grid)
#
#         if not rotten_coord:
#             return 0
#
#         distances = {vertex: float("inf") for vertex in graph}
#         distances[rotten_coord] = 0
#         visited_vertices = set()
#         heap = [(0, rotten_coord)]
#         while len(heap):
#             curr_dst_from_src, curr_vertex = heapq.heappop(heap)
#
#             visited_vertices.add(curr_vertex)
#
#             for neighbour, curr_to_neighbour_dist in graph[curr_vertex]:
#                 new_dist_neighbour = curr_dst_from_src + curr_to_neighbour_dist
#                 if new_dist_neighbour < distances[neighbour]:
#                     distances[neighbour] = new_dist_neighbour
#                     if neighbour not in visited_vertices:
#                         heapq.heappush(
#                             heap, (new_dist_neighbour, neighbour)
#                         )
#
#         min_time = max(distances.values())
#         return min_time if min_time != float("inf") else -1
#
#     def _build_undirected_graph_from_grid(self, grid: List[List[int]]) -> tuple:
#         next_moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
#         rows = len(grid)
#         columns = len(grid[0])
#         graph = {}
#         rotten_coord = None
#         for i in range(rows):
#             for j in range(columns):
#                 if grid[i][j] == 0:
#                     continue
#
#                 if grid[i][j] == 2:
#                     rotten_coord = (i, j)
#
#                 graph[(i, j)] = []
#                 for next_move in next_moves:
#                     next_i = i + next_move[0]
#                     next_j = j + next_move[1]
#                     if self._check_if_out_of_bounds(
#                         next_i, next_j, rows, columns
#                     ):
#                         continue
#                     if grid[next_i][next_j] != 1:
#                         continue
#
#                     graph[(i, j)].append(((next_i, next_j), 1))
#
#         return graph, rotten_coord
#
#     def _check_if_out_of_bounds(
#         self, i: int, j: int, rows: int, columns: int
#     ) -> bool:
#         if i < 0 or j < 0 or i > rows - 1 or j > columns - 1:
#             return True
#         return False


def main():
    print(Solution().orangesRotting(
        grid=[[2,1,1],[1,1,0],[0,1,1]]
        # grid=[[2,1,1],[0,1,1],[1,0,1]]
        # grid=[[0,2]]
        # grid=[[0]]
        # grid=[[0,1]]
    ))


if __name__ == '__main__':
    main()
