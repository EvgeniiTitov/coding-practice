import heapq


"""
Prims algorithm:
    
    1. Pick a point in the graph to start from
    2. Go through the graph/tree to find the point that is the shortest distance
       away from the current points in the MST (current solution could be 1+
       vertices, these vertices connect to other vertices, find the shortest
       unvisited vertex to go to across all visited vertices)
    3. Add the selected vertex to the solution
    4. Repeat 2,3 till the N vertices in the solution == total N vertices in G
"""


def perform_prims(graph: list[list[tuple]], source_index: int):
    edges = []
    weights = []
    visited_vertices = {source_index}

    while len(visited_vertices) < len(graph):

        # Find the next vertex to go to. Consider all possible moves from the
        # existing solution (MST)
        moves = []
        for visited_vertex in visited_vertices:
            for node in graph[visited_vertex]:
                next_vertex, next_vertex_weight = node
                if next_vertex not in visited_vertices:
                    heapq.heappush(
                        moves, (next_vertex_weight, visited_vertex, next_vertex)
                    )
        # Pick the closest vertex (for the existing solution)
        next_vertex_weight, visited_vertex, next_vertex = heapq.heappop(moves)

        visited_vertices.add(next_vertex)
        weights.append(next_vertex_weight)
        edges.append((visited_vertex, next_vertex))

    return edges, weights


def main():
    # Index is the vertex, values are the vertex it connects to and the weight
    graph = [
        [(1, 2), (3, 6)],
        [(0, 2), (2, 3), (3, 8), (4, 5)],
        [(1, 3), (4, 7)],
        [(0, 6), (1, 8), (4, 9)],
        [(1, 5), (2, 7), (3, 9)]
    ]
    edges, weights = perform_prims(graph, 0)
    for edge, weight in zip(edges, weights):
        print(edge, weight)


if __name__ == '__main__':
    main()
