from typing import Optional


"""
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a 
cycle in it.

There is a cycle in a linked list if there is some node in the list that can 
be reached again by continuously following the next pointer. Internally, pos 
is used to denote the index of the node that tail's next pointer is connected 
to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.


Floyd's Cycle Finding Algorithm:

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Mine, but its cheesy though as we mutate the nodes
    # T: O(N); S: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while True:
            # Reached the end of the LL
            if not head:
                break
            if hasattr(head, "seen"):
                return True
            head.seen = True
            head = head.next
        return False

    # T: O(N); S: O(N)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        while head:
            if head in visited_nodes:
                return True
            visited_nodes.add(head)
            head = head.next
        return False

    # T: O(N); S: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if head and not head.next:
            return False

        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        """

        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
