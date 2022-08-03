- ### Fast slow runner (Tortoise and Hare)

Analogy: Say we have 2 runners that run along an infinitely 
long rope. One runner runs at 1 m/s, the other at 2 m/s --> hence
at any given point in time the fast runner will be 2 times 
ahead of the slow runner.

```
F = 2 m/s
S = 1 m/s
At any point in time, F = 2 S

Slow at 2, the fast at 4
Slow at 8, the fast at 16, etc
```

1. Slow runner moves one step at a time, the fast on N steps (usually 2). Say, to 
find the middle element of a LL initialize 2 runners and itirate until the fast
one reaches the end --> the slow one is in the middle. If there's an
odd number of nodes, the middle node must be attached to the first half. 

2. They don't need to run at different speeds all the time. Say, you need to 
find the Nth element from the end in a sinple pass. To do so, set 1 pointer at
the start of the LL, the other N elements ahead. Start moving them at the same
speed until the one ahead reaches None --> The one behind reached the Nth
element from the end

3. Floyds cycle detection algorithm:

```
Phase 1:
Here, we initialize two pointers - the fast hare and the slow tortoise. 
Then, until hare can no longer advance, we increment tortoise once and hare 
twice. If, after advancing them, hare and tortoise point to the same node, 
we return it. Otherwise, we continue. If the while loop terminates without 
returning a node, then the list is acyclic, and we return null to indicate as much.

Phase 2:
Given that phase 1 finds an intersection, phase 2 proceeds to find the node 
that is the entrance to the cycle. To do so, we initialize two more pointers: 
ptr1, which points to the head of the list, and ptr2, which points to the 
intersection. Then, we advance each of them by 1 until they meet; the node 
where they meet is the entrance to the cycle, so we return it.
```

---

- ### Detecting a cycle ^

```python
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None

    def _find_intersection() -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

    # Phase 1 - find intersection if any
    intersection = _find_intersection()
    if not intersection:
        return

    # Phase 2 - find entrance to the cycle
    p1 = intersection
    p2 = head
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1
```

---

- ### Reversing Linked List
The idea is we need to keep 3 references: previous, current, and next_node.
Current gets relinked to previous, previous gets moved to the right, current
becomes the next node. 
Once the end has been reached (last node), next_node is null, previous becomes
the new start of the LL, current becomes null so the loop ends. 
Return the reference to the start of the LL


```python
class Solution:

    # T Complexity O(n), S complexity O(1) - we don't accumulate anything
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        previous = None
        current = head
        while current:
            next_node = current.next
            current.next = previous
            previous = current  # When reaching the end, previous is the start
            current = next_node  # When reaching the end, current becomes null
        return previous

# OR IF OPERATING IN PLACE
def reverse(self) -> None:
    if not self.head:
        return
    node = self.head.next
    self.head.next = None
    while node:
        next_node = node.next
        node.next = self.head
        self.head = node
        node = next_node

# TODO: Study how to do it recursively
```
---

- ### Iterating over a list

1. When imitating a fast runner who jumps over a node every iteration be careful
with while loop's condition as None has no attribute .next

```python
def build_ll(elements: list[t.Any]) -> Node:
    first = elements.pop(0)
    head = current = Node(first)
    for element in elements:
        current.next = Node(element)
        current = current.next
    return head


def iterate_every_element(head: Node) -> None:
    while head:
        print(head.value, end=" ")
        head = head.next


def iterate_every_second_element(head: Node) -> None:
    while head and head.next:  # ! IMPORTANT to check head is not None
        print(head.value, end=" ")
        head = head.next.next


def main():
    elements = list(range(1, 11))
    head = build_ll(elements)
    iterate_every_element(head)  # 1 2 3 4 5 6 7 8 9 10
    print()
    iterate_every_second_element(head)  # 1 3 5 7 9
```

2. Or when you need to reach the end (the last node without going into Nulls)

```python
current = self.head
while current.next:
    current = current.next
```
^ Now current is the last node, not None, we could, say, extend it with another
LL

---

- ### Merge LLs

The idea is to move the pointer the of list from which the smaller value came, there
could be more smaller ones
```python
def mergeTwoLists(
    self, list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if not list1:
        return list2
    if not list2:
        return list1
    if not list1 and not list2:
        return None

    ll_out = head = ListNode(-1)  # !
    while list1 and list2:
        value_list1 = list1.val
        value_list2 = list2.val
        if value_list1 < value_list2:
            head.next = ListNode(value_list1)
            list1 = list1.next
        else:
            head.next = ListNode(value_list2)
            list2 = list2.next
        head = head.next

    head.next = list1 if not list2 else list2
    return ll_out.next
```

---

- ### Find intersection

LLs might be of different length, so we need to know the diff in lengths. Then, 
move the longer point diff steps. Start iterating at the same time checking if 
the pointers point to the same object OR more memory hungry ones

```python
def getIntersectionNode(
    self, headA: ListNode, headB: ListNode
) -> Optional[ListNode]:
    head_a, head_b = headA, headB
    seen_nodes = set()

    while head_a:
        seen_nodes.add(head_a)
        head_a = head_a.next

    while head_b:
        if head_b in seen_nodes:
            return head_b
        head_b = head_b.next
    return None
```

OR

```python
def getIntersectionNode(
    self, headA: ListNode, headB: ListNode
) -> Optional[ListNode]:
    def _calculate_ll_length(head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def _set_ll_pointer_to_position(head: ListNode, pos: int) -> ListNode:
        for _ in range(pos):
            head = head.next
        return head

    head_a, head_b = headA, headB
    a_ll_length = _calculate_ll_length(head_a)
    b_ll_length = _calculate_ll_length(head_b)
    diff = abs(a_ll_length - b_ll_length)  # Diff in size between two LLs

    if a_ll_length > b_ll_length:
        shorter, longer = head_b, head_a
    else:
        shorter, longer = head_a, head_b

    longer = _set_ll_pointer_to_position(longer, diff)

    while longer and shorter:
        if longer == shorter:  # ! We don't care about .val but actual obj
            return longer
        longer = longer.next
        shorter = shorter.next

    return None
```

--- 

- ### Check if palindrome

Proper in place solution requires reversing the second half OR more memory hungry
is to just accumulate all values in a list and check if its == list[::-1]

```python
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    def _collect_ll_values(head: ListNode) -> list:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values

    values = _collect_ll_values(head)
    return values == values[::-1]
```

OR

```python
def isPalindrome(self, head: ListNode) -> bool:
    if head is None:
        return True

    # Find the end of first half and reverse second half.
    first_half_end = self.end_of_first_half(head)
    second_half_start = self.reverse_list(first_half_end.next)

    # Check whether or not there's a palindrome.
    result = True
    first_position = head
    second_position = second_half_start
    while result and second_position is not None:
        if first_position.val != second_position.val:
            result = False
        first_position = first_position.next
        second_position = second_position.next

    # Restore the list and return the result.
    first_half_end.next = self.reverse_list(second_half_start)
    return result    

def end_of_first_half(self, head):
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow

def reverse_list(self, head):
    previous = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous
```

--- 

- ### Removing nth node

The idea is to use 2 pointers. Move one of them N steps. Then, start moving both 
of them until the one moved reaches the end of the list - that results in the
first one being on the node that needs deletion. The one we move could straight
away land on null, meaning the current already points to the node to delete. Say,
in a ll like [1, 2],  n = 2

```python
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return

        def _reach_nth_node(head: ListNode, n: int) -> ListNode:
            for _ in range(n):
                head = head.next
            return head

        nth_node = _reach_nth_node(head, n)
        if not nth_node:
            return head.next

        current = head
        prev = None
        while nth_node:
            nth_node = nth_node.next
            prev = current
            current = current.next

        prev.next = current.next
        return head
```

---

- ### Dummy head and inserting at the beginning

Say, we have a Bucket class that we use to implement a Hash Set. It is a nice trick to:

- Use a dummy head to avoid some edge cases
- Insert at the beginning of the LL instead of the end because the order doesn't matter

```python
class Node:
    def __init__(
        self, value: t.Any, next_node: t.Optional["Node"] = None
    ) -> None:
        self.value = value
        self.next = next_node


class Bucket:
    # Acts as a Facade hiding the underlying details

    def __init__(self) -> None:
        self.head = Node(0)  # Pseudo head

    def insert(self, value: t.Any) -> None:
        if self.exists(value):
            return
        # Append new item to the beginning
        new_node = Node(value, next_node=self.head.next)
        self.head.next = new_node

    def delete(self, value: t.Any) -> None:
        previous = self.head
        current = self.head.next
        while current:
            if current.value == value:
                previous.next = current.next
            previous = current
            current = current.next

    def exists(self, value: t.Any) -> bool:
        current = self.head.next
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
```