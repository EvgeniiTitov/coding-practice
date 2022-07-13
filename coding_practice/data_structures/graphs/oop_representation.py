import typing as t


"""
Key - value, some data that gets associated with a vertex, could say it is the
vertex' name. Could be a string, say NY, LA or whatever.
"""


Key = t.Any
Weight = t.Union[int, float]


class VertexAlreadyExistsError(Exception):
    """Raised if there is another vertex with the same name exists in the G"""


class Vertex:
    """
    Represents a vertex in the G. Holds references to its connections.
    """
    def __init__(self, key: Key) -> None:
        self.key = key
        self.neighbours: t.MutableMapping["Vertex", Weight] = {}

    def add_neighbour(self, neighbour: "Vertex", weight: Weight) -> None:
        self.neighbours[neighbour] = weight

    def get_connections(self) -> list["Vertex"]:
        return list(self.neighbours.keys())

    def get_neighbour_weight(self, neighbour: "Vertex") -> Weight:
        return self.neighbours.get(neighbour)

    def __str__(self) -> str:
        return (
            f"Vertex {self.key}; "
            f"Connections: {' '.join([str(n.key) for n in self.neighbours])}"
        )


class Graph:
    """
    Holds the master list of vertices, mapping keys to vertices that
    store it.
    """
    def __init__(self) -> None:
        self.vertices: t.MutableMapping[Key, Vertex] = {}

    def add_vertex(self, vertex: Vertex) -> None:
        vertex_name = vertex.key
        if vertex_name in self.vertices:
            raise VertexAlreadyExistsError(
                f"Vertex named {vertex_name} already exists"
            )
        self.vertices[vertex_name] = vertex

    def get_vertex(self, key: Key) -> t.Optional[Vertex]:
        return self.vertices.get(key)

    def add_edge(self, from_key: Key, to_key: Key, weight: Weight) -> None:
        if from_key not in self.vertices:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.vertices:
            self.add_vertex(Vertex(to_key))
        self.vertices[from_key].add_neighbour(self.vertices[to_key], weight)

    def get_vertices(self) -> list[Key]:
        return list(self.vertices.keys())

    def __contains__(self, key: Key) -> bool:
        return key in self.vertices

    def __iter__(self) -> t.Iterator[Vertex]:
        return iter(self.vertices.values())


def main():
    graph = Graph()
    for i in range(6):
        graph.add_vertex(Vertex(i))

    # graph.add_vertex(Vertex(5))  # Throws error

    graph.add_edge(0, 1, 5)
    graph.add_edge(1, 0, 3)
    graph.add_edge(0, 5, 2)
    graph.add_edge(1, 2, 4)
    graph.add_edge(2, 3, 9)
    graph.add_edge(3, 4, 7)
    graph.add_edge(3, 5, 3)
    graph.add_edge(4, 0, 1)
    graph.add_edge(5, 4, 8)
    graph.add_edge(5, 2, 1)

    for vertex in graph:
        for connection in vertex.get_connections():
            print(f"Vertex {vertex.key} -> {connection.key}")


if __name__ == '__main__':
    main()
