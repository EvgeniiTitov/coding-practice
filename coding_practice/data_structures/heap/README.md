#### Theory (https://docs.python.org/3/library/heapq.html)

Heap is a data structure that follows a complete binary tree's property and 
satisfies the heap property. Therefore, it is also known as a binary heap. 

Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for all k, 
counting elements from 0. For the sake of comparison, non-existing elements are 
considered to be infinite. The interesting property of a heap is that a[0] is 
always its smallest element.

```
                               0

              1                                 2

      3               4                5               6

  7       8       9       10      11      12      13      14

15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30
```

As we all know, the complete binary tree is a tree with every level filled and 
all the nodes are as far left as possible. In the binary tree, it is possible 
that the last level is empty and not filled. In the heap data structure, we 
assign key-value or weight to every node of the tree. Now, the root node key 
value is compared with the children’s nodes and then the tree is arranged 
accordingly into two categories i.e., max-heap and min-heap. 

Heap data structure is basically used as a heapsort algorithm to sort the elements 
in an array or a list. Heapsort algorithms can be used in priority queues, 
order statistics, Prim's algorithm or Dijkstra's algorithm, etc. In short, 
the heap data structure is used when it is important to repeatedly remove the
objects with the highest or the lowest priority.


Max/Min Heap implementation - https://favtutor.com/blogs/heap-in-python

---

#### Time complexity / API:

Python's heapq is a binary heap with time complexity:

- O(log N) for pushing and poping (needs to be rearranged)
- O(N) for heapifying inplace operation

API:

- heapq.heapify(x): transform list x into a heap, in place, linear time O(N)
- heapq.heappush(heap, item): push item onto the heap O(log N)
- heapq.heappop(heap): pop and return the smallest item from the heap O(log N)
- To access the smallest item without popping it: heap[0], O(1)
- heapq.heappushpop(heap, item): push item onto the heap, then pop the smallest 
and return it. The combination of heappush() followed by heappop()
- heapq.nlargest(n, iterable, key=None): return a list with N largest elements 
from the heap
- heapq.nsmallest(n, iterable, key=None): return a list with N smallest elements 
from the heap
- heapq.merge(*iterables, key=None, reverse=False): merge multiple sorted inputs
into a single sorted output (iterator)
---

#### To remember:

- If values in your heap get updates, say distance to graph vertices, the heap
won't rebuild itself, you need to do it manually! (custom objects)
