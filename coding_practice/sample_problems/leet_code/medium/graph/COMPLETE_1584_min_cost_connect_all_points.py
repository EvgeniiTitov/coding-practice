from typing import List, Any, MutableMapping


# TODO: Solve it with Prim algorithm as well


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


def main():
    print(Solution().minCostConnectPoints(
        points=[[0,0], [2,2], [3,10], [5,2], [7,0]]
    ))


if __name__ == '__main__':
    main()
