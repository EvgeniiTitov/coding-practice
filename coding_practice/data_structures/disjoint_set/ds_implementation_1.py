import typing as t


"""
Each node in a disjoint-set forest consists of a pointer and some auxiliary 
info (a size or a rank, but not both).
The pointers are used to mke parent pointer trees, where each node that is not
the root of a tree points to its parent. 
Each tree represents a set stored in the forest, with the members of the set
being the nodes in the tree. 
Root nodes provide set representatives: two nodes are in the same set if and 
only if the roots of the trees containing the nodes are equal.

So, each node has a value and a pointer that points to the root of the set it 
is currently in. If it points to itself, it is not a part of any other set.

    find() - follows the chain of parent pointers from a specified query node X 
until it reaches a root element. The root element represents the set to which
X belongs, could be X itself. Returns the root element it reaches.

    union(x, y) - replaces the set containing X and the set containing Y with
their union. Union first uses Find() to determine the roots of the trees which
contain X and Y. If they are the same, no need to do anything. Otherwise, the
trees get merged by either setting the parent pointer of X to Y or vice versa.

The efficient Union implementation uses union by size or by rank. This info is
used to decide which node becomes the new parent when they get united. It makes
sure the trees do not become too deep. 

Union by rank: when initialised, the node's ranks are 0. To merge trees with
roots X and Y, first compare their ranks. If they are !=, the larger rank tree
becomes the parentm their ranks don't change. Else, then either could become
the parent, but the new parent's rank += 1.

    Time complexity:
    - FIND and UNION require O(N) time. Other implementations could have 
    slightly different times. 
"""


Vertex = t.Any
Child = Vertex
Parent = Vertex


class DisjointSet:
    def __init__(self, vertices: list[Vertex]) -> None:
        self.vertices = vertices

        # Initially nodes have themselves as parents(not part of any other set)
        self.parent: t.MutableMapping[Child, Parent] = {}
        for vertex in vertices:
            self.parent[vertex] = vertex

        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item: Vertex) -> Vertex:
        """
        Returns the root element it reaches (the set root the node item belongs
        to)
        """
        if self.parent[item] == item:
           return item
        else:
            return self.find(self.parent[item])

    def union(self, x: Vertex, y: Vertex):
        x_root = self.find(x)
        y_root = self.find(y)
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            # Y's parent is X now, so X's rank increases
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

    def __str__(self) -> str:
        return f"DisjointSet, parents: {self.parent}, ranks: {self.rank}"


def main():
    vertices = ["A", "B", "C", "D", "E"]

    """
    STDOUT:
    
    DisjoinSet, parents: {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}, 
                ranks: {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    Parent of A is A
    DisjoinSet, parents: {'A': 'A', 'B': 'A', 'C': 'C', 'D': 'D', 'E': 'E'}, 
                ranks: {'A': 1, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    Parent of B is A
    DisjoinSet, parents: {'A': 'A', 'B': 'A', 'C': 'A', 'D': 'D', 'E': 'E'}, 
                ranks: {'A': 1, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    Parent of S is A
    
    ^ This is important, despite union-ing B and C, C's parent is still A 
    because B's parent is A. A is the root of this subset!
    """

    ds = DisjointSet(vertices)
    print(ds)

    print("Parent of A is", ds.find("A"))  # A - the parent of A is A

    ds.union("A", "B")
    print(ds)
    print("Parent of B is", ds.find("B"))

    ds.union("B", "C")
    print(ds)
    print("Parent of S is", ds.find("C"))


if __name__ == '__main__':
    main()
