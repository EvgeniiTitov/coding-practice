from typing import List


"""
Summary: Dijkstra's with heap for efficiency
_______________________________________________________________________________

https://leetcode.com/problems/network-delay-time/

You are given a network of n nodes, labeled from 1 to n. You are also given 
times, a list of travel times as directed edges times[i] = (ui, vi, wi), where 
- ui is the source node, 
- vi is the target node, and 
- wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes 
for all the n nodes to receive the signal. If it is impossible for all the n 
nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
"""


class Solution:

    # My Dijkstras. Passed 52/53 tests wtf
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for source, dest, delay in times:
            if source in graph:
                graph[source].append((dest, delay))
            else:
                graph[source] = [(dest, delay)]
            if dest not in graph:
                graph[dest] = []

        distances = self.calculate_distances(graph, k)
        min_time = max(distances.values())
        return -1 if min_time == float("inf") else min_time

    def calculate_distances(self, graph: dict, source: int) -> dict:
        import heapq

        distances = {vertex: float("inf") for vertex in graph}
        distances[source] = 0
        visited_vertices = set()
        closest_vertices = [(0, source)]

        while len(closest_vertices):
            curr_dist_from_src, curr_vertex = heapq.heappop(closest_vertices)

            visited_vertices.add(curr_vertex)

            for neighbour, curr_to_neighbour_dist in graph[curr_vertex]:
                new_dist_to_neighbour = (
                    curr_dist_from_src + curr_to_neighbour_dist
                )
                if new_dist_to_neighbour < distances[neighbour]:
                    distances[neighbour] = new_dist_to_neighbour
                    if neighbour not in visited_vertices:
                        heapq.heappush(
                            closest_vertices,
                            (new_dist_to_neighbour, neighbour),
                        )
        return distances

    # Alternative Dijkstras
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        import heapq

        """
        [[1,2,1],[2,3,7],[1,3,4],[2,1,2]] 
        results in
        defaultdict(<class 'dict'>, {1: {2: 1, 3: 4}, 2: {3: 7, 1: 2}})
        """
        graph = defaultdict(dict)
        for source, dest, delay in times:
            graph[source][dest] = delay

        heap = [(0, k)]
        distances = {}
        while len(heap):
            curr_vertex_delay, curr_vertex = heapq.heappop(heap)

            if curr_vertex not in distances:
                distances[curr_vertex] = curr_vertex_delay
                for neighbour in graph[curr_vertex]:
                    neighbour_delay = (
                        curr_vertex_delay + graph[curr_vertex][neighbour]
                    )
                    heapq.heappush(heap, (neighbour_delay, neighbour))
        return max(distances.values()) if len(distances) == n else -1

    # My Bellman Ford. Passed 52/53 tests wtf
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = set()
        for source, dest, _ in times:
            nodes.add(source)
            nodes.add(dest)

        distances = {node: float("inf") for node in nodes}
        distances[k] = 0
        for i in range(n - 1):
            for source, dest, delay in times:
                if (
                    distances[source] != float("inf")
                    and distances[source] + delay < distances[dest]
                ):
                    distances[dest] = distances[source] + delay

        # Omit Vth iteration to detect the cycle as we know there are no
        # negative delays
        min_time = max(distances.values())
        return -1 if min_time == float("inf") else min_time

    # Alternative Bellman Ford
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float("inf") for _ in range(n)]
        distances[k - 1] = 0  # Vertices from 1 to N, array from 0, so - 1
        for _ in range(n - 1):
            for source_i, dest_i, delay in times:
                if distances[source_i - 1] + delay < distances[dest_i - 1]:
                    distances[dest_i - 1] = distances[source_i - 1] + delay
        return max(distances) if max(distances) < float("inf") else -1


def main():
    print(
        Solution().networkDelayTime(
            times=[[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]], n=4, k=1
        )
    )


if __name__ == "__main__":
    main()
