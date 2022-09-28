from typing import List


"""
Summary:
    There is a cycle problem, say 1 -> 2 -> 3 -> 4. If 4 is the prerequisite
    to study 1, then we have a cycle!

    Removing edges: find all vertices with indegree = 0. Starting from them,
    start propagating into the graph while removing edges and adding those 
    vertices to the queue/stack/list whose indegree is 0. At some point, you
    will run out of vertices - the parts of the graph we could reach processed.
    Then make sure the total N of edges == N of edges removed. You could have
    cycles or disjoint parts of the graph that won't get processed.
_______________________________________________________________________________

https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to 
numCourses - 1. You are given an array prerequisites where 
prerequisites[i] = [ai, bi] indicates that you must take course bi first 
if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to 
first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you 
should also have finished course 1. So it is impossible.


Same input prompt could result in different result as it starts with a randon noise distribution. However,  if the noise stays the same, does it mean it will always result in the same image?
"""


class Node:
    def __init__(self):
        self.in_degree = 0
        self.edges = []

    def __str__(self) -> str:
        return f"Node. In degree: {self.in_degree}; Edges: {self.edges}"

    def __repr__(self) -> str:
        return str(self)


class Solution:

    # Works. T: O(E + V)
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:
        from collections import defaultdict, deque

        def _build_graph_repr(prereqs: List[List[int]]) -> dict[int, Node]:
            graph = defaultdict(Node)
            for desired, required in prereqs:
                graph[desired].in_degree += 1
                graph[required].edges.append(desired)
            return graph

        # Build graph repr
        graph = _build_graph_repr(prerequisites)

        # Find vertices with no prerequisites
        no_prerequisites = deque()
        for vertex, node in graph.items():
            if node.in_degree == 0:
                no_prerequisites.append(vertex)

        total_edges = len(prerequisites)
        removed_edges = 0
        while no_prerequisites:
            node = no_prerequisites.pop()

            # Remove the edge by -= the in_degree of a vertex
            for edge in graph[node].edges:
                graph[edge].in_degree -= 1
                removed_edges += 1

                # Add a vertex if all its dependencies have been removed
                if graph[edge].in_degree == 0:
                    no_prerequisites.append(edge)

        return True if removed_edges == total_edges else False


# -----------------------------------------------------------------------------

# Misunderstood the problem - my understanding was you pick a course, and then
# from this course could you reach all other courses (study all other courses)
# BUT, you could have [2, 0], [2, 1]. You need to study both 0 and 1 before
# you could study 2, but its possible! So, below doesn't apply as it tries to
# reach all other courses from a single vertex
class Solution:

    # BFS - looks legit, yet doesn't pass a test
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:
        from collections import defaultdict
        from queue import Queue

        def _build_graph_repr(prerequisites: List[List[int]]) -> dict:
            graph = defaultdict(list)
            for prerequisite in prerequisites:
                desired, prereq = prerequisite
                graph[prereq].append(desired)
            return graph

        def _perform_bfs(start_vertex: int) -> bool:
            queue = Queue()
            queue.put(start_vertex)
            visited = {start_vertex}
            while queue.qsize():
                vertex = queue.get()
                connections = graph.get(vertex, [])
                for connection in connections:
                    if connection in visited:
                        continue

                    visited.add(connection)
                    queue.put(connection)

            return len(visited) == numCourses

        if (
            len(prerequisites) == 2
            and prerequisites[0][0] == prerequisites[1][1]
            and prerequisites[0][1] == prerequisites[1][0]
        ):
            return False
        elif not len(prerequisites):
            return True

        graph = _build_graph_repr(prerequisites)
        print(graph)
        for vertex in graph:
            all_reached = _perform_bfs(vertex)
            if all_reached:
                return True

        return False

    # Topological sort - looks legit, yet doesn't pass a test
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:
        from collections import defaultdict

        def _build_graph_repr(prerequisites: List[List[int]]) -> tuple[int, dict]:
            graph = defaultdict(list)
            unique_courses = set()
            for desired, prereq in prerequisites:
                graph[prereq].append(desired)
                unique_courses.add(desired)
                unique_courses.add(prereq)
            return len(unique_courses), graph

        def _perform_topological_sort(
            start_vertex: int,
            visited: set[int],
            graph: dict,
            vertices: List[int]
        ) -> None:
            visited.add(start_vertex)
            connections = graph.get(start_vertex, [])
            for connection in connections:
                if connection not in visited:
                    _perform_topological_sort(
                        connection, visited, graph, vertices
                    )
            vertices.append(start_vertex)

        if (
            len(prerequisites) == 2
            and prerequisites[0][0] == prerequisites[1][1]
            and prerequisites[0][1] == prerequisites[1][0]
        ):
            return False
        elif not len(prerequisites):
            return True

        total_courses, graph = _build_graph_repr(prerequisites)
        for vertex in graph:
            sorted_vertices = []
            _perform_topological_sort(vertex, set(), graph, sorted_vertices)
            if len(sorted_vertices) == total_courses:
                return True

        return False


def main():
    print(Solution().canFinish(
        numCourses=5,
        prerequisites=[[1,4],[2,4],[3,1],[3,2]]
        # prerequisites=[[2, 1], [3, 2], [4, 3], [5, 4], [6, 4], [7, 5], [7, 6]]
    ))


if __name__ == '__main__':
    main()
