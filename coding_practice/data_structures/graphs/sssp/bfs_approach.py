import typing as t
from queue import Queue


"""
Unweighted Directed G; SSSP using BFS
"""


Vertex = str
GraphRepr = t.Mapping[str, t.List[str]]


class VertexDoesntExistError(Exception):
    pass


class Graph:

    def __init__(self, graph: t.Optional[GraphRepr] = None) -> None:
        self._graph = graph or {}

    def find_path_bfs(
        self,
        start: Vertex,
        end: Vertex
    ) -> t.Optional[t.List[Vertex]]:
        if start not in self._graph or end not in self._graph:
            raise VertexDoesntExistError()
        queue = Queue()
        queue.put([start])
        while queue.qsize():
            path = queue.get()
            last_vertex = path[-1]
            if last_vertex == end:
                return path
            for adjacent_vertex in self._graph[last_vertex]:
                new_path = path.copy()
                new_path.append(adjacent_vertex)
                queue.put(new_path)


def main():
    graph_repr = {
        "A": ["B", "C"],
        "B": ["D", "G"],
        "C": ["D", "E"],
        "D": ["F"],
        "E": ["F"],
        "G": ["F"],
        "F": []
    }
    graph = Graph(graph_repr)

    '''
    Searching path from A to A: ['A']
    Searching path from A to F: ['A', 'B', 'D', 'F']
    Searching path from C to F: ['C', 'D', 'F']
    Searching path from C to G: None
    '''
    print("Searching path from A to A:", graph.find_path_bfs("A", "A"))
    print("Searching path from A to F:", graph.find_path_bfs("A", "F"))
    print("Searching path from C to F:", graph.find_path_bfs("C", "F"))
    print("Searching path from C to G:", graph.find_path_bfs("C", "G"))


if __name__ == '__main__':
    main()
