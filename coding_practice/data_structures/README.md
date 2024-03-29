### TODO:

- AVL trees and why self-balancing is important for trees

- B-tree (relevant to DB design)

- LSM-tree (relevant to DB design)

- Merkle tree implementation (relevant to DB design)

- Graphs (stopped at 355, pending: Min spanning trees, Floyd Warshall, Kruskal and Prim's)

- Watch Circular Singly/Doubly LL

---

When dealing with data structures, its worth paying attention to:
1) Time complexity 
2) Space complexity
3) Thread safety

---

### Time complexities:

In reality, time complexities listed below could differ depending on the 
implementation. Say, a poor stack implementation using an array could result 
in push being O(N) in case of underlying array being copied to a larger 
memory chunk as it grows etc

- ### Array

    - Access - O(1)
    - Search - O(N)
    - Insert - O(N)
    - Delete - O(N)
    - len() - O(1)
    - min(), max() - O(N)
    - contains - O(N)
    - .append() - O(1)
    - .pop() last - O(1)
    - .pop() intermediate - O(N)
    - .sort() - O(N log N)


- ### Set

    - contains - O(1)
    - .remove() - O(1)
    - .add() - O(1)

  Collisions could lead to O(N)


- ### Hash Map

    - Contains - O(1), worst case O(N)
    - Set item - O(1), worst case O(N)
    - Get item - O(1), worst case O(N)
    - Delete item - O(1), worst case O(N)
    - Iteration - O(N)
  
  Collisions could lead to O(N)
  

- ### Stack

  - Push - O(1)
  - Pop - O(1)
  - Peek - O(1)
  - Search - O(N)
  - Size - O(1)


- ### Queue

  - Put/Enqueue - O(1)
  - Get/Dequeue - O(1)
  - Search - O(N)
  - Size - O(1)


- ### Singly Linked List

  - Access - O(N)
  - Search - O(N)
  - Insertion - O(1): at the beginning, O(N): at the end
  - Deletion - O(1): current node


- ### Doubly Linked List

  - Access - O(N)
  - Search - O(N)
  - Insertion - O(1)
  - Deletion - O(1)


- ### Circular Singly Linked List

  - Creation - O(1)
  - Insertion - O(N)
  - Searching - O(N)
  - Traversing - O(N)
  - Node deletion - O(N)
  - Deletion of the entire LL - O(1)


- ### Circular Doubly Linked List

  - Creation - O(1)
  - Insertion - O(N)
  - Searching - O(N)
  - Traversing (forward, backwards) - O(N)
  - Node deletion (on edges its O(1)) - O(N)
  - Deletion of the entire LL - O(N)


- ### Binary Search Tree (balanced)
  
  - Access - O(log N)
  - Search - O(log N)
  - Insertion - O(log N)
  - Deletion - O(log N)


- ### Heap (Priority Queue)

  - Heapify() - O(N)
  - Push() - O(log N)
  - Pop() - O(log N)
  - Size - O(1)
  - Creating a heap by pushing N elements to an empty (initially heap) is - O(N log N), 
  don't do it, heapify an array instead


- ### Merkle Tree (hash tree)

  - Space - O(N)
  - Searching - O(log N)
  - Traversal - O(N)
  - Insertion - O(log N)
  - Deletion - O(log N)
  - Synchronization - O(log N)


- ### Tries (TBA)


- ### Graph (TBA)


- ### AVL Tree (TBA)
