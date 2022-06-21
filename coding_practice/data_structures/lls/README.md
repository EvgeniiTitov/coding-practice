
### The Two Runner Pointer Technique

Analogy: Say we have 2 runners that run along an infinitely 
long rope. One runner runs at 1 m/s, the other at 2 m/s --> hence
at any given point in time the fast runner will be 2 times 
ahead of the slow runner.

```
F = 2 m/s
S = 1 m/s
At any point in time, F = 2S

Slow at 2, the fast at 4
Slow at 8, the fast at 16, etc
```
--> To find the end of the first half of a LL, the same 
approach could be used: first pointer moves 1 node per iteration 
and the other 2 nodes per iteration. When the fast pointer 
reaches the end of the LL, the slow one is in the middle. If there's an
odd number of nodes, the middle node must be attached to the first half. 


----

### Reversing Linked List
The idea is we need to keep 3 references: previous, current, and next_node.
Current gets relinked to previous, previous gets moved to the right, current
becomes the next node. 
Once the end has been reached (last node), next_node is null, previous becomes
the new start of the LL, current becomes null so the loop ends. 
Return the reference to the start of the LL


```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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