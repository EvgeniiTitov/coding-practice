from typing import List


"""
Tags: Backtracking, graph

Summary:
_______________________________________________________________________________

https://leetcode.com/problems/all-paths-from-source-to-target/

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit 
from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
"""


class Solution:

    # This ia actually backtracking Eugene. Slow AF. Top-down DP to fix
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def _find_all_paths(node_index: int, current_path: List[int]) -> None:
            if node_index == target_node_idx:
                paths.append(current_path)
            else:
                connections = graph_repr[node_index]
                for connection in connections:
                    path_copy = current_path.copy()
                    path_copy.append(connection)
                    _find_all_paths(connection, path_copy)

        # Strictly speaking its unnecessary, could just use indices in lists
        graph_repr = {}
        for node_index, connections in enumerate(graph):
            graph_repr[node_index] = connections

        '''
        We're looking for all paths from source to origin. So, we consider
        all paths: from source we go to all nodes, from each node we go to all
        of its nodes, etc. A tree like structure. 
        '''

        target_node_idx = len(graph) - 1
        paths = []
        _find_all_paths(0, [0])

        return paths


def main():
    print(Solution().allPathsSourceTarget(
        # graph=[[1,2],[3],[3],[]]
        graph=[[4,3,1],[3,2,4],[3],[4],[]]
    ))


if __name__ == '__main__':
    main()
