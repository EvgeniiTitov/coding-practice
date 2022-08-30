from typing import List


"""
Summary:
    In the iterative BFS solution we propagate from ALL gates simultaneously
    (BFS), whereas your recursive solution is DFS, which apparently leads to 
    some errors (weird, I update only if the new value - path from the gate, is
    smaller than the current one).
    
    In the BFS approach, a cell gets updated only ONCE from the CLOSEST gate. 
    So, you DO NOT process cells that already got their values, the closest
    gate had led to them.
    How does
_______________________________________________________________________________

https://leetcode.com/problems/walls-and-gates/

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to 
represent INF as you may assume that the distance to a gate is less than 
2147483647.

Fill each empty room with the distance to its nearest gate. If it is 
impossible to reach a gate, it should be filled with INF.

Example 1:


Input: rooms = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]
]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
"""


INF = 2147483647


class Solution:

    # My recursive
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        def _find_all_gates() -> list[tuple[int, int]]:
            gates = []
            for row in range(rows):
                for col in range(cols):
                  if rooms[row][col] == 0:
                      gates.append((row, col))
            return gates

        def _is_out_of_bounds(i: int, j: int) -> bool:
            if i < 0 or i >= rows:
                return True
            if j < 0 or j >= cols:
                return True
            return False

        def _calculate_dist_from_gate(
            curr_coord: tuple[int, int],
            curr_steps: int,
            visited_coords: set[tuple[int, int]]
        ) -> None:
            """
            From a gate calculate distances to all reachable rooms. If a new
            distance is shorter, update it.
            """
            curr_i, curr_j = curr_coord
            visited_coords.add((curr_i, curr_j))

            # TODO: Might not be treating the initial gate value correctly
            curr_cell_value = rooms[curr_i][curr_j]
            if  curr_cell_value == INF:
                rooms[curr_i][curr_j] = curr_steps
            elif curr_cell_value != INF and curr_steps < curr_cell_value:
                rooms[curr_i][curr_j] = curr_steps

            for next_move in next_moves:
                next_i = curr_i + next_move[0]
                next_j = curr_j + next_move[1]

                if _is_out_of_bounds(next_i, next_j):
                    continue

                # Can't go into a gate or a wall
                if rooms[next_i][next_j] == -1 or rooms[next_i][next_j] == 0:
                    continue

                if (next_i, next_j) in visited_coords:
                    continue

                _calculate_dist_from_gate(
                    (next_i, next_j), curr_steps + 1, visited_coords
                )
            return

        rows = len(rooms)
        cols = len(rooms[0])

        if not rows:
            return

        next_moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        gate_coords = _find_all_gates()
        for gate_coord in gate_coords:
            _calculate_dist_from_gate(gate_coord, 0, set())

        return

    # My iterative BFS
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        from queue import Queue

        def _is_out_of_bounds(i: int, j: int) -> bool:
            if i < 0 or i >= rows:
                return True
            if j < 0 or j >= cols:
                return True
            return False

        rows = len(rooms)
        cols = len(rooms[0])
        if not rows:
            return

        next_moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        # Find all gates
        queue = Queue()
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue.put((i, j))

        # Perform BFS from each gate
        while queue.qsize():
            curr_i, curr_j = queue.get()
            for next_move in next_moves:
                next_i = curr_i + next_move[0]
                next_j = curr_j + next_move[1]

                if _is_out_of_bounds(next_i, next_j):
                    continue
                if rooms[next_i][next_j] != INF:
                    continue

                rooms[next_i][next_j] = rooms[curr_i][curr_j] + 1
                queue.put((next_i, next_j))
        return


def main():
    rooms = [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
    ]
    Solution().wallsAndGates(rooms=rooms)
    print(rooms)


if __name__ == '__main__':
    main()
