from typing import Optional


"""
Summary: The proper one is to use 2 pointers, a dummy value to initialize the new
ll out, which will be skipped when returning and then using the pointers get
a pair of values from each LL. Move pointer which game smaller value, there could
be more smaller values.
_______________________________________________________________________________

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing 
together the nodes of the first two lists.

Return the head of the merged linked list.


Thoughts:
1. Solution 1 is simple. Collect all the values from both lists, merge, sort,
and then build a new LL out

2. Solution 2 allows to build the out LL on the fly. While we haven't reached
the end of both LLs, get 2 values (current LLs pointers), compare them, add
the smaller value to the LL out and move the pointer of the LL from which you
got the smaller value. We don't do anything with the larger value (no moving
the pointer of the other LL as there might be more smaller items/values coming
from the first LL).
Once one of the LL's reached the end, connect the other one to the end of the 
LL out as it will only have larger values!
On top of that, use the fake number as the first node in the LL out (so you
have an instance of LL out before you started iterating), when returning 
exclude this first number
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # My solution
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if not list1 and not list2:
            return None

        def _get_ll_values(ll: ListNode):
            values = []
            while ll:
                values.append(ll.val)
                ll = ll.next
            return values

        values_ll_1 = _get_ll_values(list1)
        values_ll_2 = _get_ll_values(list2)
        values_ll_1.extend(values_ll_2)
        # Lists are already sorted, this bit is ugly, can't achieve O(n)
        values_ll_1.sort()  # O(n log n)
        all_values = values_ll_1

        first = all_values.pop(0)
        ll_out = head = ListNode(first)
        for value in all_values:
            new_node = ListNode(value)
            head.next = new_node
            head = new_node
        return ll_out

    # My solution with help from Leetcode
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
