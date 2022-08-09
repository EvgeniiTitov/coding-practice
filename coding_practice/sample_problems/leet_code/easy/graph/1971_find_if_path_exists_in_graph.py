from typing import List


"""
Summary: BFS is fine
_______________________________________________________________________________

https://leetcode.com/problems/find-if-path-exists-in-graph/

There is a bi-directional graph with n vertices, where each vertex is labeled 
from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D 
integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional 
edge between vertex ui and vertex vi. Every vertex pair is connected by at 
most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex 
source to vertex destination.

Given edges and the integers n, source, and destination, return true if there 
is a valid path from source to destination, or false otherwise.
"""


class Solution:

    # My BFS solution
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:

        from collections import defaultdict
        from queue import Queue

        graph = defaultdict(list)
        for vertex1, vertex2 in edges:
            graph[vertex1].append(vertex2)
            graph[vertex2].append(vertex1)

        queue = Queue()
        queue.put([source])
        visited_vertices = {source}
        while queue.qsize():
            path = queue.get()
            last_vertex = path[-1]

            if last_vertex == destination:
                return True

            for adjacent_node in graph[last_vertex]:
                if adjacent_node in visited_vertices:
                    continue
                new_path = path[:]
                new_path.append(adjacent_node)
                queue.put(new_path)
                visited_vertices.add(adjacent_node)

        return False


def main():
    print(
        Solution().validPath(
            n=5,
            edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]],
            source=0,
            destination=5,
        )
    )


if __name__ == "__main__":
    main()
