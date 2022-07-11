#### Heap

Heap is a data structure that follows a complete binary tree's property and 
satisfies the heap property. Therefore, it is also known as a binary heap. As 
we all know, the complete binary tree is a tree with every level filled and 
all the nodes are as far left as possible. In the binary tree, it is possible 
that the last level is empty and not filled. In the heap data structure, we 
assign key-value or weight to every node of the tree. Now, the root node key 
value is compared with the children’s nodes and then the tree is arranged 
accordingly into two categories i.e., max-heap and min-heap. Heap data 
structure is basically used as a heapsort algorithm to sort the elements 
in an array or a list. Heapsort algorithms can be used in priority queues, 
order statistics, Prim's algorithm or Dijkstra's algorithm, etc. In short, 
the heap data structure is used when it is important to repeatedly remove the
objects with the highest or the lowest priority.


Max/Min Heap implementation - https://favtutor.com/blogs/heap-in-python

---

#### Time complexity:

Python's heapq is a binary heap with time complexity:

- O(log N) for pushing and poping (needs to be rearranged)
- O(N) for heapifying inplace operation

---

#### To remember:

- If values in your heap get updates, say distance to graph vertices, the heap
wont rebuild itself, you need to do it manually!

- 