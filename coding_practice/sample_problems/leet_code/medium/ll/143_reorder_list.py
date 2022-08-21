from typing import Optional, Tuple

from coding_practice.utils import (
    build_singly_ll_from_sequence,
    print_ll_values
)


"""
Summary: 
_______________________________________________________________________________

https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves 
may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # My solution. T: O(N); S: O(N)
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or (head and not head.next):
            return head

        # Single pass, collect (index, node) pairs
        nodes = {}
        counter = 0
        current = head
        while current:
            nodes[counter] = current
            counter += 1
            current = current.next

        # Start assembling the new LL mixing nodes from start and end
        left, right = 0, counter - 1
        dummy_head = ListNode(-1)
        current = dummy_head
        while left <= right:
            left_node = nodes.get(left)
            right_node = nodes.get(right)

            # Unwire the nodes from their old references
            left_node.next = None
            right_node.next = None

            if left == right:
                current.next = left_node
                current = current.next
            else:
                current.next = left_node
                current = current.next
                current.next = right_node
                current = current.next

            left += 1
            right -= 1

        # Modify the head, operating in-place
        head = dummy_head.next

    # Constant space solution. T: O(N); S: O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:

        def _find_middle_node(head: ListNode) -> Tuple[ListNode, ListNode]:
            slow = fast = head
            prev_slow = None
            while fast and fast.next:
                prev_slow = slow
                slow = slow.next
                fast = fast.next.next
            return prev_slow, slow

        def _reverse_ll(head: ListNode) -> ListNode:
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        if not head or (head and not head.next):
            return head

        current = head
        before_middle, middle = _find_middle_node(current)
        reversed_start = _reverse_ll(middle)

        # Connect the first half to the reversed one
        before_middle.next = reversed_start

        print_ll_values(current)
        print_ll_values(reversed_start)

        # Merge the two lists
        # TODO: COMPLETE ME


def main():
    # sequence = [1, 2, 3, 4, 5]
    # ll = build_singly_ll_from_sequence(sequence)
    #
    # print_ll_values(ll, sep=" -> ")
    #
    # Solution().reorderList(head=ll)
    #
    # print()
    # print_ll_values(ll, sep=" -> ")

    # ---
    sequence = [1, 2, 3, 4, 5]
    ll = build_singly_ll_from_sequence(sequence)
    Solution().reorderList(head=ll)


if __name__ == '__main__':
    main()
