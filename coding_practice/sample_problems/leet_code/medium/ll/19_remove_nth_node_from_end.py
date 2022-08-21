from typing import Optional

from coding_practice.utils import (
    build_singly_ll_from_sequence,
    print_ll_values,
)


"""
Summary: The idea is to use 2 pointers. Move one N steps, and then move both 
of them until the one moved reaches the end of the list - that results in the
first one being on the node that needs deletion.
_______________________________________________________________________________

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list 
and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # T: O(N); S: O(1)
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
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


def main():
    ll = build_singly_ll_from_sequence(elements=(1, 2))
    print_ll_values(Solution().removeNthFromEnd(ll, 2))


if __name__ == "__main__":
    main()
