from __future__ import annotations
import typing as t
import heapq


"""
Neat idea how to represent the graph but the implementation sucked and I only
overcomplicated it

The algorithm iterates over vertices processing them. However, this iteration
must be done in a certain order. In implementation 1 you manually iterate over
all nodes looking for the one closest to the beginning - that shit is slow O(N),
we could do better -> min heap. Every time we pop the head we get the shortest
vertex in O(log N) time. 
"""


Node = str
Weight = t.Union[int, float]


class ConnectionDoesntExistError(Exception):
    pass


class VertexDoesntExistError(Exception):
    pass


class Vertex:
    """
    Represents a vertex, which could store a value like data - Node and a
    bunch of other related information
    """

    def __init__(self, node: Node) -> None:
        self.node = node
        self.adjacent: t.MutableMapping[Vertex, Weight] = {}
        self.distance = float("inf")
        self.visited = False
        self.previous = None

    def add_edge(self, neighbour: Vertex, weight: Weight) -> None:
        self.adjacent[neighbour] = weight

    def get_connections(self) -> t.List[Vertex]:
        return list(self.adjacent.keys())

    def get_dist_to_neighbour(self, neighbour: Vertex) -> Weight:
        if neighbour not in self.adjacent:
            raise ConnectionDoesntExistError(
                f"Vertex {self} is not connected to {neighbour}"
            )
        return self.adjacent[neighbour]

    def __lt__(self, other: Vertex) -> bool:
        return self.distance < other.distance

    def __repr__(self) -> str:
        connections = [
            f"{pair[0].node, pair[1]}" for pair in self.adjacent.items()
        ]
        return f"Vertex {self.node}; " f"Connections: {' '.join(connections)}"


class Graph:
    def __init__(self) -> None:
        self._vertices: t.MutableMapping[Node, Vertex] = {}
        self._num_vertices = 0

    def add_vertex(self, node: Node) -> Vertex:
        self._num_vertices += 1
        new_vertex = Vertex(node)
        self._vertices[node] = new_vertex
        return new_vertex

    def add_vertices(self, *nodes: Node) -> t.List[Vertex]:
        vertices = []
        for node in nodes:
            vertices.append(self.add_vertex(node))
        return vertices

    def get_vertex(self, node: str) -> Vertex:
        if node not in self._vertices:
            raise VertexDoesntExistError(f"Vertex {node} doesn't exist")
        return self._vertices[node]

    def add_edge(
        self, node1: Node, node2: Node, weight: Weight, undirected: bool = True
    ) -> None:
        if node1 not in self._vertices:
            raise VertexDoesntExistError(f"Vertex {node1} doesn't exist")
        if node2 not in self._vertices:
            raise VertexDoesntExistError(f"Vertex {node2} doesn't exist")
        self._vertices[node1].add_edge(
            neighbour=self._vertices[node2], weight=weight
        )
        if undirected:
            self._vertices[node2].add_edge(
                neighbour=self._vertices[node1], weight=weight
            )

    def get_vertices(self) -> t.List[Node]:
        return list(self._vertices.keys())

    def __iter__(self) -> t.Iterator[Vertex]:
        return iter(self._vertices.values())

    def __str__(self) -> str:
        return f"Graph. Vertices: {self._vertices}"


def calculate_paths(graph: Graph, start: Node):
    start = graph.get_vertex(start)

    # Set distance of the start vertex to 0
    start.distance = 0

    # Create a min heap storing distances from start to the nodes to process
    nodes = [(vertex.distance, vertex) for vertex in graph]
    heapq.heapify(nodes)

    while len(nodes):
        # Pop the closest vertex to the start (start at the very beginning)
        current = heapq.heappop(nodes)[1]
        current.visited = True

        for adjacent_neighbour, weight in current.adjacent.items():
            # Same vertex could be reached and processed from different
            # directions, skip processed ones - for them distance to their
            # neighbours was already calculated
            if adjacent_neighbour.visited:
                continue

            # From start to the neighbouring vertex
            new_dist = current.distance + current.get_dist_to_neighbour(
                adjacent_neighbour
            )
            # Adjacent neighbours distance is either inf or another value
            # that could have already been calculated from a different vertex
            if new_dist < adjacent_neighbour.distance:
                adjacent_neighbour.distance = new_dist
                adjacent_neighbour.previous = current

        # Since values on the heap got modified (the distance attribute),
        # rebuild the heap
        del nodes
        nodes = [
            (vertex.distance, vertex) for vertex in graph if not vertex.visited
        ]
        heapq.heapify(nodes)


def get_the_shortest_path(dest_vertex: Vertex, path: t.List[Node]) -> None:
    if dest_vertex.previous:
        path.append(dest_vertex.previous.node)
        get_the_shortest_path(dest_vertex.previous, path)


def main():
    graph = Graph()
    graph.add_vertices("a", "b", "c", "d", "e", "f")
    graph.add_edge("a", "b", 7)
    graph.add_edge("a", "c", 9)
    graph.add_edge("a", "f", 14)
    graph.add_edge("b", "c", 10)
    graph.add_edge("b", "d", 15)
    graph.add_edge("c", "d", 11)
    graph.add_edge("c", "f", 2)
    graph.add_edge("d", "e", 6)
    graph.add_edge("e", "f", 9)

    calculate_paths(graph, start="a")
    dest = graph.get_vertex("d")
    path = [dest.node]
    get_the_shortest_path(dest, path)
    print("Path to e:", path[::-1])


if __name__ == "__main__":
    main()
