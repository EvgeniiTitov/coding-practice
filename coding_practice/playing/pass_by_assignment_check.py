import typing as t


"""
Clarifying how assignment works in python

When passing lists, dicts and custom objects to functions, they could be
modified inside the function and the changes would be seen everywhere (somewhat
pass by reference). Then, why the fuck below happens?!

ll_out = head = ListNode(values[0])  # Two values point to the same object

You built your LL, return the pointer to the first node. Then, we measure its
length by traversing the entire LL by passing reference to the first node to
the measure_ll_length function. What's important despite operating on the ref
directly (ll = ll.next) it doesn't seem to change the reference in main(). Why?
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_ll(values: t.Sequence[int]) -> t.Optional[ListNode]:
    if not len(values):
        return None
    ll_out = head = ListNode(values[0])  # Two vars refer to the same object
    for value in values[1:]:
        head.next = ListNode(value)
        head = head.next
    return ll_out


def measure_ll_length(ll: ListNode) -> int:
    length = 0
    while ll:
        length += 1
        ll = ll.next
    return length


def main():
    values = list(range(10))
    ll = build_ll(values)
    print("LL built")
    print("LL length is:", measure_ll_length(ll))
    print("LL's pointer after measuring its length is at:", ll.val)
    print(measure_ll_length(ll), measure_ll_length(ll))


if __name__ == "__main__":
    main()
