import typing as t


"""
Add two numbers - https://github.com/qiyuangong/leetcode/blob/master/python/002_Add_Two_Numbers.py

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

2 --> 4 --> 3
5 --> 6 --> 4
=
7 --> 0 --> 8

This shit is confusing.
"""


class ListNode:
    def __init__(self, value: t.Any, next=None):
        self.value = value
        self.next = next


class Solution:

    # def addTwoNumbers(
    #     self,
    #     l1: t.Optional[ListNode],
    #     l2: t.Optional[ListNode]
    # ) -> t.Optional[ListNode]:
    #     result = ListNode(0)
    #     result_tail = result
    #     carry = 0
    #
    #     while l1 or l2 or carry:
    #         val1 = (l1.val if l1 else 0)
    #         val2 = (l2.val if l2 else 0)
    #         carry, out = divmod(val1 + val2 + carry, 10)
    #
    #         result_tail.next = ListNode(out)
    #         result_tail = result_tail.next
    #
    #         l1 = (l1.next if l1 else None)
    #         l2 = (l2.next if l2 else None)
    #
    #     return result.next

    def addTwoNumbers(
        self, l1: t.Optional[ListNode], l2: t.Optional[ListNode]
    ) -> t.Optional[ListNode]:
        number_1, number_2 = [], []

        while l1:
            value = l1.val
            number_1.append(str(value))
            l1 = l1.next
        while l2:
            value = l2.val
            number_2.append(str(value))
            l2 = l2.next

        number_1 = "".join(number_1)
        number_2 = "".join(number_2)
        number_1 = int(number_1[::-1])
        number_2 = int(number_2[::-1])
        result = list(map(int, str(number_1 + number_2)[::-1]))

        first = result.pop(0)
        ll_out = head = ListNode(first)
        for char in result:
            new_node = ListNode(char)
            head.next = new_node
            head = new_node
        return ll_out


def iterate_over_ll(ll):
    """
    Example how to print the values
    """
    values = []
    while True:
        values.append(ll.val)
        if ll.next:
            ll = ll.next
        else:
            break
    print("Values:", values)
