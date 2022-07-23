import typing as t


__all__ = ["build_singly_ll_from_sequence", "print_ll_values"]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"ListNode: value {self.val}"


def build_singly_ll_from_sequence(
    elements: t.Sequence[t.Any]
) -> t.Optional[ListNode]:
    if not len(elements):
        return

    head = out = ListNode(elements[0])
    for element in elements[1:]:
        head.next = ListNode(element)
        head = head.next

    return out


def print_ll_values(head: ListNode) -> None:
    while head:
        print(head.val, end=" ")
        head = head.next
