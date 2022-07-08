from typing import Optional


"""
https://leetcode.com/problems/reverse-linked-list/
Given the head of a singly linked list, reverse the list, and return the reversed list.

The idea is we need to keep 3 references: previous, current, and next_node.
Current gets relinked to previous, previous gets moved to the right, current
becomes the next node. 
Once the end has been reached (last node), next_node is null, previous becomes
the new start of the LL, current becomes null so the loop ends. 
Return the reference to the start of the LL

"""

# Definition for singly-linked list.
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
