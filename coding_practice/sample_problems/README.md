### How to approach solving problems:

- Carefully read the problem definition, there could be hints there
- Okay to start with brute force, then think how to optimise 
- Draw!

---

### Terms:

- Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.


- In mathematics, the lexicographic or lexicographical order (also known as 
lexical order, or dictionary order) is a generalization of the alphabetical 
order of the dictionaries to sequences of ordered symbols or, more generally, 
of elements of a totally ordered set. 
For example, using the natural order of the integers, the lexicographical 
ordering on the subsets of three elements of S = {1,2,3,4,5,6} is:
```
123 < 124 < 125 < 126 < 134 < 135 < 136 < 145 < 146 < 156 < 234 < 235 < 236 < 245 < 246 < 256 < 345 < 346 < 356 < 456
```

___

### Poorly solved problems / Not understood solutions:
- 14 Longest Common Prefix
- 53 Max subarray, dynamic solution
- 88 merge sorted arrays, O(1) solution
- 136 bits manipulation solution

---

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
### To remember:

<<<<<<< HEAD
- Checking if intervals overlap and meting them

```python
Interval = List[int]

def _check_if_overlap(
    interval_1: Interval, interval_2: Interval
) -> bool:
    start_1, end_1 = interval_1
    start_2, end_2 = interval_2
    if start_1 <= start_2:
        return end_1 >= start_2
    else:
        return end_2 >= start_1

def _merge(*intervals: Interval) -> Interval:
    starts = [interval[0] for interval in intervals]
    ends = [interval[1] for interval in intervals]
    return [min(starts), max(ends)]
```
=======
- Power set - all possible combinations of all possible lengths, from 0 to N.
>>>>>>> 9f6e3eaad221baaf7732f98e776fdf372e2c23bf

---

- Recursively processing 2D grid (DFS, BFS)

Remember you can check for out of bounds before or after the recursive call:

```python
# Here I check before
def numIslands(self, grid: List[List[str]]) -> int:

    def _search_islands(i: int, j: int) -> bool:
        if grid[i][j] == "0" or (i, j) in visited_coordinates:
            return False

        visited_coordinates.add((i, j))
        possible_directions = []
        if i > 0:
            possible_directions.append([i - 1, j])
        if j > 0:
            possible_directions.append([i, j - 1])
        if i < rows - 1:
            possible_directions.append([i + 1, j])
        if j < columns - 1:
            possible_directions.append([i, j + 1])

        for next_move in possible_directions:
            # If next move is the sea or was already visited (attempt to go
            # back from where we just came), skip
            if (
                    grid[next_move[0]][next_move[1]] == "0"
                    or tuple(next_move) in visited_coordinates
            ):
                continue
            _search_islands(*next_move)

        return True

    total_islands = 0
    visited_coordinates = set()
    rows = len(grid)
    columns = len(grid[0])
    for i in range(rows):
        for j in range(columns):
            found  = _search_islands(i, j)
            if found:
                total_islands += 1

    return total_islands

--- OR ---

#Here I check after (BFS)
def numIslands(self, grid: List[List[str]]) -> int:

    # Here we call first, then check if we're out of bounds. ^ you check
    # first
    def _perform_dfs(i: int, j: int):
        """
        Sets all visited island points from 1 to 0
        """
        # Check for out of bounds
        if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        _perform_dfs(i - 1, j)
        _perform_dfs(i + 1, j)
        _perform_dfs(i, j - 1)
        _perform_dfs(i, j + 1)

    total_islands = 0
    rows = len(grid)
    columns = len(grid[0])
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == "0":
                continue
            _perform_dfs(i, j)
            total_islands += 1
    return total_islands

--- OR even like this ---

@staticmethod
def are_valid_coords(i: int, j: int, grid_i: int, grid_j: int) -> bool:
    if i < 0 or j < 0 or i >= grid_i or j >= grid_j:
        return False
    return True

# In this approach we keep track of visited nodes by changing it from 1to0
def numIslands(self, grid: List[List[str]]) -> int:
    from queue import Queue

    next_moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    total_islands = 0
    rows = len(grid)
    columns = len(grid[0])
    for i_index in range(rows):
        for j_index in range(columns):
            if grid[i_index][j_index] == "0":
                continue

            total_islands += 1

            # Mark as visited and process all adjacent land (reminds ^
            # but not recursive
            queue = Queue()
            queue.put((i_index, j_index))
            grid[i_index][j_index] = "0"
            while queue.qsize():
                i, j = queue.get()
                for next_move in next_moves:
                    new_i, new_j = i + next_move[0], j + next_move[1]
                    if (
                            Solution.are_valid_coords(new_i, new_j, rows,
                                                      columns)
                            and grid[new_i][new_j] == "1"
                    ):
                        queue.put((new_i, new_j))
                        grid[new_i][new_j] = "0"

    return total_islands
```

---

- collections.Counter() 
Uses heap under the hood, so it could give you N most common items

```python
counter = Counter("cbbaaazzzz")
print(counter)
print(list(counter.elements()))  # All values (flat structure)

print(counter.most_common(2))  # Uses heap under the hood
counter.pop("z")
print(counter.most_common(2))

counter_list = Counter([1, 2, 3, 3, 3, 3])  # Works with tuples as well
print(counter_list.most_common(1))

d = {"one": 1, "two": 2, "three": 3}
print(Counter(d))

---
Counter({'z': 4, 'a': 3, 'b': 2, 'c': 1})
['c', 'b', 'b', 'a', 'a', 'a', 'z', 'z', 'z', 'z']

[('z', 4), ('a', 3)]
[('a', 3), ('b', 2)]

[(3, 4)]

Counter({'three': 3, 'two': 2, 'one': 1})
```

---

- Get key of the largest value in a dict

```python
d = {"A": 10, "B": 0, "C": 100}
largest_key = max(d, key=d.get)
OR
largest_key = max(d, key=lambda k: d.get(k))
```

---

- Two pointers approach to find longest, max, etc for a string/array

```
- Seems to be the best approach as it requries a single pass only

- You need a way to store state between the pointers
    - An array of size 128 for keeping track of ascii chars
    - A dict
    - Just a value
    
- You need to come up with logic to move the pointers based on the current state
    - Say when dealing with ascii chars, we keep moving left till there are no more repetitive chars
    - Or the number of random chars within the window cannot be covered by K 
      (allows to change N chars to anything else)
    
    - IMPORTANT: depending on the task every iter you could move just right, just
      left OR both! You could have inner WHILE trying to fix the state (ascii example)
```

---

- Iterating over string indices while slicing it. You iterate 0 to length (or whatever)
but when you slice you need to +1 to include the last character!

```python
s = "ABCDE"

length = len(s)

for i in range(length):
    print(i, s[i])

for i in range(length):
    print(s[0: i + 1])  # ! Up to but not included


0 A
1 B
2 C
3 D
4 E

A
AB
ABC
ABCD
ABCDE

```

---

- Backwards looping options

```python
l = [1, 2, 3, 4, 5, 6]

for i in range(len(l) - 1, -1, -1):
    print(f"Index {i}; Value {l[i]}")

for i in reversed(range(len(l))):
    print(f"Index {i}; Value {l[i]}")

'''
Index 5; Value 6
Index 4; Value 5
Index 3; Value 4
Index 2; Value 3
Index 1; Value 2
Index 0; Value 1
'''
```

---

- When inserting/deleting nodes in a BST it is important to a) reassign a subtree 
when modifying it and b) return root from recursive calls otherwise subtrees would be Nones
```python
def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    
    if root.val == val:
        return root
    
    if val > root.val:
        # insert into the right subtree
        root.right = self.insertIntoBST(root.right, val)  # !
    else:
        # insert into the left subtree
        root.left = self.insertIntoBST(root.left, val)  # !
    return root  # !
```

---

- Floyd's algorithm for finding cycles and entrance into them in LL:
```
Slow and fast runners. slow = slow.next; fast = fast.next.next; If there is a 
cycle they will meet, i.e. reference the same node -> slow == fast (intersection node),
which could then be used to find the entrance to the cycle.
Then pointer 1 starts at the beginning of the LL, pointer 2 at the intersection
and they both move with the same speed until they intersect - entrance.
```

---

- While iterating through a LL with a fast pointer jumping over 2 nodes instead of one,
its enough to check:

```python
while fast and fast.next:  # fast already checks if its None or not
    pass
```

---

- When given an array of N + 1 ints where each int is in the range [1, N] you
can straight away see the list could be turned into a LL to detect a cycle/duplicate
or whatever. Say:
```
[2, 6, 4, 1, 3, 1, 5]
New element is the index of the current element:
LL: 2 -> 4 -> 3 -> 1 -> 6 -> 5 -> 1 -> 6 -> 5 -> 1 -> CYCLE!

Could use the Floyd's algorithm now to detect the cycle
```

---

- When recursively working with trees, an action / modification could be done
either before or after the recursive call(s). Be careful:
```python
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
```

---

- When working with trees iteratively we usually place a node in a stack or a queue,
however reassinging the root variable itself within the loop is a viable approach 
as well (inserting into BST)
```python
    def insertIntoBST(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        head = root
        while True:
            if root.val == val:
                return
            elif val < root.val:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    return head
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    return head
```

---

- Whenever you want to sort something to get access to 1 or more smallest/largest
items consider using heap. Heapify is O(N) in place while pushing/popping is O(log N),
which is much better than sorting O(N log N)

---

- Fine to pop off elements from an array in a loop as long as you: a) keep track
of its length yourself OR b) recalculate its length len(arr) every iter to know
when to break off the WHILE loop

---

- Careful with a != b != c because `0 != 1 != 0` passes the condition -> be explicit
`a != b and a != c and b != c`

---

- Sequential loops still result in O(n), no nested looping.

---

- When slicing, going beyond is fine: l = [1,2]; l[:1000] won't result in error

---

- When reassigning a variable min, max are cleaner and more pythonic.
```
largest_sum = -math.inf
for _ in range(_):
    largest_sum = max(largest_sum, subarray_sum)
```
---

- Modifying original array in place: nums1[:] = out

---

- In python strings could be sorted! No need to explicitly cast list(str) first
```
print(sorted("awhrubgwhgrc"))
['a', 'b', 'c', 'g', 'g', 'h', 'h', 'r', 'r', 'u', 'w', 'w']
```

---

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

---

- When measuring *distance* between 2 pointers don't forget to +1 or -1 
depending on what you want to get
```
a b c d e
The number of chars between b (1) and e (4) is: right - left - 1, aka
4 - 1 - 1 = 2
The number of chars inclusive of the pointers: right - left + 1, aka
4 - 1 + 1 = 4
```
---

- How do I get rid of duplicates? Say (1, 2) and (2, 1) OR (1, 2, 3) 
and (2, 3, 1)? 
You need a place to store already seen/processed items with the ability to check
if an item exists in constant time --> dict or set.

---

- When an array is sorted, it is already a good indication using pointers might
be a good idea.

---

- When working on trees, it appears there are usually 2 solutions: recursive and
iterative one. Iterative often comes down to using a queue.

---

- When dealing with a palindrom str, if we verify 0 and len(str) - 1 are the same,
then we only care to check 1 to len(str) - 2, i.e racecar is a palindrom, we 
verify that first and last chars match, then we can forget about them and focus 
only on the aceca string, pretend the matched ones no longer exist. Etc.

---

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

---

- Boyer-Moore Voting Algorithm (169 majority element)

If we had some way of counting instances of the majority element as +1+1 and 
instances of any other element as -1−1, summing them would make it obvious 
that the majority element is indeed the majority element.
```python
def majorityElement(self, nums: List[int]) -> int:
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
```