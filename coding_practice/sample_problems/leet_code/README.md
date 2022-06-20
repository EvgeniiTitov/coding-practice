### General information:

"Most questions fall into some category of DP/memoization, DFS/BFS, two pointer,
sort/binary search, or Hash table/counting occurrences in my experience"

- DFS: Finding out if a path exists? Most kinds of backtracking type problems, 
also just as a general search in graphs/trees

- BFS: Finding the shortest path? Level-order traversals in trees, finding the 
shortest path between A and B in a graph of uniform weight.

- Cycle detection (linked list, array, etc)? Floyds method

- Finding missing/repeated numbers? Gauss summation formula or Bitwise operations


---
### Important points to remember:

- Sequential loops still result in O(n), no nested looping.

- 
```python
l = list(range(10))

# Nested loop only covers the subset of values
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        pass
    
# permutations like approach (start from 0)
for i in range(len(l)):
    for j in range(len(l)):
        pass

```

- Sliding window approach is very good. 2 points that you update within 
a while loop - linear time.
- When measuring *distance* between 2 pointers don't forget to +1 or -1 
depending on what you want to get
```
a b c d e
The number of chars between b (1) and e (4) is: right - left - 1, aka
4 - 1 - 1 = 2
The number of chars inclusive of the pointers: right - left + 1, aka
4 - 1 + 1 = 4
```
- How do I get rid of duplicates? Say (1, 2) and (2, 1) OR (1, 2, 3) 
and (2, 3, 1)? 
You need a place to store already seen/processed items with the ability to check
if an item exists in constant time --> dict or set.

- When an array is sorted, it is already a good indication using pointers might
be a good idea.
- 
- When working on trees, it appears there are usually 2 solutions: recursive and
iterative one. Iterative often comes down to using a queue.
- 

