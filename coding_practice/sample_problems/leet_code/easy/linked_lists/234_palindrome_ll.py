from typing import Optional


'''
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome.

Time complexity O(n) as each node in LL is visited, writing to an arr is O(1)
Space complexity is O(n), we add N values to the array

To remember:
! Checking whether an array is polindrom is as simple as arr == arr[::-1]
'''


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
            left_subarray = values[:middle_i + 1]
            right_subarray = values[middle_i:]

        else:
            left_subarray = values[: length // 2]
            right_subarray = values[length // 2:]
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        def _reach_end_first_half(head: ListNode) -> ListNode:
            slow, fast = head, head
            while slow.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def _reverse_ll(head: ListNode) -> ListNode:
            previous = None
            current = head
            while current:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            return previous

        first_half_end = _reach_end_first_half(head)
        reversed_second_half_start = _reverse_ll(head)

        is_palindrom = True
        first_pointer = head
        second_pointer = reversed_second_half_start
        while is_palindrom and second_pointer:
            if first_pointer.val != second_pointer.val:
                is_palindrom = False
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        # Restore the correct order
        first_half_end.next = _reverse_ll(reversed_second_half_start)
        return is_palindrom
