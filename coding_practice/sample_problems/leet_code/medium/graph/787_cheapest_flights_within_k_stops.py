from typing import List, Union


# TODO: Dijkstra, Bellman Ford solutions


"""
Summary:
    ! Some graph problems could be thought of as DP problems. DP approach with
    memoization
    
    BFS approach. Make sure to prune the solutions that exceed the number of 
    steps K.
_______________________________________________________________________________

https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are n cities connected by some number of flights. You are given an array 
flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight
from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price 
from src to dst with at most k stops. If there is no such route, return -1.

Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
"""


class Solution:

    # DP with memoization
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        def _reach_destination(
            curr_vertex: int,
            curr_steps: int,
            curr_cost: int,
        ) -> Union[float, int]:

            min_cost = float("inf")

            # Base cases
            if curr_vertex == dst:
                return curr_cost
            if curr_steps > k:
                return min_cost

            if (curr_vertex, curr_steps) in cache:
                return cache[(curr_vertex, curr_steps)]

            # Probe the solution space
            for connection in graph[curr_vertex]:
                dest_vertex, cost_to_dest_vertex = connection
                new_cost = _reach_destination(
                    dest_vertex, curr_steps + 1,
                                 curr_cost + cost_to_dest_vertex
                )
                min_cost = min(min_cost, new_cost)

            cache[(curr_vertex, curr_steps)] = min_cost

            return min_cost

        def _build_graph_repr(flights: List[List[int]]) -> dict:
            graph = {}
            for source, dest, cost in flights:
                if source not in graph:
                    graph[source] = [(dest, cost)]
                else:
                    graph[source].append((dest, cost))

                if dest not in graph:
                    graph[dest] = []

            return graph

        graph = _build_graph_repr(flights)
        cache = {}
        cost = _reach_destination(src, 0, 0)

        return -1 if cost == float("inf") else cost

    # BFS based, works but Time Limit Exceeded (28/52)
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        from queue import Queue

        def _build_graph_repr(flights: List[List[int]]) -> dict:
            graph = {}
            for source, dest, cost in flights:
                if source not in graph:
                    graph[source] = [(dest, cost)]
                else:
                    graph[source].append((dest, cost))

                if dest not in graph:
                    graph[dest] = []

            return graph

        graph = _build_graph_repr(flights)

        if dst not in graph:
            return -1

        queue = Queue()
        queue.put((0, 0, src))
        cheapest_path = float("inf")
        while queue.qsize():
            cost, number_stops, vertex = queue.get()

            if vertex == dst:
                cheapest_path = min(cheapest_path, cost)
                continue

            if number_stops > k:
                continue

            connections = graph[vertex]
            for connection in connections:
                dest_vertex, cost_to_dest_vertex = connection
                queue.put(
                    (cost + cost_to_dest_vertex, number_stops + 1, dest_vertex)
                )

        return cheapest_path if cheapest_path != float("inf") else -1


def main():
    print(Solution().findCheapestPrice(
        n=4,
        flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
        src=0,
        dst=3,
        k=1
    ))


if __name__ == '__main__':
    main()
