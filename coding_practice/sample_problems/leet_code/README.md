#### Poorly solved problems / Not understood solutions:
- 14 Longest Common Prefix
- 53 Max subarray, dynamic solution
- 88 merge sorted arrays, O(1) solution
- 

---

#### General information:

"Most questions fall into some category of DP/memoization, DFS/BFS, two pointer,
sort/binary search, or Hash table/counting occurrences in my experience"

- DFS: Finding out if a path exists? Most kinds of backtracking type problems, 
also just as a general search in graphs/trees

- BFS: Finding the shortest path? Level-order traversals in trees, finding the 
shortest path between A and B in a graph of uniform weight.

- Cycle detection (linked list, array, etc)? Floyds method

- Finding missing/repeated numbers? Gauss summation formula or Bitwise operations


---
#### To remember:

- Sequential loops still result in O(n), no nested looping.

- When slicing, going beyond is fine: l = [1,2]; l[:1000] won't result in error

- When reassigning a variable min, max are cleaner and more pythonic.
```python
largest_sum = -math.inf
for _ in range(_):
    largest_sum = max(largest_sum, subarray_sum)
```
- Modifying original array in place: nums1[:] = out

- Some looping:
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

- When working on trees, it appears there are usually 2 solutions: recursive and
iterative one. Iterative often comes down to using a queue.

- When dealing with a palindrom str, if we verify 0 and len(str) - 1 are the same,
then we only care to check 1 to len(str) - 2, i.e racecar is a palindrom, we 
verify that first and last chars match, then we can forget about them and focus 
only on the aceca string, pretend the matched ones no longer exist. Etc.

- When dealing with pointers and going from left and right towards the middle,
opting to left <= right instead of left < right will ensure the middle character
is considered for odd sequences.
```python
def _check_if_palindrom(s: str, left: int, right: int) -> bool:
    if not s or len(s) == 1:
        return True
    while left <= right:  # !
        print("Checking:", s[left], s[right])
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
# Passing racecar string will result in:
# Checking: r r
# Checking: a a
# Checking: c c
# Checking: e e
# FOR left <= right, OR in 
# Checking: r r
# Checking: a a
# Checking: c c
# FOR left < right

```