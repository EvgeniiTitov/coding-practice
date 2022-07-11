import typing as t
from queue import Queue

from coding_practice.data_structures.stacks.stack_implementation_2 import Stack


"""
Adjacent list; Unweighted undirected G; BFS; DFS;
"""


class VertexAlreadyExistsError(Exception):
    pass


class VertexDoesntExistError(Exception):
    pass


class UnweightedUndirectedGraph:
    def __init__(self, graph_dict: t.Optional[t.Mapping] = None) -> None:
        self._graph_dict = graph_dict or {}

    def perform_dfs(self, vertex) -> t.Iterator[str]:
        self._check_vertexes_exist(vertex)
        visited_nodes = {vertex}
        stack = Stack()
        stack.push(vertex)
        while not stack.is_empty():
            vertex = stack.pop()
            yield vertex
            for adjacent_vertex in self._graph_dict[vertex]:
                if adjacent_vertex not in visited_nodes:
                    visited_nodes.add(adjacent_vertex)
                    stack.push(adjacent_vertex)

    def perform_bfs(self, vertex) -> t.Iterator[str]:
        self._check_vertexes_exist(vertex)
        visited_nodes = {vertex}
        queue = Queue()
        queue.put(vertex)
        while queue.qsize():
            vertex = queue.get()
            yield vertex
            for adjacent_vertex in self._graph_dict[vertex]:
                if adjacent_vertex not in visited_nodes:
                    queue.put(adjacent_vertex)
                    visited_nodes.add(adjacent_vertex)

    def add_vertex(self, vertex) -> None:
        if vertex in self._graph_dict:
            raise VertexAlreadyExistsError(f"Vertex {vertex} already exists")
        self._graph_dict[vertex] = []

    def remove_vertex(self, vertex) -> None:
        self._check_vertexes_exist(vertex)
        self._remove_vertex(vertex)

    def add_edge(self, vertex1, vertex2) -> None:
        self._check_vertexes_exist(vertex1, vertex2)
        self._graph_dict[vertex1].append(vertex2)
        self._graph_dict[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2) -> None:
        self._check_vertexes_exist(vertex1, vertex2)
        self._remove_edge(vertex1, vertex2)
        self._remove_edge(vertex2, vertex1)

    def _remove_vertex(self, vertex) -> None:
        affected_vertexes = self._graph_dict[vertex]
        for affected_vertex in affected_vertexes:
            self._remove_edge(affected_vertex, vertex)
        del self._graph_dict[vertex]

    def _remove_edge(self, vertex1, vertex2) -> None:
        # TODO: Multiple ways how it could be done. Ask for forgiveness not P
        try:
            self._graph_dict[vertex1].remove(vertex2)
        except ValueError:
            print(f"No edge to delete between {vertex1} and {vertex2}")

    def _check_vertexes_exist(self, *vertexes) -> None:
        missing_vertexes = []
        for vertex in vertexes:
            if vertex not in self._graph_dict:
                missing_vertexes.append(vertex)
        if len(missing_vertexes):
            raise VertexDoesntExistError(
                f"Vertexes {missing_vertexes} do not exist"
            )

    def __str__(self) -> str:
        out = []
        for vertex, edges in self._graph_dict.items():
            out.append(f"Vertex: {vertex}. Edges: {edges}")
        return "\n".join(out)


def test_2():
    graph_repr = {
        "A": ["B", "C", "D"],
        "B": ["A"],
        "C": ["A", "E"],
        "D": ["A", "F"],
        "E": ["C"],
        "F": ["D", "G"],
        "G": ["F"],
    }
    """
                       E
     B            C
           A
        
           D
           
           F
                H
           G     
    """
    # graph_repr = {
    #     "A": ["B", "C"],
    #     "B": ["A", "D", "E"],
    #     "C": ["A", "E"],
    #     "D": ["B", "E", "F"],
    #     "E": ["D", "F", "C"],
    #     "F": ["D", "E"]
    # }

    graph = UnweightedUndirectedGraph(graph_repr)
    graph.add_vertex("H")
    graph.add_edge("F", "H")
    print(graph)

    print("\nPerforming BFS")
    for vertex in graph.perform_bfs("A"):
        print(vertex, end=" ")

    print("\nPerforming DFS")
    for vertex in graph.perform_dfs("A"):
        print(vertex, end=" ")

    """
    Performing BFS
    A B C D E F G H 
    Performing DFS
    A D F H G C E B 
    """


def test_1():
    # graph_dict = {
    #     "A": ["B", "C"],
    #     "B": ["A", "E", "D"],
    #     "C": ["A", "E"],
    #     "D": ["B", "E", "F"],
    #     "E": ["C", "D", "F"],
    #     "F": ["D", "E"]
    # }
    # graph = Graph(graph_dict)
    # print(graph)
    # print()
    # graph.add_edge("E", "B")
    # print(graph)

    graph = UnweightedUndirectedGraph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    print(graph)

    print("\nDeleting edges")
    graph.remove_edge("A", "B")
    graph.remove_edge("A", "D")
    print(graph)

    print("\nDeleting vertex C")
    graph.remove_vertex("C")
    print(graph)


if __name__ == "__main__":
    test_2()
