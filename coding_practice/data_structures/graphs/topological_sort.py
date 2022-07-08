import typing as t
from collections import defaultdict

from coding_practice.data_structures.stacks.stack_implementation_1 import Stack


"""
Adjacency list; Topological sort; Unweighted directed G;
"""


Vertex = str


class VertexDoesntExistError(Exception):
    pass


class Graph:
    def __init__(self) -> None:
        self._graph = defaultdict(list)

    def add_edge(self, vertex1: Vertex, vertex2: Vertex) -> None:
        self._graph[vertex1].append(vertex2)

    def perform_topological_sort(
        self, start_vertex: t.Optional[Vertex] = None
    ) -> None:
        visited_vertices = set()
        stack = Stack()
        if start_vertex:
            if start_vertex not in self._graph:
                raise VertexDoesntExistError(
                    f"Vertex {start_vertex} doesn't exist"
                )
            self._perform_topological_sort(
                start_vertex, visited_vertices, stack
            )
        else:
            # That shit's bad, isn't it?
            for vertex in self._graph.keys():  # T: O(E + V)
                if vertex not in visited_vertices:
                    self._perform_topological_sort(
                        vertex, visited_vertices, stack
                    )
        print(f"{' -> '.join(reversed(stack._data))}")

    def _perform_topological_sort(
        self, vertex: Vertex, visited: set, stack: Stack
    ) -> None:
        visited.add(vertex)
        # If a vertex has *kids*, keep propagating deeper
        for dependent_vertex in self._graph[vertex]:  # T: O(E)
            if dependent_vertex not in visited:
                self._perform_topological_sort(
                    dependent_vertex, visited, stack
                )
        # Once the vertex with no *kids* reached, add it to stack and go one
        # level up in the recursive call stack to check if the previous vertex
        # has other dependent nodes to go to
        stack.push(vertex)

    def __str__(self) -> str:
        return (
            f"Graph:\n"
            f"{' '.join([f'{key}: {self._graph[key]};' for key in self._graph])}"
        )


def main():
    graph = Graph()
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")
    graph.add_edge("D", "F")
    graph.add_edge("E", "H")
    graph.add_edge("E", "F")
    graph.add_edge("F", "G")
    print(graph)
    """
    Graph: 
    A: ['C']; B: ['C', 'D']; C: ['E']; D: ['F']; E: ['H', 'F']; F: ['G'];
    """

    print("\nPerforming topological sort from A")
    graph.perform_topological_sort("A")
    """
    Performing topological sort from A
    A -> C -> E -> F -> G -> H
    """

    print("\nPerforming topological sort from B")
    graph.perform_topological_sort("B")
    """
    Performing topological sort from B
    B -> D -> C -> E -> F -> G -> H
    """

    print("\nPerforming topological sort, no entry vertex provided")
    graph.perform_topological_sort()


if __name__ == "__main__":
    main()
