from typing import List, Any, MutableMapping


"""
Summary:
    Kruskals + DisJoint set. Generate edges between the points, sort them,
    then create a disjoint set with vertices = points. Implement the Kruskal's 
    algorithm - pick an edge, get its parents from the disjoint set, if they
    are not the same (no cycle), edge the edge to the solution, merge the sets,
    else, skil the edge.

    When generating edges you did it:
        edges = []
        for i in range(number_points):
            for j in range(number_points):
                if i == j:
                    continue
                point_1 = points[i]
                point_2 = points[j]
                distance = _calculate_distance(point_1, point_2)
                edges.append([point_1, point_2, distance])
    
    That generates edges both directions, i.e. A to B and B to A. This is not
    necessary since the graph is indireted, one is enough! So:
        edges = []
        for i in range(number_points):
            for j in range(i + 1, number_points):
                point_1 = points[i]
                point_2 = points[j]
                distance = _calculate_distance(point_1, point_2)
                edges.append([point_1, point_2, distance])
    
_______________________________________________________________________________

https://leetcode.com/problems/min-cost-to-connect-all-points/

You are given an array points representing integer coordinates of some points 
on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan 
distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected 
if there is exactly one simple path between any two points.

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
"""


# MY KRUSKALS SOLUTION
# THIS SOLUTION BELOW IS CRAZY YET CORRECT! GOOD REFERENCE EUGENE FOR INDEPTH

Vertex = Any
Child = Vertex
Parent = Vertex


class DisjointSet:
    def __init__(self, vertices: list[Vertex]) -> None:
        self.vertices = vertices

        # Initially nodes have themselves as parents(not part of any other set)
        self.parent: MutableMapping[Child, Parent] = {}
        for vertex in vertices:
            self.parent[vertex] = vertex

        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item: Vertex) -> Vertex:
        """
        Returns the root element it reaches (the set root the node item belongs
        to)
        """
        if self.parent[item] == item:
           return item
        else:
            return self.find(self.parent[item])

    def union(self, x: Vertex, y: Vertex):
        x_root = self.find(x)
        y_root = self.find(y)
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            # Y's parent is X now, so X's rank increases
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def _calculate_distance(point_1: list[int], point_2: list[int]) -> int:
            x1, y1 = point_1
            x2, y2 = point_2
            return abs((x1 - x2)) + abs((y1 - y2))

        def _generate_edges() -> list[list[int]]:
            edges = []
            for i in range(number_points):
                for j in range(i + 1, number_points):
                    point_1 = points[i]
                    point_2 = points[j]
                    distance = _calculate_distance(point_1, point_2)
                    edges.append([point_1, point_2, distance])
            return edges

        number_points = len(points)
        if number_points == 2:
            return _calculate_distance(*points)

        edges = _generate_edges()
        edges.sort(key=lambda item: item[-1])

        points = [tuple(point) for point in points]

        disjoint_set = DisjointSet(points)
        min_spanning_tree = []

        curr_edge_index = 0
        edges_in_mst = 0
        while edges_in_mst < number_points - 1:
            source, dest, weight = edges[curr_edge_index]
            curr_edge_index += 1

            source = tuple(source)
            dest = tuple(dest)

            ds_source_root = disjoint_set.find(source)
            ds_dest_root = disjoint_set.find(dest)

            if ds_source_root != ds_dest_root:  # Introducing this edge leads to no cycle
                edges_in_mst += 1
                min_spanning_tree.append(weight)
                disjoint_set.union(ds_source_root, ds_dest_root)

        return sum(min_spanning_tree)


# MY PRIMS SOLUTION
# TIME LIMIT EXCEEDED 71 / 72 test cases passed.
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        from collections import defaultdict
        import heapq

        def _calculate_distance(point_1: list[int], point_2: list[int]) -> int:
            x1, y1 = point_1
            x2, y2 = point_2
            return abs((x1 - x2)) + abs((y1 - y2))

        def _build_graph_repr() -> dict:
            graph = defaultdict(dict)
            for i in range(number_of_points):
                for j in range(number_of_points):
                    if i == j:
                        continue
                    source = points[i]
                    dest = points[j]
                    distance = _calculate_distance(source, dest)
                    graph[tuple(source)][tuple(dest)] = distance
            return graph

        number_of_points = len(points)
        if number_of_points == 2:
            return _calculate_distance(*points)
        elif number_of_points == 1:
            return 0

        graph = _build_graph_repr()
        """
        Vertex: (0, 0). Neighbours: {(2, 2): 4, (3, 10): 13, (5, 2): 7, (7, 0): 7}
        Vertex: (2, 2). Neighbours: {(0, 0): 4, (3, 10): 9, (5, 2): 3, (7, 0): 7}
        Vertex: (3, 10). Neighbours: {(0, 0): 13, (2, 2): 9, (5, 2): 10, (7, 0): 14}
        Vertex: (5, 2). Neighbours: {(0, 0): 7, (2, 2): 3, (3, 10): 10, (7, 0): 4}
        Vertex: (7, 0). Neighbours: {(0, 0): 7, (2, 2): 7, (3, 10): 14, (5, 2): 4}
        """

        source = list(graph.keys())[0]
        visited = {source}
        edges = [
            (weight, source, to)
            for to, weight in graph[source].items()
        ]
        heapq.heapify(edges)

        total_weight = 0
        while len(edges):
            weight, from_vertex, to_vertex = heapq.heappop(edges)
            if to_vertex not in visited:
                visited.add(to_vertex)
                total_weight += weight

                for vertex_next, weight in graph[to_vertex].items():
                    if vertex_next not in visited:
                        heapq.heappush(edges, (weight, to_vertex, vertex_next))

        return total_weight


# PRIMS FROM SOLUTION
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq

        n = len(points)

        # Min-heap to store minimum weight edge at top.
        heap = [(0, 0)]

        # Track nodes which are included in MST.
        in_mst = [False] * n

        mst_cost = 0
        edges_used = 0

        while edges_used < n:
            weight, curr_node = heapq.heappop(heap)

            # If node was already included in MST we will discard this edge.
            if in_mst[curr_node]:
                continue

            in_mst[curr_node] = True
            mst_cost += weight
            edges_used += 1

            for next_node in range(n):
                # If next node is not in MST, then edge from curr node
                # to next node can be pushed in the priority queue.
                if not in_mst[next_node]:
                    next_weight = (
                            abs(points[curr_node][0] - points[next_node][0]) +
                            abs(points[curr_node][1] - points[next_node][1])
                    )
                    heapq.heappush(heap, (next_weight, next_node))

        return mst_cost


def main():
    print(Solution().minCostConnectPoints(
        points=[[0,0], [2,2], [3,10], [5,2], [7,0]]
    ))


if __name__ == '__main__':
    main()
