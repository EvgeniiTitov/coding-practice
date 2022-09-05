import typing as t

from coding_practice.data_structures.disjointSet_unionFind import DisjointSet


"""
Kruskal algorithm is for solving the Min Spanning Tree (MST) problem. 
It is a greedy algorithm, so we try to pick the best solution at every step. 
It finds the min spanning tree for weighted undirected graph

_______________________________________________________________________________
Algorithm:

Sort edges based on their weights, we want to start from the smallest/lightest
ones.

Use DisjoinSet to keep track of cycles, i.e. subset intersections, when adding
a new edge (pair of nodes).

Start iterating over edges, edge is between two nodes, check if addition of
this edge to the solution would introduce a cycle, i.e. both nodes belong
to the same subset. 

If that's not the case, add the current edge to the solution AND unite the 
roots of each node (each node is a set of its own, unite them into a greater
one representing the nodes/set of the current solution - min spanning tree).

IMPORTANT: MST property is its number of edges = number of vertices - 1.

The intermediate solution, say a list, could contain multiple subsets. As you
add edges, they are sorted in the ascending order, so they could come from
different parts of our graph. Eventually, all these subsets will merge into 
the single set once the MST is reached.
"""


Vertex = t.Any


class Graph:
    def __init__(self, nb_vertices: int) -> None:
        self._nb_vertices = nb_vertices
        self._graph = []
        self._nodes = []

    def add_node(self, node: Vertex) -> None:
        self._nodes.append(node)

    def add_edge(self, source: Vertex, dest: Vertex, weight: float) -> None:
        self._graph.append((source, dest, weight))

    def perform_kruskal(self) -> list[tuple[Vertex, Vertex, float]]:
        # Create disjoint set to keep track of cycles
        disjoint_set = DisjointSet(vertices=self._nodes)

        # TODO: Would using a heap be better?
        # Sort graph edges
        self._graph = sorted(self._graph, key=lambda item: item[-1])

        min_spanning_tree = []
        curr_edge_index = 0  # Edge index
        curr_nb_edges_in_mst = 0  # MST has nb vertices - 1
        while curr_nb_edges_in_mst < self._nb_vertices - 1:
            source, dest, weight = self._graph[curr_edge_index]
            curr_edge_index += 1

            # Get disjoint sets for each vertex (new edge we want to add)
            ds_source_root = disjoint_set.find(source)
            ds_dest_root = disjoint_set.find(dest)

            # Check if they belong to the same set, i.e there is a cycle. If
            # not, add the edge to the solution, increment the edges counter
            # and unite the edges into a single set.
            if ds_source_root != ds_dest_root:
                curr_nb_edges_in_mst += 1
                min_spanning_tree.append((source, dest, weight))

                # Union edges together
                disjoint_set.union(ds_source_root, ds_dest_root)

        return min_spanning_tree

    def __str__(self) -> str:
        return f"Graph. Nodes: {self._nodes}; Edges: {self._graph}"


def main():
    graph = Graph(5)
    for node in "ABCDE":
        graph.add_node(node)

    graph.add_edge("A", "B", 5)
    graph.add_edge("B", "A", 5)
    graph.add_edge("B", "D", 8)
    graph.add_edge("D", "B", 8)
    graph.add_edge("D", "C", 6)
    graph.add_edge("C", "D", 6)
    graph.add_edge("C", "B", 10)
    graph.add_edge("B", "C", 10)
    graph.add_edge("C", "A", 13)
    graph.add_edge("A", "C", 13)
    graph.add_edge("C", "E", 20)
    graph.add_edge("E", "C", 20)
    graph.add_edge("E", "A", 15)
    graph.add_edge("A", "E", 15)
    print(graph)

    print(graph.perform_kruskal())


if __name__ == '__main__':
    main()
