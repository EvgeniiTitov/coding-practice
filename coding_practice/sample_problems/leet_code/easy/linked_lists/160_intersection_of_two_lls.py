from typing import Optional


'''
https://leetcode.com/problems/intersection-of-two-linked-lists/


------------------------------------------------------------------------------
Summary / Insights:
When dealing with LL' nodes, we don't always care about the data it stores and 
where it refers. We could also operate on the reference to the node and check 
if 1+ LLs holds references to the same node.
------------------------------------------------------------------------------


Given the heads of two singly linked-lists headA and headB, return the node at 
which the two lists intersect. If the two linked lists have no intersection at 
all, return null.

The test cases are generated such that there are no cycles anywhere in the 
entire linked structure.

Note that the linked lists must retain their original structure after the 
function returns.

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # Brute force.
    # The trick is we look for the same reference to a Node instead of a value
    def getIntersectionNode(
        self,
        headA: ListNode,
        headB: ListNode
    ) -> Optional[ListNode]:
        head_a, head_b = headA, headB
        while head_a:
            head_b_copy = head_b
            while head_b_copy:
                if head_b_copy == head_a:  # Pointers point to the same node!
                    return head_b_copy
                head_b_copy = head_b_copy.next
            head_a = head_a.next
        return None

    # Mine optimized, linear time and space complexities.
    def getIntersectionNode(
        self,
        headA: ListNode,
        headB: ListNode
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

    # Mine further space complexity optimization
    def getIntersectionNode(
        self,
        headA: ListNode,
        headB: ListNode
    ) -> Optional[ListNode]:

        def _calculate_ll_length(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        def _set_ll_pointer_to_position(head: ListNode, pos: int) -> ListNode:
            for i in range(pos):
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
