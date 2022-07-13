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