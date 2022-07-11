### Graph types

- Undirected Unweighted
- Directed Unweighted
- Undirected Weighted Positive
- Undirected Weighted Negative
- Directed Weighted Positive
- Directed Weighted Negative

---

### Terms

- Indegree of a vertex - N of directed edges going into it
- Outdegree of a vertex - N of directed edges going out of it
- Complete graph - simple undirected G where every pair of distinct vertices is
connected by a unique edge, i.e. every vertex is connected to all other vertices

---

### Graph representations

1. Adjacency list / ll - essentially a dictionary where keys are vertices and
values are the vertices a vertex is connected to. Could simulate directed and
undirected graphs
```python
graph_repr = {
        "A": ["B", "C", "D"],
        "B": ["A"],
        "C": ["A", "E"],
        "D": ["A", "F"],
        "E": ["C"],
        "F": ["D", "G"],
        "G": ["F"],
    }
```

2. Adjacency matrix - TBA

---


### Graph traversal

The intuition is simple - start at a vertex, add all its *unseen* neighbours to 
the queue / stack, repeat. Queue allows to simulate BFS because we pop vertices
around the starting vertex / previous vertices straight away rather than 
pushing them down the stack

- #### Breadth First Search (BFS)

```python
def perform_bfs(self, vertex) -> t.Iterator[str]:
    self._check_vertexes_exist(vertex)
    visited_nodes = {vertex}
    queue = Queue()
    queue.put(vertex)
    while queue.qsize():
        vertex = queue.get()
        yield vertex
        for adjacent_vertex in self._graph_dict[vertex]:
            if adjacent_vertex not in visited_nodes:
                queue.put(adjacent_vertex)
                visited_nodes.add(adjacent_vertex)
```

- #### Depth First Search (DFS)

```python
def perform_dfs(self, vertex) -> t.Iterator[str]:
    self._check_vertexes_exist(vertex)
    visited_nodes = {vertex}
    stack = Stack()
    stack.push(vertex)
    while not stack.is_empty():
        vertex = stack.pop()
        yield vertex
        for adjacent_vertex in self._graph_dict[vertex]:
            if adjacent_vertex not in visited_nodes:
                visited_nodes.add(adjacent_vertex)
                stack.push(adjacent_vertex)
```
---

### Topological sort

DAGs. The intuition - start at a vertex, keep propagating down until we reach a
vertex that has no *kids*. At this point stop recursive calls, add the vertex
to the stack, complete the recursive call going one way *up* in the recursion
call stack, check if there are other vertices to go to. Yes, go there. No, add
vertex to the stack and go *up* again, repeat.

You could start from 1+ vertices, in this case all subsequent traversals will
pick up remaining vertices (unseen) that haven't been collected yet.

Vertices at the *end* of the graph end up deep in the stack whereas *parents* 
at the start

```python
def perform_topological_sort(
    self, start_vertex: t.Optional[Vertex] = None
) -> None:
    visited_vertices = set()
    stack = Stack()
    if start_vertex:
        if start_vertex not in self._graph:
            raise VertexDoesntExistError(
                f"Vertex {start_vertex} doesn't exist"
            )
        self._perform_topological_sort(
            start_vertex, visited_vertices, stack
        )
    else:
        # That shit's bad, isn't it?
        for vertex in self._graph.keys():  # T: O(E + V)
            if vertex not in visited_vertices:
                self._perform_topological_sort(
                    vertex, visited_vertices, stack
                )
    print(f"{' -> '.join(reversed(stack._data))}")

def _perform_topological_sort(
    self, vertex: Vertex, visited: set, stack: Stack
) -> None:
    visited.add(vertex)
    # If a vertex has *kids*, keep propagating deeper
    for dependent_vertex in self._graph[vertex]:  # T: O(E)
        if dependent_vertex not in visited:
            self._perform_topological_sort(
                dependent_vertex, visited, stack
            )
    # Once the vertex with no *kids* reached, add it to stack and go one
    # level up in the recursive call stack to check if the previous vertex
    # has other dependent nodes to go to
    stack.push(vertex)
```

---


### Single Source Shortest Path Problem (SSSP)

- ### BFS 
Very similar to BFS except for instead of placing vertices in the queue we
place paths seen to far where the last vertex in the path is the vertex we're
going in to next iteration. So, say your starting vertex A points to 3 vertices B C and D.
Your queue would be:
1. [A]
2. [A, B], [A, C], [A, D],
3. etc until one of the paths reaches the destination node if possible (no 
guarantees for directed graph)

Works only for unweighted directed/undirected graphs.

```python
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
```

- ### Dijkstra's

Algorithm:

```
1. Mark all nodes unvisited (set of invisited nodes)

2. Initial node’s value is 0. Infinity for all other nodes. Set the initial node as current. 

3. During the run, the tentative distance between the source and a current node 
is the shortest distance discovered so far. For the current node, consider all 
of its unvisited neighbours and calculate their tentative distance through the 
current node. Compare the newly calculated distance to the one currently 
assigned to the neighbour and assign the smaller one. For example, if the current 
node A is marked with a distance of 6, and the edge connecting it with a neighbor 
B has length 2, then the distance to B through A will be 6 + 2 = 8. If B was 
previously marked with a distance greater than 8 then change it to 8. Otherwise, 
the current value will be kept.

4. When done considering all of the unvisited neighbours of the current node, 
mark the current node as visited and remove it from the unvisited set. A visited 
node will never be checked again.

5. If the destination node has been marked visited (when dealing with 2 specific 
nodes) or if the smallest tentative distance among the nodes in the unvisited 
set is infinity (complete traversal, when there is no connection between the 
initial node and remaining unvisited nodes), then stop.

6. Otherwise, select the unvisited node marked with the smallest tentative distance, 
go there by setting it as the new current node. Go to step 3.
```

We operate on 3 things: nodes, edges, weights / distances

1. Approach 1

```python
def find_paths_using_dijkstra(graph: Graph, initial: Vertex) -> tuple:
    """
    Calculates distances to all vertices in the graph
    
    We start from the start vertex. Every iteration we calculate distances from
    the vertex to its neighbours, once it's done the vertex is processed, we pop 
    it all the set of vertices to process. 
    
    Then, we get a new vertex to process - the one we've calculated distance to
    (seen it, otherwise we would start from a vertex not connected to our paths 
    from the start), we could have multiple candidates to become the next vertex 
    to process - prioritise the one with shorter distance from the initial one. 
    
    For the new vertex we calculate distances to its neighbours. What is important
    is that some neighbours could have already been visited and the distances
    to them are calculated, we update their distances and paths only if the new
    vertex can offer a shorter path. 
    
    Slowly repeat the process until all nodes have been processed (popped). 
    What we end up with is a dictionary with distances to all vertices calculated 
    and their paths.
    """
    # Initially the only visited node is the one we start from
    visited_nodes = {initial: 0}
    paths = defaultdict(list)
    nodes = graph.nodes.copy()
    while nodes:
        min_node = None
        # Every iter we find a node to start from, must be closest to the start,
        # i.e. has smallest distance/weight. This node is the one we've visited
        # before (calculated distance to) BUT which haven't been processed yet
        # (from which we calculated distances to its neighbours and then pop)
        for node in nodes:
            if node in visited_nodes:
                # First FOR iter min_node is None, pick a random seen vertex
                if not min_node:
                    min_node = node
                # However, we could reassign the min_node if we find a better
                # candidate (smaller weights/distance value)
                elif visited_nodes[node] < visited_nodes[min_node]:
                    min_node = node

        # All nodes processed
        if not min_node:
            break

        # Every node gets processed just once, once distance to its neighbours
        # was calculated, get rid of the current node
        nodes.remove(min_node)
        current_weight = visited_nodes[min_node]

        # Iterate over edges of the current min node and a) if haven't calculated
        # distance to it yet, calculate OR b) check if distance from the curr
        # node is smaller than the previous distance (from different vertex)
        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited_nodes or weight < visited_nodes[edge]:
                visited_nodes[edge] = weight
                paths[edge].append(min_node)

    return visited_nodes, paths
```

---

