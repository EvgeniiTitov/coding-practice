from collections import defaultdict
import heapq


"""
Initially we start with edges going out from the source. Heapify them to 
get access to the shortest edge. 

Start looping over available edges. 

Initially we pick the vertex closest to the source, its not visited, so we
process it by adding it to visited, adding it to the MST solution. THEN, we
add all of its unvisited neighbours (so we don't go back) to the heap.

The next iteration we pick the next CLOSEST vertex within the MST solution (
could be either from the source or newly added vertex).

Repeat until we've run out of edges to consider. 

So, we start from a source and then slowly build out solution by attaching
the shortest/closest vertices.
"""


def build_mst_with_prims(graph: dict, source: str):
    mst = defaultdict(set)
    visited = {source}
    edges = [
        (weight, source, to)
        for to, weight in graph[source].items()
    ]
    heapq.heapify(edges)

    while len(edges):
        weight, from_vertex, to_vertex = heapq.heappop(edges)
        if to_vertex not in visited:
            visited.add(to_vertex)
            mst[from_vertex].add(to_vertex)

            # Add all neighbours of the newly picked vertex to the heap
            for vertex_next, weight in graph[to_vertex].items():
                if vertex_next not in visited:
                    heapq.heappush(edges, (weight, to_vertex, vertex_next))

    return mst


def main():
    graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
        'C': {'A': 3, 'B': 1, 'F': 5},
        'D': {'B': 1, 'E': 1},
        'E': {'B': 4, 'D': 1, 'F': 1},
        'F': {'C': 5, 'E': 1, 'G': 1},
        'G': {'F': 1},
    }
    print(build_mst_with_prims(graph, "A"))


if __name__ == '__main__':
    main()
