from typing import Optional


"""
Summary: Either using sets or Floyd on steroids:

Floyd the man:

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

_______________________________________________________________________________

https://leetcode.com/problems/linked-list-cycle-ii/

Given the head of a linked list, return the node where the cycle begins. 
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can 
be reached again by continuously following the next pointer. Internally, 
pos is used to denote the index of the node that tail's next pointer is 
connected to (0-indexed). It is -1 if there is no cycle. Note that pos is 
not passed as a parameter.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # T: O(N); S: O(N)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next

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

        # Phase 2 -
        p1 = intersection
        p2 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
