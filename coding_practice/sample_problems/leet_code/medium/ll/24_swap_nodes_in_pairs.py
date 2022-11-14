from typing import Optional

from coding_practice.utils import build_singly_ll_from_sequence


"""
Summary:
    Bloody hell its confusing one - the idea is simple, 3 references, you do
    some rewiring. Its important to correctly wire the prev reference otherwise
    it all mixes up
_______________________________________________________________________________

https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head. You
must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Edge cases
        if not head:
            return head
        elif head and not head.next:
            return head

        prev = dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            next = head.next
            head.next = next.next
            next.next = head
            prev.next = next
            head = head.next
            prev = next.next
        return dummy.next


def main():
    head = build_singly_ll_from_sequence((1, 2, 3, 4))
    head = Solution().swapPairs(head)
    while head:
        print(head)
        head = head.next


if __name__ == '__main__':
    main()
