import typing as t


"""
Tags: Adjacency matrix

The algorithm finds all shortest path pairs. The graph needs to be represented
as an adjacency matrix. 

Example graph definition:

    A   B   C   D

A   0   8  INF  1

B  INF  0   1  INF
  
C   4  INF  0  INF

D  INF  2   9   0

The diagonal ^ is 0s because the node's distance to itself if 0.

INF - means from this vertex you cannot directly reach the other one

Complexities:
T: O(V ^ 3)
S: O(V ^ 2)
"""


Graph = list[list[t.Any]]
INF = float("inf")


def print_adjacent_matrix(nb_vertices: int, graph: Graph) -> None:
    for i in range(nb_vertices):
        print()
        for j in range(nb_vertices):
            if graph[i][j] == INF:
                print("INF", end=" ")
            else:
                print(graph[i][j], end=" ")


def perform_floyd_warshall(nb_vertices: int, graph: Graph) -> Graph:
    distances = graph
    # Take all vertices one by one as a source V. Iterating over rows, each
    # row represents connections from the current vertex
    for i in range(nb_vertices):
        # Iterate over all cells in the matrix
        for row in range(nb_vertices):
            for col in range(nb_vertices):
                # If direct distance is greater than through another node,
                # pick the one going through another node
                # distances[row][col] = min(
                #     distances[row][col], distances[row][i] + distances[i][col]
                # )

                # OR
                curr_dist = distances[row][col]
                new_dist = distances[row][i] + distances[i][col]
                if new_dist < curr_dist:
                    distances[row][col] = new_dist

    return distances


def main():
    graph = [
        [0, 8, INF, 1],
        [INF, 0, 1, INF],
        [4, INF, 0, INF],
        [INF, 2, 9, 0]
    ]
    nb_vertices = 4
    distances = perform_floyd_warshall(nb_vertices, graph)
    print_adjacent_matrix(nb_vertices, distances)


if __name__ == '__main__':
    main()
