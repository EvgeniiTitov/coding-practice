#### The broadcast problem:

How to efficiently transfer a piece of info to anyone and everyone who may be
listening. Important in gaming so that all the players know the very latest
position of every other player. 

The brute force approach would be the broadcaster sends a single copy of 
the message to every listener (it needs to maintain a list of them). The problem 
here is that the routers see many copies of the same message (the router closer 
to the broadcaster processes all of them,whereas other routers could see fewer 
copies).

The solution to this problem lies in the construction of a MST. Formally,
the min spanning tree T for a graph G(V, E) is an asyclic subset of Es that 
connects all Vs. The sum of the weights of the edges in T is minimised.

Idea of constructing a spanning tree:

```
While T is not yet a spanning tree
    Find an edge that is safe to add to the tree
    Add the new edge to T
```

A safe edge is an edge that connects a vertex that is in the spanning tree T to
a vertex that is not in the spanning tree (avoiding cycles).

---

- Prim's needs a source whereas Kruskal doesn't. It sorts the edges and then
slowly builds the solution.

