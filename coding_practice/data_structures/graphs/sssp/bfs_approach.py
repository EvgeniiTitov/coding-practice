import typing as t
from queue import Queue


Vertex = str


class VertexDoesntExistError(Exception):
    pass


class Graph:

    def __init__(self, graph: t.Optional[t.Mapping[str, str]] = None) -> None:
        self._graph = graph or {}

    def perform_bfs(self, start: Vertex, end: Vertex) -> t.List[Vertex]:
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

    }


if __name__ == '__main__':
    main()