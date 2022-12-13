## Terms:

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
- Optimal substructure - a problem is said to have optimal substructure if an 
optimal solution could be constructed from optimal solutions of its subproblems. 
Say, Fib(N) = Fib(N - 1) + Fib(N - 2)


- Overlapping subproblems - a problem is said to have overlapping subproblems 
if the problem can be broken down into subproblems which are reused several 
times or a recursive algorithm for the problem solves the same subproblem over 
and over rather than generating new subproblems - good example is calculating Fibonacci

- A subset - any combination of elements from a set. A set with N elements, 
subsets: 2 ^ N. Example: {1, 5} --> 2 ^ 2 = 4 --> {}, {1}, {5}, {1, 5}. A set 
with 3 elements has 2 ^ 3 = 8 subsets, etc.

- Power set - all possible combinations of all possible lengths, from 0 to N.

![alt text](../../images/combinations_vs_permutations.png?raw=true)

^ 5 letters available (A, B, C, D, E)

- Permutations and Combinations are the ways in which objects from a set may be
selected to form subsets.

  - Combinations - order doesn't matter: {A, C, B} and {A, B, C} are the same 
  combination.

  - Permutations - ordered combination, the total length must be equal to the
    original input
  
---

## General information:

"Most questions fall into some category of DP/memoization, DFS/BFS, two pointer,
sort/binary search, or Hash table/counting occurrences etc."

- DFS: Finding out if a path exists? Most kinds of backtracking type problems, 
also just as a general search in graphs/trees

- BFS: Finding the shortest path? Level-order traversals in trees, finding the 
shortest path between A and B in a graph of uniform weight.

- Cycle detection (linked list, array, etc)? Floyds method

- Finding missing/repeated numbers? Gauss summation formula or Bitwise operations


---

## To remember:


- #### Avoid generating duplicated permutations

Your typical approach to generating permutations could result in duplicates if
input array contains. Lazy way is to aggregate permutations as tuples in a set that would
get rid of any duplicates. The smart way, instead, suggests to keep track of numbers available when
generating a new permutation. If a number's count == 0, it means this number has 
already been used in the permutation, so we cant use it again

```python
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    from collections import defaultdict

    def _generate_unique_permutations(
        num_counts: dict,
        curr_permutation: List[int],
        permutations: List[List[int]]
    ) -> None:
        if len(curr_permutation) == len(nums):
            permutations.append(curr_permutation[:])
            return

        for num, count in num_counts.items():
            if count > 0:
                curr_permutation.append(num)
                num_counts[num] -= 1
                _generate_unique_permutations(
                    num_counts, curr_permutation, permutations
                )
                num_counts[num] += 1
                curr_permutation.pop()

    permutations = []
    num_counts = defaultdict(int)  # OR collections.Counter()
    for num in nums:
        num_counts[num] += 1

    _generate_unique_permutations(num_counts, [], permutations)
    return permutations
```

---

- #### Skipping adjacent duplicates

You might need something like this when doing backtracking generating combinations
and you need to avoid duplicated combinations so you skip adjacent numbers 
```python
l = [1, 2, 3, 3, 3, 4, 5, 5, 5, 6]

# Picks all unique numbers looking -1 backwards
for i in range(len(l)):    
    if i > 0 and l[i] == l[i - 1]:
        continue
    print(l[i])

# Picks all unique numbers looking +1 forward
for i in range(len(l)):
    if i != len(l) - 1 and l[i] == l[i + 1]:
        continue
    print(l[i])
```

---

- #### Generating unique combinations

When dealing with such a problem, there're usually two ways:

    - Proper one: algorithm doesn't generate duplicates 
    - Cheesy one: use a data structure that filters them out with a simpler algorithm that generateds dups

When implementing both, SORT the input array, then you could use a set
to accumulate combinations as tuples (for a cheesy solution) or skip adjacent duplicates
when solving it properly.

Proper solution:
```python
def _generate_combinations(
    curr_index: int,
    curr_combination: List[int],
    remaining: int,
    combinations: List[List[int]]
) -> None:
    # Base case
    if remaining == 0:  # Reached the target
        combinations.append(curr_combination.copy())
        return

    for i in range(curr_index, length):

        # ! Skip adjacent duplicates, while addressing the edge case
        if i > curr_index and candidates[i] == candidates[i - 1]:
            continue

        num = candidates[i]

        # ! Optimization: To the right only bigger numbers, sorted
        if remaining - num < 0:
            break

        curr_combination.append(num)
        _generate_combinations(
            curr_index=i + 1,
            curr_combination=curr_combination,
            remaining=remaining - num,
            combinations=combinations
        )
        curr_combination.pop()
```

---

- #### Backtracking - solution space probing logic 

It is common when solving a backtracking problem to use a loop to iterate over
all possible cases. But sometimes it is not required, we need to prune those 
solutions that are incorrect as we generate combinations instead of generating all
of them and then validating them at the end. 

An example is generating valid parentheses. A dummy way is to generate all combinations
and then keep only the validated ones. The better way is to avoid generating invalid 
ones entirely

```python
def generateParenthesis(self, n: int) -> List[str]:

    def _generate_solutions(
        curr_solution: List[str],
        open: int,
        close: int,
        solutions: List[str]
    ) -> None:
        if len(curr_solution) == nb_parentheses:
            solutions.append("".join(curr_solution))
            return

        if open < n:
            curr_solution.append("(")
            _generate_solutions(curr_solution, open + 1, close, solutions)
            curr_solution.pop()

        if close < open:
            curr_solution.append(")")
            _generate_solutions(curr_solution, open, close + 1, solutions)
            curr_solution.pop()

    if n == 0:
        return []
    elif n == 1:
        return ["()"]

    nb_parentheses = n * 2
    solutions = []
    _generate_solutions([], 0, 0, solutions)
    return solutions
```

---

- #### Using pointers to keep track of state and while loop to solve a problem

When solving a problem, which involves keep track of a state between the pointers,
before you enter the loop and define the initial state it is often convenient to leave out 
an item so that at the beginning of the while loop you could straight away do some updates
instead of dealing with an edge case (we've just started).

Example - finding anangrams from one string in the other

```python
def findAnagrams(self, s: str, p: str) -> List[int]:
    from collections import defaultdict

    def _get_chars_count(string: str) -> dict:
        char_counts = defaultdict(int)
        for char in string:  # O(N)
            char_counts[char] += 1
        return char_counts

    indices = []
    p_counts = _get_chars_count(p)
    s_subset_counts = _get_chars_count(s[: len(p) - 1])  # LEFT OUT LAST CHAR

    left, right = 0, len(p) - 1
    while right < len(s):
        s_subset_counts[s[right]] += 1  # ADDED THE CHAR

        if p_counts == s_subset_counts:
            indices.append(left)

        s_subset_counts[s[left]] -= 1
        if s_subset_counts[s[left]] == 0:
            del s_subset_counts[s[left]]

        left += 1
        right += 1

    return indices
```

---

- #### `while curr and curr.next`:

Having just `while curr` is NOT enough when you're also checking for the next
reference. When it reaches None, it throws an error saying None has no .next
attribute -> `while curr and curr.next:`

```python
original = build_singly_ll_from_sequence((1, 2, 3, 4, 5))

# 1) Reaching an actual end of LL (beyond the last node)
head = original
while head:
    print(head)
    head = head.next
print("Last:", head)  # None

# 2) Reaching the last node
head = original
while head and head.next:
    print(head)
    head = head.next
print("Last:", head)  # 5
```

---

- #### String's .split() works with multiple spaces as well

```python
s = "   hello                 world "
print(s.split())  # ['hello', 'world']
```
---

- #### Manual list reversing by hand

Works for both odd and even arrays

```python
def reverse_array(array: list[T]) -> None:
    left, right = 0, len(array) - 1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
```


---

- #### Picking graph algorithm to solve a problem at hand

When dealing wih graph questions, pay attention to:
```
1. Directed / Undirected
2. Weighted / Unweighted
3. Cyclic / Acyclic
```
^ will define the algorithm(s) to consider to solve the problem at hand. 
Usually:
```
- Shortest path problem for unweighted G - BFS
- Shortest path weighted (positive) graph - Dijkstra
- Shortest path weighted (negative -> potential cycles) graph - Bellman Ford
```

On top of that, there're intereating variations of problems such as find min
path within K stops. We can't just use D or B because they minimise the cost,
not the number of vertices. Further modifications are needed, or use BFS while
keeping track of the cost for each branch. 

---

- #### Slicing out a single char from a string. Good for D&C etc

```python
s = 'abcde'
for i in range(len(s)):
    print(s[:i] + s[i + 1:])
```

---

- #### When accumulating a set of numbers to add up to a target sometimes its beneficial to go down (reaching 0 while subtracking what you picked)
Instead of having a variable, say, summed_numbers where you keep track of the current sum.

---

- #### Keeping track of intermediate result/state (variable VS list/set)

Often when dealing with recursion etc, I accumulate results in a list/set and then
pass it to the next call. However, often it is not necessary, just calculate a value.
Say, when reaching a target value, there is no point accumulating numbers in a list
and then passing it, just sum them up, unless you need to know the combination 
(numbers that made up the sum)

```python
def findTargetSumWays(self, nums: List[int], target: int) -> int:

    def build_expression(
        nums: List[int],
        curr_index: int,
        curr_sum: int,
        target: int
    ) -> None:
        nonlocal evaluated_to_target

        if curr_index >= len(nums):
            if curr_sum == target:
                evaluated_to_target += 1
            return

        build_expression(
            nums, curr_index + 1, curr_sum + nums[curr_index], target
        )
        build_expression(
            nums, curr_index + 1, curr_sum - nums[curr_index], target
        )

    evaluated_to_target = 0
    build_expression(nums, 0, 0, target)
    return evaluated_to_target
```
In my first iteration of ^, I accumulated the signs + and - in a list and then
evaluated the expression, which is not as clean as just passing a single number - 
current sum.

Another examples (overlapping intervals), I would straight away want to have a stack
where I would put intervals and then compare the last one on the stack with the one
I am iterating over / processing now. BUT,  it is unnecessary, we are not asked to return
len / intervals, we need to know how many we need to remove, so just keep track of the
LAST interval:

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    if not len(intervals):
        return 0

    intervals.sort(key=lambda interval: interval[0])
    intervals_removed = 0
    prev_interval = intervals[0]
    for curr_interval in intervals[1:]:
        # If there's an overlap (case 2), we don't update the prev, we just
        # increment the counter. If case 3, ignore the longer one, prev
        # is the current one (shorter)
        if prev_interval[1] > curr_interval[0]:
            if prev_interval[1] > curr_interval[1]:  # Case 3 ^
                prev_interval = curr_interval
            intervals_removed += 1
        else:
            prev_interval = curr_interval

    return intervals_removed
```

---

- #### FOR loops (linear time) does not always mean left --> right or right --> left passes.

Consider this example - find the longest consecutive sequence in the array. We
turn nums into a set to eliminate duplicates AND allow constant time lookups. Then,
we iterate over nums and search for starts of ascending sequences - start num wouldnt
have num - 1 in the set. For each start, we check how long the ascending sequence is!
SO, we iterate through nums but not left to right, we find a certain value we're
interesated in and then *go up*. 

```python
# T: O(N); S: O(N)
def longestConsecutive(self, nums: List[int]) -> int:
    nums = set(nums)  # O(N)
    longest_global = 0

    for num in nums:
        # Found a new potential start for the ascending sequence
        if num - 1 not in nums:
            current_num = num
            longest_current = 1

            while current_num + 1 in nums:
                current_num += 1
                longest_current += 1

            longest_global = max(longest_global, longest_current)

    return longest_global
```

---

- #### Possible palindrom centers

1. When it comes to finding all palindrome substrings, there could be 2N - 1 centres,
say, you have a string: `aaa`, there're 5 possible centers (between letters as well)

2. Left and right either coincide or not (odd / even). //2 because i ranges [0, 2N - 1]

Finding all palindrome substrings:
```python
def countSubstrings(self, s: str) -> int:

    def _expand_around_centre(centre: int) -> int:
        counter = 0

        left = centre // 2
        right = left + centre % 2
        while left >= 0 and right <= length - 1 and s[left] == s[right]:
            counter += 1
            left -= 1
            right += 1
        return counter

    length = len(s)
    if length == 1:
        return 1

    counter = 0
    for i in range(2 * length - 1):
        counter += _expand_around_centre(i)

    return counter
```

---

- #### Passing a copy of the list VS original value
```
l = [1]
def pass_me_a_list(input_l):
    print(input_l is l)
    
l2 = l
l3 = l + [2]
l2.append(2)
pass_me_a_list(l2)
True
pass_me_a_list(l3)
False
```

```list + [...] creates a copy!```

Ways to copy:
```python
original_l = [1, 2]
l_1 = original_l  
# Proper copies
l_2 = original_l.copy()
l_3 = original_l[:]
l_4 = original_l[::]
l_5 = list(original_l)

original_l.append(3)  # Affects l_1 as its reference to the same list in memory

l_6 = original_l + [4]  # Creates a copy and adds 4 to it: [1, 2, 3, 4]
```
---

- #### Find Binary Tree paths (using a param to keep track of different paths)

Given a root, find all root-to-leaf paths.

Notice how we keep track of paths using a function parameter. Each recursive
call results in a different path! Strings are immutable simple objects, so 
passing them to functions results in copies.

```python
def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

    def _find_paths(root: TreeNode, curr_path: str):
        if curr_path:
            curr_path += f"->{root.val}"
        else:
            curr_path = f"{root.val}"

        # If reached the leaf node, save the constructed path
        if not root.left and not root.right:
            paths.append(curr_path)

        if root.left:
            _find_paths(root.left, curr_path)
        if root.right:
            _find_paths(root.right, curr_path)

    if not root:
        return [""]
    elif root and not root.left and not root.right:
        return [str(root.val)]

    paths = []
    _find_paths(root, "")

    return paths
```

---

- #### DP (1D)

If a problem satisfies both Optimal Substructure and Overlapping Subproblems
properties, it could be solved using DP.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _Top-down with memoization:_

We start top to bottom, breaking down the problem into smaller subproblems till we
reach the simplest possible subproblems that we know how to solve. Involves a
bunch of recursive calls. 

In general, we need the following:

- Base case: when to stop recursive calls (out of bounds, ran out of capacity, etc)
- Logic to perform recursive calls (probing the solution space) and do something with their results (add, max, min, compare etc.)
- Cache (passed as a parameter or a use decorator)

^ This heavily reminds dealing with trees when you have bases cases + calling logic.

Examples:
```python
def climbStairs(self, n: int) -> int:
    def _cache(func):
        cache = {}
        def wrapper(n: int, stairs: int) -> int:
            if n in cache:
                return cache[n]
            result = func(n, stairs)
            cache[n] = result
            return result

        return wrapper

    @_cache
    def _climb_stairs(current_step: int, stairs: int) -> int:
        if current_step > stairs:
            return 0
        elif current_step == stairs:
            return 1
        return (
                _climb_stairs(current_step + 1, stairs) +
                _climb_stairs(current_step + 2, stairs)
        )

    return _climb_stairs(0, n)
```
Here we could start either from first (0) or second (1) step

```python
# Top-down DP
def minCostClimbingStairs(self, cost: List[int]) -> int:

    def _cache(func):
        _cache = {}
        def wrapper(num: int, *args, **kwargs):
            if num not in _cache:
                _cache[num] = func(num, *args, **kwargs)
            return _cache[num]
        return wrapper

    @_cache
    def _climb_stairs(step_index: int, cost: List[int]) -> int:
        if step_index >= len(cost):
            return 0

        option1 = _climb_stairs(step_index + 1, cost)
        option2 = _climb_stairs(step_index + 2, cost)

        return cost[step_index] + min(option1, option2)


    if len(cost) == 1:
        return cost[0]

    option1 = _climb_stairs(0, cost)
    option2 = _climb_stairs(1, cost)

    return min(option1, option2)
```
Example of a cache that gets passed in
```python
def rob(self, nums: List[int]) -> int:

    Cache = MutableMapping[int, int]

    def _rob_houses(
        house_index: int, houses: List[int], cache: Cache
    ) -> int:
        if house_index >= len(houses):
            return 0

        if house_index in cache:
            return cache[house_index]

        rob_current = (
                houses[house_index] +
                _rob_houses(house_index + 2, houses, cache)
        )
        rob_next = _rob_houses(house_index + 1, houses, cache)

        max_steal = max(rob_current, rob_next)
        cache[house_index] = max_steal

        return max_steal

    return _rob_houses(0, nums, {})
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _Bottom-up with tabulation:_

Once a problem's solved top-down, we could try to reformulate the solution to
solve the subproblems first (bottom-up). 

In general you need:

- A way to store subproblems results (array, table, etc)
- Knowing base cases: simplest possible problems. Often its okay to go out of bounds.
- Filling the array right-to-left or left-to-right depending on the base cases
- When filling the array, often you use data from both the temp array and input data

Examples:
```python
def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    
    l = [0] * (n + 1)
    # If you draw you notice that to climb 1st there is only 1 way, 2nd 2 ways
    l[1] = 1
    l[2] = 2
    for i in range(3, len(l)):
        l[i] = l[i - 1] + l[i - 2]
    
    return l[n]
```
```python
def minCostClimbingStairs(self, cost: List[int]) -> int:

    min_cost = [0] * (len(cost) + 1)

    for i in range(2, len(cost) + 1):
        take_one_step = min_cost[i - 1] + cost[i - 1]
        take_two_steps = min_cost[i - 2] + cost[i - 2]
        min_cost[i] = min(take_one_step, take_two_steps)

    return min_cost[-1]
```
```python
def rob(self, nums: List[int]) -> int:
    length = len(nums)
    robbed_amounts = [0] * (length + 1)

    robbed_amounts[-2] = nums[-1]
    for i in range(length - 2, -1, -1):
        robbed_amounts[i] = max(
            robbed_amounts[i + 1],
            nums[i] + robbed_amounts[i + 2]
        )

    return robbed_amounts[0]
```

---

- #### DP (2D)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _Top-down with memoization:_

Unique paths
```python
def uniquePaths(self, m: int, n: int) -> int:

    def _cache(func):
        _cache = {}
        def wrapper(m: int, n: int, i: int, j: int) -> int:
            if (i, j) not in _cache:
                _cache[(i, j)] = func(m, n, i, j)
            return _cache[(i, j)]
        return wrapper

    @_cache
    def _find_paths(m: int, n: int, i: int, j: int) -> int:
        # Base cases
        # 1. Out of bounds
        if i >= m or j >= n:
            return 0

        # 2. Reached the end
        if i == m - 1 and j == n - 1:
            return 1

        path1 = _find_paths(m, n, i + 1, j)
        path2 = _find_paths(m, n, i, j + 1)

        return path1 + path2

    return _find_paths(m, n, 0, 0)
```

Paths to reach last cell within given cost (needs cache)
```python
Matrix = t.List[t.List[int]]


def find_paths(
    matrix: Matrix, cost: int, i: int = 0, j: int = 0
) -> t.Union[int, float]:
    # Base cases

    # 1. Out of bounds
    rows = len(matrix)
    cols = len(matrix[0])
    if i >= rows or j >= cols:
        return 0

    # Ran out of cost
    remaining_cost = cost - matrix[i][j]
    if remaining_cost < 0:
        return 0

    # Reached the last cell
    if i == rows - 1 and j == cols - 1:
        return 1 if remaining_cost == 0 else 0

    path1 = find_paths(matrix, remaining_cost, i + 1, j)
    path2 = find_paths(matrix, remaining_cost, i, j + 1)

    return path1 + path2
```

Min cost reach last cell (needs cache)
```python
def find_min_cost_path(matrix: Matrix, i: int, j: int) -> t.Union[int, float]:
    rows = len(matrix)
    cols = len(matrix[0])
    # Out of bounds
    if i >= rows or j >= cols:
        return float("inf")
    # Reached the last cell
    if i == rows - 1 and j == cols - 1:
        return matrix[i][j]

    path1 = find_min_cost_path(matrix, i + 1, j)
    path2 = find_min_cost_path(matrix, i, j + 1)

    return matrix[i][j] + min(path1, path2)
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _Bottom-up with tabulation_:

Unique paths - since we can go just down and right, the first row and col are
just 1s. Then, we could come up with logic to populate other grid cells
```python
def uniquePaths(self, m: int, n: int) -> int:
    grid = [[1 for _ in range(n)] for _ in range(m)]

    for row in range(1, m):
        for col in range(1, n):
            grid[row][col] = grid[row - 1][col] + grid[row][col - 1]

    return grid[-1][-1]
```

---

- #### 2D grid traversals

-  When it comes to solving 2D cell traversal graph problems quite often it is
a good idea to reverse/flip the problem, which makes it easier to solve:

   - Instead of flowing from the mountains into the ocean (edges), lets start from
   the edges and see where it could get us

   - Instead of finding all surrounded regions by picking a 0 on the grid and checking
   if you could get to a border from there, let's pick all 0s on the edges and then
   traverse from them into the grid. By doing so you process only a subset of 
   coordinates (edges that are 0) instead of all coordinates (all 0s on the grid)

    This ^ allows to process only a subset of coordinates rather then all of them
  and is often quicker.


- To keep track of visited/processed cells you could:

   - Have a set to drop visited/processed coords there and then check before/after
   recursively/iteratively going to the next coord if its been already processed - 
   O(N) space complexity

   - Change grid values in place to another char. Then, you could change them back to
   to the original value if you don't need to return anything and working with the
   passed grid - O(1) space complexity


- Check if the next coordinate you want to go to satisfies your condition before
making the call rather than straight away in the recursive call (out of bounds, 
cell value is what we want etc) - reduces overhead associated with unnecessary 
function calls.

---

- #### Finding array rotation (wrapping)

Say we have an array `[3,4,5,6,7,8,9,0,1,2]`, we need to know the pivot index:

```python
def search(self, nums: List[int], target: int) -> int:

    def _find_pivot_index() -> int:
        left, right = 0, length - 1

        # No rotation, proper ascending array
        if nums[left] < nums[right]:
            return 0

        while left <= right:
            middle = (left + right) // 2
            middle_val = nums[middle]
            next_val = nums[middle + 1]
            if middle_val > next_val:
                return middle + 1
            else:
                # We could be left or right of the *drop*, identify where
                if middle_val < nums[left]:
                    right = middle - 1
                else:
                    left = middle + 1
    ...
```

---

- #### Binary Search

When it comes to BS, we do not always want to do it in its standard way:
```python
def binary_search(array: list[int], target: int) -> bool:
    left, right = 0, len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return True
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return False
```
Sometimes, we could use one of the pointers as the *result*, i.e. we will return
it. We find a solution, one of the pointers holds it, but then we also want to check
just in case we find a better one. We could also try to maximize (as with Koko's banana eating speed) 
or minimise the result, which I GUESS affects which pointer acts as a result.

Koko eating bananas:
```python
def minEatingSpeed(piles: List[int], h: int) -> int:
    import math

    left, right = 1, max(piles)
    while left < right:
        mid_speed = (left + right) // 2
        time_spent = 0
        for pile in piles:
            time_spent += math.ceil(pile / mid_speed)

        if time_spent <= h:
            right = mid_speed
        else:
            left = mid_speed + 1

    return right
```
If speed is fast enough, lets move the right pointer to the middle one (not middle - 1), and
keep iterating in case we find a slightly better speed. It is also CRUCIAL that left < right and not
<=

---

- #### Checking if intervals overlap and meting them

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

---

- #### Recursively processing 2D grid (DFS, BFS)

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

- #### collections.Counter() 
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

- #### Get key of the largest value in a dict

```python
d = {"A": 10, "B": 0, "C": 100}
largest_key = max(d, key=d.get)
OR
largest_key = max(d, key=lambda k: d.get(k))
```

---

- #### Two pointers approach to find longest, max, etc for a string/array

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

- #### Iterating over string indices while slicing it. 

You iterate 0 to length (or whatever) but when you slice you need to +1 to include the last character!

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

- #### Backwards looping options

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

- #### When inserting/deleting nodes in a BST 

it is important to a) reassign a subtree when modifying it and b) return root from recursive calls otherwise subtrees would be Nones
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

- #### Floyd's algorithm for finding cycles and entrance into them in LL:
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

- When recursively working with trees, graphs etc, an action / modification could be done
either before or after the recursive call(s). Be careful:
```python
 def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
     # Base case  
     if not root:
         return None
     
     # Recursive call (solution space)
     left = self.invertTree(root.left)
     right = self.invertTree(root.right)
     
     # Logic
     root.left = right
     root.right = left
     return root
```

When doing topological sort, we first need to reach the leaf nodes before we add them
to the stack:

```python
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