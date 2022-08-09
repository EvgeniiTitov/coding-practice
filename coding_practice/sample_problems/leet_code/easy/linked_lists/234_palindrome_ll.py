from typing import Optional


"""
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome.

Time complexity O(n) as each node in LL is visited, writing to an arr is O(1)
Space complexity is O(n), we add N values to the array

To remember:
! Checking whether an array is polindrom is as simple as arr == arr[::-1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Mine head on solution ( T complexity: O(n), S complexity: O(n) )
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def _collect_ll_values(head: ListNode) -> list:
            # Takes a lot of space, could use a gen?
            values = []
            while head:
                values.append(head.val)
                head = head.next
            return values

        values = _collect_ll_values(head)
        length = len(values)
        # That's dumb haha values == values[::-1]
        if length == 1:
            return True
        elif length % 2:
            middle_i = length // 2
            left_subarray = values[: middle_i + 1]
            right_subarray = values[middle_i:]

        else:
            left_subarray = values[: length // 2]
            right_subarray = values[length // 2 :]
        right_subarray.reverse()

        return left_subarray == right_subarray

    # TODO: Wtf - just do: values == values[::-1] !
    # Head on improved ( T complexity: O(n), S complexity: O(n) )
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def _collect_ll_values(head: ListNode) -> list:
            # Takes a lot of space, could use a gen?
            values = []
            while head:
                values.append(head.val)
                head = head.next
            return values

        values = _collect_ll_values(head)
        return values == values[::-1]

    # TODO: Throws a NoneType error, find the error
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
