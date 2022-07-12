from __future__ import annotations
import typing as t


"""
Bellman Ford; Directed Weighted Negative G;
"""


Inf = float("Inf")


class Graph:
    def __init__(self) -> None:
        self._graph: list[list] = []
        self._nodes: list[str] = []

    def add_edge(self, source: str, dest: str, weight: int | float) -> None:
        self._graph.append([source, dest, weight])

    def add_nodes(self, *value: str) -> None:
        for node in value:
            self._nodes.append(node)

    def find_paths_using_bellman_ford(
        self, source: str
    ) -> t.Optional[t.MutableMapping]:
        distances: t.MutableMapping[str, int | float] = {
            node: Inf for node in self._nodes
        }
        distances[source] = 0

        for _ in range(len(self._nodes) - 1):

            """
            Iterate over vertices pairs updating their weights.

            Every iter we consider a pair of vertices and distance between them
            All set of vertices is considered
            If src (start) vertex has its distance calculated (its either 0 for
            source or was calculated in previous iterations) AND its distance
            from source + distance src to dest < than the current dest distance
            (could be inf or another value calculated from a different vertex),
            update it
            """
            for src, dest, weight in self._graph:
                if (
                    distances[src] != Inf
                    and distances[src] + weight < distances[dest]
                ):
                    distances[dest] = distances[src] + weight

        """
        Identify negative cycle. We run the logic above V'th time, above we
        ran it V - 1, we expect no changes, if anything changes -> cycle
        """
        for src, dest, weight in self._graph:
            if (
                distances[src] != Inf
                and distances[src] + weight < distances[dest]
            ):
                print("Graph contains a negative cycle")
                return None

        return distances


def main():
    graph = Graph()
    graph.add_nodes("A", "B", "C", "D", "E")
    graph.add_edge("A", "C", 6)
    graph.add_edge("A", "D", 6)
    graph.add_edge("B", "A", 3)
    graph.add_edge("C", "D", 1)
    graph.add_edge("D", "C", 2)
    graph.add_edge("D", "B", 1)
    graph.add_edge("E", "B", 4)
    graph.add_edge("E", "D", 2)
    distances = graph.find_paths_using_bellman_ford("E")
    print(distances)
    # TODO: Debug me, add comments and add to the Graph's summary


if __name__ == "__main__":
    main()
