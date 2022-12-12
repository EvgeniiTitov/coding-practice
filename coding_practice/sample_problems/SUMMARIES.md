## How to approach solving a problem?

- Understand well the problem at hand:
  - Whats given
  - Whats expected
  - What are the constraints (say, cant use builtin sort methods, etc)
  - Often examples provided DO NOT cover the entire space of what could be provided,
so think of more exampels (contain duplicates, contain no items etc)


- Start simple, dumb solution is fine (nested loops, sorting results to avoid duplicates in the final solution, etc)


- Estimate time and space complexity of the solution


- Come up with a new optimised solution:
  - Consider more efficient approach / algorithm
  - Better data structures


IMPORTANT:

- Solving the problem right sometimes is not necessary, if you think out load, explain what you're doing, 
how you think the problem could be solved, explain complexities, data structure tradeoffs etc
that might already be enough.

- When solving, think out loud - say you decide you want to use 2 pointers to solve your problem, do you 
start at one end and go right (sliding window), do you have two pointers at 0, len(arr) - 1? Think out loud,
say the options

- 


---

## General (arrays, queues, stacks, sets, dicts, sliding window, 2 pointers, math, etc): 


- `(1) Two sum:` calculate compliment, keep track of their availability in a dict.

Could be solved using pointers, sort, then left (0), right (len - 1), add them up. If < target,
move left, else move right. 

OR

Use a dict to keep track of numbers you've seen and their indices. Then, when you need a compliment,
check if its in the dict. Yes - use it, no - add the number you're itersating over. 

---

- `(20) Valid parenthesis:` add opening to a stack, for closing pop off the stack and check if match

---


- `(26) Remove duplicates from sorted:` slow-fast runner, fast keep running right until 
nums[slow] != nums[fast], then you move slow + 1, nums[slow] = nums[fast]. All 
duplicates get skipped

---

- `(35) Search insert position:` BS, if item not found in the list, will be inserted at left pointer

---

- `(66) Plus one:` value (%) + carry over (//)

---

- `(36) Valid Sudoku:` 9 x 9 board, partially filled, validate partially fixed nums make sense. Each
row must contain digits 1-9 no reps, same for the col, 9 3x3 boxes must contain to reps as well. 

Iterate over subboxes (for i in range(0, 9, 3): for j in range(0, 9, 3):)), get a box, then
validate each box: a) check its content values, then rows and cols that this box overlaps. To validate
nums just iterate over them, put in a set, check if a num exists there, then duplicate, not valid!
Could cache because the same box (9 items) overlaps the same 3 rows and 3 cols. No need to validate
the same row or col 3 times, do it once. 

---


- `(70) Climbing stairs:` D&C or top-down/bottom-up DP. Base case: current index > stairs? 
return 0 OR if on the final step return 1; Else: `return climb(curr_step + 1, nb_stairs) + 
climb(curr_step + 2, nb_stairs)`

---

- `(88) Merging sorted arrays/LLs:` pointers are at index 0, get values, find the min, add to the array out,
move the pointer of the array from which you got the smaller value - there might be more smaller
values. 

---

- `(121) Best time buy sell stock:` sliding window, left = 0, right = 1, while right < len(stocks),
calculate temp profit (sell - buy), if buy < sell: max_profit = (max_profit, temp); 
if buy > sell, left = right. Every iteration ! we move the right pointer + 1

---

- `(125) Valid palindrom phrase:` S: O(N) is to clean the str with .isalnum() and then 
str_cleaned == str_cleaned[::-1] OR for S(1) use to pointers: 0, len(str) - 1. If any
pointer is not .isalnum() skip it and continue. Iterate while left < right. If 
left_char.lower() != right_char.lower(): return False. 

---

- `(136) Find single number:` every number except for 1 appears twice. S: O(N) is to add/remove
items from a set. At the end set has 1 item. OR O(1) using bit manipulation

---

- (167) `Two sum || (sorted):` 2 pointers, move either left or right to match target. Same 
number cant be used twice -> while left < right

---

- `(169) Majority element:` find most popular item in a list. S: O(N) - defaultdict
to get how often each item appears. Then pick the most popular one. OR for S: O(1)
track a candidate and how often it appears. Iterate over numbers, if count == 0:
pick a candidate (candidate = num). Each iter: count += 1 if num == candidate else -1

---

- `(202) Happy number:` Use a set to keep track of seen number forms, if its != 1 and in seen,
then its not a happy number, there is a cycle. OR use the Floyd's cycle finding algo
using 2 runners: slow and fast! If either == 1 -> true, if slow == fast -> cycle -> false

---

- `(242) Valid anangram:` 2 strs as input. If length dont match -> False. Sort them and see 
if match

---

- `(252) Meeting rooms:` check if a person could attend all, iterate over meetings cur and cur + 1
and check if they overlap. 

---

- `(344) Reverse a string:` In place: s[:] = s[::-1] OR s.reverse() OR using 2 pointes:
left, right, while left < right: swap left and right chars, and move them towards
each other

---

- `(346) Moving average from data stream:` we care only about values within the window, anything
else should be discarded -> queue. The denominator is min(window_size, len(queue)) in
case queue has fewer items than the window size

---

- `(415) Add strings:` cannot convert to ints. ascii 0 is 48. 1 - 49, 2 - 50, ..., 9 - 57. Could 
get actual value by ord(number) - ascii_zero. Then, value + carry over stuff. After looping
dont forget to check if there is anything in carry_over variable

---

- `(509) Fibo number:` fibo(n) = fibo(n - 1) + fibo(n - 2); + Memoization

---

- `(605) Planting flowers:` no adjacent plants allowed: 1 0 0 0 1, could plant 1 in the middle.
Look at 3 items at once: i - 1, i, i + 1. If all 0s, change middle to 1. Keep moving right.
Add 0s as padding to avoid edge cases

---

- `(680) Valid palindrom 2:` 1 error allowed. 2 pointers approach, left, right. If dont match,
call a func to check if 2 strings are palindroms skipping left and right chars

```python
def validPalindrome(self, s: str) -> bool:
    def _check_if_palindrom(s: str, left: int, right: int) -> bool:
        if not s or len(s) == 1:
            return True
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        # If the chars mismatch, we need to check whether deletion of
        # either of them results in a palindrom anyway
        if s[left] != s[right]:
            return _check_if_palindrom(
                s, left + 1, right
            ) or _check_if_palindrom(s, left, right - 1)
        left += 1
        right -= 1
    return True
```
---

- `(1047) Remove all adjacent duplicates in a str:` Use a stack to drop letter there, 
for each new char check if the last in the stack, if equal, pop off the stack. If
stack is empty, just add a char and continue. Return "".join(stack)

---

- `(1160) Find words formed by chars:` for every word make a copy of available chars, and
as you iterate over the word chars remove the chars from the available chars. If
at some point a char you need is not present in the available chars, the word is 
not a good one

---

- `(1304) Find N unique ints sum to 0:` Symmetric around 0. If n is odd, add 0, else
i, -i for i in range(n // 2)

---

- `(155) Min stack:` stack is a list: List[Tuple[int, int]], that stores 2 things:
(val, curr_min). When adding a new item, check if the val < the curr min on the stack. If yes,
stack.append((val, val)) else stack.append((val, last_min)). Popping is safe. The min
is accessible at O(1) by self.stack[-1][1]

---

- `(15) Three sum:` Sort numbers, start iterating over the numbers, fix one number - the
one you are standing on, and solve the two sum problem. When solving the 2 sum problem,
you consider only those numbers to the right from the one you fixed. As soon as the number
you iterate over is > 0, break, anything to the right > 0, so cant reach sum = 0.

---

- `(33) Search rotated sorted array:` [4,5,6,7,0,1,2], and a target to find in O(log N) time,
need to use BS. First, find the rotation index: left, right = 0, len(arr) - 1. Using BS,
check middle value and middle + 1 value. If middle > middle + 1, found the drop, rotation
index is middle + 1. Else, we need to find if we are on the left or right of the drop, 
check middle value against the left. Move either right or left pointer, repeat. Once found
the pivot index, you know whether the target to the left or right of the drop, using BS
find it within the subarray. 

---

- `(49) Group anangrams:` Iterate over strs, each could be sorted and used as a key in 
the defaultdict. Then, return the values (lists of anangrams)


---

- `(50) Pow X n:` The trick is to avoid multiplying the number N times. Could be done in
O(log N) using some math properties.

The dum solution is to check if n is 0, then the res 1. Then, you iterate N times multiplying
num by itself. If n (power) is < 0, return 1 / res, else return res.

---


- `(53) Max subarray:` contiguous subarray with max sum. max(subarray) is O(N), so avoid
doing that. Brute force would be to use 2 loops and process all combinations.  
Fix an i, then iterate over j in range (i, len(arr)) and keep track of a temp subarray sum 
(for each i), adding every new j and checking the max subarray by = 
max(max_subarray, temp_subarray) for each j. There is a better solution i dont understand

---


- `(56) Merge intervals:` sort, keep them on the stack. For each new interval, does it overlap
the prev on the stack? Yes - pop, merge, append. Else, just append. 


---

- `(57) Insert interval:` already sorted in ascending order, insert a new one merging with
any overlapping ones. Single pass is possible: for each interval, if its end < new_interval
start, just append to a list out. If interval start > new_interval end, no overlap, just
add to list out. If there is an overlap, increase the new_interval: new_interval_start = 
min(interval_start, new_interval[0]), new_interval_end = max(...); Pay close attention to when
insert the new_interval, must be done before the intervals that are greater than it.


---

- `(74) Search 2D matrix:` its sorted, so BS is possible. left = 0, right = n_rows * items_per_row + 1,
then just have a helped function to translate a value in 1D to 2D: 
```python
def _get_item_at_index(
    self, matrix: List[List[int]], items_per_row: int, index: int
) -> int:
    return matrix[index // items_per_row][index % items_per_row]
```


---

- `(150) Eval reverse polish notation:` Evaluate ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

Use a stack. If not an operator, add to the stack, if an operator - pop 2 items, using lambda 
function perform the action (`{"+": lambda a,b: a + b}`), push to the stack. 


---

- `(238) Product of an array except self:` Given array if ints nums, return array where res[i] equals
to product of all nums in the input array except nums[i]. 

Optimised brute force is possible. 2 loops for i
and j, for i == j we skip the number (except self), else we calculate the product for the 
number i, and save it. Also, have a cache where you keep products for numbers as duplicated
are possible. 

OR a single pass approach: for each num in nums, we could calculate its 
products to the left and to the right (sequential FOR loops still O(N)). Then, we iterate one last time
adding product_left * product_right


- `(875) Koko eating bananas:` Linear probing is fine but slow, better pick slowest speed = 1 
and fastest = max(piles), and then using BS find the optimal speed. Important to do BS 
right, if time spent eating bananas < h (allowed hours), move the right pointer to
the middle index (not middle - 1) - this is out result, but maybe there is a better one so, 
keep iterating.

---

- `(75) Sort colors:` Array of nums (0 - red, 1 - white, 2- blue). Sort it so that items of the 
same color are adjacent. 

Cheating solution would be to .sort() or implement a sorting algorithm
manually (selection sort, quick sort). Proper solution is heavy, Dijkstra's Dutch National Flag Problem


---

- `(128) Longest consucutive sequence:` Given unsorted array of ints, return len of the longest
consecutive elements sequence. 

Duplicates do not contribute to the len of consec seq -> turn into set. 
Iterate through set items, looking for local mins (num - 1 not in set). Then for each min loop up
while num + 1 is in set while keeping track of the len. 

---

- `(435) Non overlapping intervals:` Return how many intervals you need to remove, so that the result
array has no overlapping intervals.

Sort the intervals based on the start, pick the first one as
prev_interval and start processing intervals `for interval in intervals[1:]`, for each new interval
you want to know if it overlaps the prev one. If not, set prev_interval to current, no overlap.
If they do, increment the counter AND set prev_interval to current IF the prev_one completely 
encompasses the current one (from both ends), we update the prev_one to the shorter one (current) as this long
one is ignored (beneficial to set to shorter one, fewer chances it will overlap with something else)

---

- `(438) Find all anangrams in a string:` Given two strings S and P, return array of start indices of
P's anangrams in S. len(S) > len(P), there could be multiple P anangrams in S.

Brute force - use dicts to compare strings P and subset of chars in S. Iterate over S comparing
substrings from left to right (not till the last index, until len(S) - len(P) + 1). The problem here
you regenerate string state (dict) every iteration while moving just one step to the right. 

Optimised would be to update the state after going right instead of regenerating it. Use pointers
to keep track of the state (dict), when moving left pointer, if a value for a char becomes 0,
delete from the dict. When you only start, generate state from 0 to len(p) - 1 (missing the last char) so inside your while
loop at the beginning you move the right pointer one step right. Iterate until the right pointer
reaches the end of S.


---

- `(678) Valid parethesis string:` Given string containing ), ( and *, return true if valid.

Brute force approach using divide and conquer could work, replace each * with ( or ) or "", once
the base case is reached (pointer reached the end of the string), validate the result using a stack. 

The smart solution is turn first turn all * into ( and check if ( + * >= right brace, that means
some * could be ''. Then we do the opposity turning all * into ) and checking ) + * >= (. --> We know
some of them could bne turned into '' and overall the string could be made valid. 

---

- `(981) Time based KV store: Design time-based KV store that can store multiple values for the same key
at different timestamps.` 

Use a dict where value is your key, value is a list. When adding items, add a (timestamp, value). 
Timestamp always grows, so when you need to get an item for a certain timestamp, use binary search to find your value. 

--- 

- `(739 Dialy tempretures:` Given array of tempretures, return an array where answer[i] is the number
of days you have to wait after the i'th day to get a warmer temp. 0 if not possible.

Create a result array of length = tempretures array. Create a stack, put there the first item and its index,
Then start iterating over tempretures and their indices (enumerate). Check if current temp < prev one, if 
yes push to the stack. Else, start checking current temp against what you have on the stack. If its warmer,
then fill the corresponding index in the result (output) array (subtract index of curr temp - what was on the stack),
its the diff - how many days we had to wait for a warmer temp

---

- `(853) Car fleet:` N cars going along the same road to the destination N miles away. Given 2 arrays: car
positions and speeds. Cars cant overtake, they form fleets going bumber to bumber if faster catches up a 
slower one. How many car fleets reach the end?

Zip positions and speeds, sort by their positions. Calculate time to reach the finish for each car. 
Starting from the closest to the finish, iterate through the cars + using a stack. If time to the finish
of the current car < the one on the stack, they will form a fleet, else the current car will form a new 
fleet (add to the stack). Then return the stack len. 

---

- `(11) Container with most water:` given array of ints (heights). Each point represents a line
`(i, 0) and (i, height[i])`. Find two lines that create the largest container (area).

Brute force - just all combinations, for each calculate the area, keep the largest.

Smart one - two pointers (0, len(arr) - 1). Calculate area between them, keep the max. Now, you 
need to move one/both pointers, which one? Move the SHORTEST one towards the other one in hopes we
find a taller line. We dont want to move both, we dont want divide in conquer by moving both separately.
The trick is to move one, the shortest one. 

---

















## Linked List

- `(21) Merge two sorted LLs:` Dummy node for a new list. Them, keep looking till
one of the pointers (list1, list2) reaches the end, connect the remaining nodes
from the list which didn't reach the end. Return head.next() to skip the dummy 
node. When moving pointers, move the one that gave the smaller value. Don't forget
to move the head: head = head.next

---

- `(141) LL cycle:` Could use a set and put nodes there while iterating. If a node is
already in the set -> cycle! OR S: O(1) 2 pointers: 1 fast 1 slow. If they ever meet
-> cycle. OR a cheesy one is to dynamically add a .seen = True attribute to every
node and check it haha damn i love python

---

- `(160) Intersection of 2 LLs:` S: O(N) is to have a set, iterate over one list adding
all nodes to the set, then iterate over the second list checking if a node is in the 
set. OR S: O(1) is to calculate distance of each list (diff), then move the longer 
list's head diff nodes, now we're the same distance from the end for both lists, 
start iterating simultaneously checking if the references point to the same node:
if longer == shorter: return True

---

- `(206) Reverse LL:` we need 3 references: previous, current, current.next;
```
previous = None
current = head
while current:
    next_node = current.next
    current.next = previous
    previous = current  # When reaching the end, previous is the start
    current = next_node  # When reaching the end, current becomes null
return previous
```

---

- `(234) Palindrom LL:` Dummy is to accumulate all the values, check values == values[::-1] OR
slow, fast runner. When fast reaches the end, the slow one is in the middle! Reverse the LL
starting from middle.next, start iterating simultaneously from the beginning and the reversed
middle checking if the values match

---

- `(19) Removing n'th node:` 2 pointers, move the first one n steps. Then, start moving
both of them simultaneously until the first one reaches the end. The second one now
points to the node to delete (prev.next = current.next)

---

- `(142) Cycle 2, return the node where the cycle begins:` Floyd algorithm: 2 runners slow
and fast. If there is a cycle, at some point slow == fast. if not, the fast reaches the end ->
no cycle. If there is, then the phase 2 is to have 2 pointers: one starts from the intersection,
the other from the start, move them simultaneously at the same speed. The node where they
intersect - the entrance to the cycle.

---

- `(287) Find the duplicate number:` The list has N + 1 ints, each [1, n]. Its a LL under the hood.
Floyds algorithm: slow = fast = nums[0]. Then, search for the intersection (slow == fast). Once
found, find the entrance by using 2 pointers (from start and intersection)

---

- `(3) Longest substring with no repeating characters:`

Brute force way is to check all combinations of substrings,
```python
for i in range(len(s)):
    for j in range(i, len(s)):
        sub_string = s[i: j + 1]
```
and then for each check if it has repeated chars (len(string) == len(set(string))) keeping track
of the longest one without repeated chars.

Proper way is two use 2 pointers and represent a state between them - sliding window. Array of
size 128 could be used (ASCII), then you process the string until the right pointer reaches the end.
At the beginning of each loop, you check what the right pointer points to (char), update the state. 
Since we move only right, then a duplicate could be introduced (the right char), so we check if moving
to the right introduced a duplicate, if it did we move the left pointer until the problem is fixed
(internal while loop - `while state[char_right_ascii_value]) > 1: move left, update the state`. Once
duplicates removed, keep moving the right pointer updating the longest substring without repetitions.







---

## Trees

- (94) Binary T inorder traversal: For each node pick values in order: left, current, right. 
Pre order would be: current, left, right and Post order: left, right, current

---

- (100) Same tree: given 2 nodes of different trees q and p. If p and not q or q and not p,
then not the same. If both are Nones, true. If values are different, false. For each node
check left subtree whether its the same, them right. If both true, return true. 
OR do the same iteratively using a queue putting corresponding nodes there (p, q).

---

- (101) Symmetric tree: given a node check if its a mirror of itself. We must traverse
left and right subtrees simultaneously, so the recursive f gets 2 nodes (root, root) initially
and then we compare the values AND whether left.right matches right.left AND left.left 
matches right.right. OR could be done iteratively, take 2 items from the queue at a time,
two corresponding nodes (root, root) initially

---

- (104) Max depth of binary tree: if not root: return 0. Else, check left and right depths
and return 1 + max(left_depth, right_depth). OR solve iteratively, using a queue and putting
a node with its depth level: (1, root) initially, and keeping track of the max depth by:
max_depth = max(max_depth, curr_depth), where curr_depth comes from the queue alongside the
corresponding node.

---

- (110) Balanced binary tree: left and right subtrees height diff <= 1. If a subtree is
imbalanced, the whole tree is imbalanced. For each node, check left, right subtrees: 
height and whether they're balanced. If height diff > 1: return False, else the 
subtrees are balanced: return True, 1 + max(left_depth, right_depth)

---

- (226) Invert binary tree: exchange left and right subtrees. root.left = right, root.right = left

---

- (235) Lowest common ancestor (LCA): given a tree root and 2 nodes p and q, find the LCA. Compare
values of p and q with the root val. If both >, recursive call for the right subtree, if <
for the left. If case one val is > the root and the other <, found LCA OR iteratively:

```python
p_val = p.val
q_val = q.val
node = root
while node:
    node_val = node.val
    if node_val > p_val and node_val > q_val:
        node = node.left
    elif node_val < p_val and node_val < q_val:
        node = node.right
    else:
        return node
```

---

- (450) Delete node BST: if value > root.val: root.right = delete_node(root.right, value),
if value < root.val: root.left = delete_node(root.left, value). If root.val == value and
root doesnt have kids, just root = None, return root. Else, we need to find a value to
replace it with (successor or predecessor). If root.right, find the successor and then
recussively delete the successor (since we took its value): root.val = find_successor(root), 
root.right = delete_node(root.right, root.val); Same for the left - predecessor if replacing
with a predecessor instead of a successor

---

- (543) Diameter of binary tree: global variable that every recuraive call compares to or
passing diameter as an argument. Diameter is left_diameter + right_diameter, essentially
depth of a subtree. Doesn't necessarily have to go through the root.

---

- (572) Subtree of another tree: slow but clear - iterate over tree BFS using a queue. For 
each node run a helper function for the current node and the subtree. Check if its the same
tree (problem 100)

---

- (700) Search in BST: if root.val < value, search left subtree, else right subtree. If 
not root, return None - haven't found the value

---

- (701) Insert into BST: guaranteed the value is not in the BST. Iterate the tree, if 
value < root.value, if root.left call recursively, else root.left = TreeNode(val). Same
if value >. OR iteratively

---

- (938) Range sum of BST: given root and 2 values, sum up all nodes within the range. 
global var sum_, for current node: current = root.val; if low <= current <= high: sum_ 
+= current. Then, for recursive call if current > low, makes sense to go left, if
current < high, makes sense to consider the right subtree.

















---

## Graph

- (997) Town judge: indegree/outdegree of a vertex. Judge's outdegree is 0, 
whereas indegree is n - 1, where n is number of people. Use a set and a dict
to keep track of who trusts in general and how many trusts each person gets

---

- (1971) Find if path exists: BFS using a queue and a set of keep track of visited
vertices. Since looking for a path, put an entire path in the queue checking each time
if the last vertex == destination















---

## Heap

- (1046) Last stone weight: get list of stone weights, keep smashing the heaviest stones,
until 1 left or all destroyed. Use heap to get 2 heaviest stoned, smash them, 
push to the heap if their sizes !=. Keep doing till there is just 1 or nothing 

- (355) OOP, separation of concerns. Users could be treated as nodes in a graph.
Each node keep track of the nodes it connects to (followers -> followees). Use
heap to keep track of the most recent tweets for each user. Tweets could be represented
as a class, just define __ lt() __ method for the heap to sort them. + Tweet id
is not a timestamp to sort on, use Tweet class attriute to generate IDs fo each
new tweet.
















---

## Greedy / Divide and Conquer / Backtracking


-