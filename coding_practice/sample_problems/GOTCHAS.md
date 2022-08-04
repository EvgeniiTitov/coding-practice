### Tips / Tricks / To Remember:

#### The below does not include the brute force solutions (for the most part)

---

#### General (arrays, queues, stacks, sets, dicts, sliding window, 2 pointers, math, etc): 

- (1) Two sum: calculate compliment, keep track of their availability in a dict


- (20) Valid parenthesis: add opening to a stack, for closing pop off the stack and check if match


- (26) Remove duplicates from sorted: slow-fast runner, fast keep running right until 
nums[slow] != nums[fast], then you move slow + 1, nums[slow] = nums[fast]. All 
duplicates get skipped


- (35) Search insert position: BS, if item not found in the list, will be inserted at left pointer


- (66) Plus one: value (%) + carry over (//)


- (70) Climbing stairs: dynamic or D&C with memoization. Base case: current index > stairs? 
return 0 OR if on the final step return 1; Else: `return climb(curr_step + 1, nb_stairs) + 
climb(curr_step + 2, nb_stairs)`


- (88) Merging sorted arrays/LLs: pointers are at index 0, get values, find the min, add to the array out,
move the pointer of the array from which you got the smaller value - there might be more smaller
values. 


- (121) Best time buy sell stock: sliding window, left = 0, right = 1, while right < len(stocks),
calculate temp profit (sell - buy), if buy < sell: max_profit = (max_profit, temp); 
if buy > sell, left = right. Every iteration ! we move the right pointer + 1


- (125) Valid palindrom phrase: S: O(N) is to clean the str with .isalnum() and then 
str_cleaned == str_cleaned[::-1] OR for S(1) use to pointers: 0, len(str) - 1. If any
pointer is not .isalnum() skip it and continue. Iterate while left < right. If 
left_char.lower() != right_char.lower(): return False. 


- (136) Find single number: every number except for 1 appears twice. S: O(N) is to add/remove
items from a set. At the end set has 1 item. OR O(1) using bit manipulation


- (167) Two sum || (sorted): 2 pointers, move either left or right to match target. Same 
number cant be used twice -> while left < right


- (169) Majority element: find most popular item in a list. S: O(N) - defaultdict
to get how often each item appears. Then pick the most popular one. OR for S: O(1)
track a candidate and how often it appears. Iterate over numbers, if count == 0:
pick a candidate (candidate = num). Each iter: count += 1 if num == candidate else -1


- (202) Happy number: Use a set to keep track of seen number forms, if its != 1 and in seen,
then its not a happy number, there is a cycle. OR use the Floyd's cycle finding algo
using 2 runners: slow and fast! If either == 1 -> true, if slow == fast -> cycle -> false


- (242) Valid anangram: 2 strs as input. If length dont match -> False. Sort them and see 
if match


- (252) Meeting rooms: check if a person could attend all, iterate over meetings cur and cur + 1
and check if they overlap. 


- (344) Reverse a string: In place: s[:] = s[::-1] OR s.reverse() OR using 2 pointes:
left, right, while left < right: swap left and right chars, and move them towards
each other


- (346) Moving average from data stream: we care only about values within the window, anything
else should be discarded -> queue. The denominator is min(window_size, len(queue)) in
case queue has fewer items than the window size


- (415) Add strings: cannot convert to ints. ascii 0 is 48. 1 - 49, 2 - 50, ..., 9 - 57. Could 
get actual value by ord(number) - ascii_zero. Then, value + carry over stuff. After looping
dont forget to check if there is anything in carry_over variable


- (509) Fibo number: fibo(n) = fibo(n - 1) + fibo(n - 2); + Memoization


- (605) Planting flowers: no adjacent plants allowed: 1 0 0 0 1, could plant 1 in the middle.
Look at 3 items at once: i - 1, i, i + 1. If all 0s, change middle to 1. Keep moving right.
Add 0s as padding to avoid edge cases


- (680) Valid palindrom 2: 1 error allowed. 2 pointers approach, left, right. If dont match,
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

- (1047) Remove all adjacent duplicates in a str: Use a stack to drop letter there, 
for each new char check if the last in the stack, if equal, pop off the stack. If
stack is empty, just add a char and continue. Return "".join(stack)


- (1160) Find words formed by chars: for every word make a copy of available chars, and
as you iterate over the word chars remove the chars from the available chars. If
at some point a char you need is not present in the available chars, the word is 
not a good one


- (1304) Find N unique ints sum to 0: Symmetric around 0. If n is odd, add 0, else
i, -i for i in range(n // 2)


- (155) Min stack: stack is a list: List[Tuple[int, int]], that stores 2 things:
(val, curr_min). When adding a new item, check if the val < the curr min on the stack. If yes,
stack.append((val, val)) else stack.append((val, last_min)). Popping is safe. The min
is accessible at O(1) by self.stack[-1][1]


---


#### Linked List

- (21) Merge two sorted LLs: Dummy node for a new list. Them, keep looking till
one of the pointers (list1, list2) reaches the end, connect the remaining nodes
from the list which didn't reach the end. Return head.next() to skip the dummy 
node. When moving pointers, move the one that gave the smaller value. Don't forget
to move the head: head = head.next


- (141) LL cycle: Could use a set and put nodes there while iterating. If a node is
already in the set -> cycle! OR S: O(1) 2 pointers: 1 fast 1 slow. If they ever meet
-> cycle. OR a cheesy one is to dynamically add a .seen = True attribute to every
node and check it haha damn i love python


- (160) Intersection of 2 LLs: S: O(N) is to have a set, iterate over one list adding
all nodes to the set, then iterate over the second list checking if a node is in the 
set. OR S: O(1) is to calculate distance of each list (diff), then move the longer 
list's head diff nodes, now we're the same distance from the end for both lists, 
start iterating simultaneously checking if the references point to the same node:
if longer == shorter: return True


- (206) Reverse LL: we need 3 references: previous, current, current.next;
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

- (234) Palindrom LL: Dummy is to accumulate all the values, check values == values[::-1] OR
slow, fast runner. When fast reaches the end, the slow one is in the middle! Reverse the LL
starting from middle.next, start iterating simultaneously from the beginning and the reversed
middle checking if the values match

---

#### Trees

-

---


#### Graph

- (997) Town judge: indegree/outdegree of a vertex. Judge's outdegree is 0, 
whereas indegree is n - 1, where n is number of people. Use a set and a dict
to keep track of who trusts in general and how many trusts each person gets


- (1971) Find if path exists: BFS using a queue and a set of keep track of visited
vertices. Since looking for a path, put an entire path in the queue checking each time
if the last vertex == destination


---


#### Heap

- (1046) Last stone weight: get list of stone weights, keep smashing the heaviest stones,
until 1 left or all destroyed. Use heap to get 2 heaviest stoned, smash them, 
push to the heap if their sizes !=. Keep doing till there is just 1 or nothing 

-

---


#### Greedy / Divide and Conquer / Backtracking


-