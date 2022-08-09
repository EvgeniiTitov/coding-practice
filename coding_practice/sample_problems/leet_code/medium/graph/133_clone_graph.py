import typing as t


"""
Summary: The idea is propagate through the graph while copying it at the same
time. To keep track of both (original and copied) vertices use a dict.
_______________________________________________________________________________

https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) 
of its neighbors:

    class Node {
        public int val;
        public List<Node> neighbors;
    }
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val == 1, the second node with val == 2, 
and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a 
finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return 
the copy of the given node as a reference to the cloned graph.


"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    # KEKL
    def cloneGraph(self, node: "Node") -> "Node":
        from copy import deepcopy

        return deepcopy(node)

    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return node

        from queue import Queue

        queue = Queue()
        queue.put(node)
        copied_vertices = {}
        copied_vertices[node] = Node(node.val)
        while queue.qsize():
            vertex = queue.get()
            for neighbour in vertex.neighbors:
                if neighbour not in copied_vertices:
                    copied_vertices[neighbour] = Node(neighbour.val)
                    queue.put(neighbour)
                copied_vertices[vertex].neighbors.append(
                    copied_vertices[neighbour]
                )

        return copied_vertices[node]
