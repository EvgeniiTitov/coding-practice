from __future__ import annotations
from collections import defaultdict


"""
Weighted directed G; Dijkstras
"""


Vertex = str


class VertexDoesntExistError(Exception):
    pass


class Graph:

    def __init__(self) -> None:
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_vertices(self, *vertices: Vertex) -> None:
        for vertex in vertices:
            self.nodes.add(vertex)

    def add_edge(
        self,
        vertex1: Vertex,
        vertex2: Vertex,
        dist: int | float
    ) -> None:
        if vertex1 not in self.nodes or vertex2 not in self.nodes:
            raise VertexDoesntExistError()
        self.edges[vertex1].append(vertex2)
        self.distances[(vertex1, vertex2)] = dist

    def __str__(self) -> str:
        return (
            f"Graph. \nNodes: {self.nodes}. \nEdges: {self.edges}. "
            f"\nDistances: {self.distances}"
        )


def find_paths_using_dijkstra(graph: Graph, initial: Vertex) -> tuple:
    """
    Calculates distances to all vertices in the graph

    We start from the start vertex. Every iteration we calculate distances from
    the vertex to its neighbours, once its done the vertex is processed, we pop
    it all the set of vertices to process.

    Then, we get a new vertex to process - the one we've calculated distance to
    (seen it, otherwise we would start from a vertex not connected to our paths
    from the start), we could have multiple candidates to become the next vertex
    to process - prioritise the one with shorter distance from the initial one.

    For the new vertex we calculate distances to its neighbours. What is important
    is that some neighbours could have already been visited and the distances
    to them are calculated, we update their distances and paths only if the new
    vertex can offer a shorter path.

    Slowly repeat the process until all nodes have been processed (popped).
    What we end up with is a dictionary with distances to all vertices calculated
    and their paths.
    """
    # Initially the only visited node is the one we start from
    visited_nodes = {initial: 0}
    paths = defaultdict(list)
    nodes = graph.nodes.copy()
    while nodes:
        min_node = None
        # Every iter we find a node to start from, must be closest to the start,
        # i.e. has smallest distance/weight. This node is the one we've visited
        # before (calculated distance to) BUT which haven't been processed yet
        # (from which we calculated distances to its neighbours and then pop)
        for node in nodes:
            if node in visited_nodes:
                # First FOR iter min_node is None, pick a random seen vertex
                if not min_node:
                    min_node = node
                # However, we could reassign the min_node if we find a better
                # candidate (smaller weights/distance value)
                elif visited_nodes[node] < visited_nodes[min_node]:
                    min_node = node

        # All nodes processed
        if not min_node:
            break

        # Every node gets processed just once, once distance to its neighbours
        # was calculated, get rid of the current node
        nodes.remove(min_node)
        current_weight = visited_nodes[min_node]

        # Iterate over edges of the current min node and a) if haven't calculated
        # distance to it yet, calculate OR b) check if distance from the curr
        # node is smaller than the previous distance (from different vertex)
        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited_nodes or weight < visited_nodes[edge]:
                visited_nodes[edge] = weight
                paths[edge].append(min_node)

    return visited_nodes, paths


def main():
    graph = Graph()
    graph.add_vertices("A", "B", "C", "D", "E", "F", "G")
    graph.add_edge("A", "B", 2)
    graph.add_edge("A", "C", 5)
    graph.add_edge("B", "C", 6)
    graph.add_edge("B", "D", 1)
    graph.add_edge("B", "E", 3)
    graph.add_edge("C", "F", 8)
    graph.add_edge("D", "E", 4)
    graph.add_edge("E", "G", 9)
    graph.add_edge("F", "G", 7)
    print(graph)

    print("\nRunning Dijkstras")
    distances, paths = find_paths_using_dijkstra(graph, "A")
    for k in distances:
        print(f"Distance to {k} is {distances[k]}")


if __name__ == '__main__':
    main()
