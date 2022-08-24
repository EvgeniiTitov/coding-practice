import typing as t


# TODO: Partition (182)
# TODO: Sum linked lists (183)
# TODO: Intersection (184)



"""
1. Remove duplicates from an unsorted LL

2. Return Kth to last (return Kth node) / Remove Nth node

3. Partition

4. Sum linked lists

5. Intersection
"""


class Node:
    def __init__(
        self,
        value: t.Any,
        next: t.Optional["Node"] = None,
        prev: t.Optional["Node"] = None
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f"< Node: value {self.value} >"


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value: t.Any) -> None:
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def __iter__(self) -> t.Iterator[Node]:
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self) -> str:
        values = [str(node.value) for node in self]
        return f"LinkedList of size {self.size}: {' -> '.join(values)}"

    def __len__(self) -> int:
        return self.size


# ---------------- 1. Remove duplicates from an unsorted LL -------------------

# T: O(N): S: O(N)
def remove_duplicates(ll: LinkedList) -> LinkedList:
    if not ll.head:
        return ll

    current = ll.head
    visited = set()
    while current:
        visited.add(current.value)
        if current.next and current.next.value in visited:
            current.next = current.next.next
            ll.size -= 1
        else:
            current = current.next
    return ll


# T: O(N2); S: O(1)
def remove_duplicates_constant_space(ll: LinkedList) -> LinkedList:
    if not ll.head:
        return ll

    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return ll


# -------------------------- 2. Remove Nth node -------------------------------

# T: O(N); S: O(1)
def remove_nth_node_from_end(n: int, ll: LinkedList) -> LinkedList:
    if not ll.head:
        return ll

    first_pointer = ll.head
    second_pointer = ll.head

    for _ in range(n):
        second_pointer = second_pointer.next

    while second_pointer.next:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next

    # OR JUST RETURN FIRST POINTER - Kth FROM THE LAST (^ while second_pointer)
    first_pointer.next = first_pointer.next.next
    return ll


def main():
    print("Removing duplicate linear space")
    dll = LinkedList()
    for value in (1, 1, 2, 3, 4, 5, 5, 5, 5, 6):
        dll.append(value)
    print(dll)
    remove_duplicates(dll)
    print(dll)

    print("\nRemoving duplicates constant space")
    dll = LinkedList()
    for value in (1, 1, 2, 3, 4, 5, 5, 5, 5, 6):
        dll.append(value)
    print(dll)
    remove_duplicates_constant_space(dll)
    print(dll)

    print("\nRemoving Nth item from list")
    dll = LinkedList()
    for value in range(10):
        dll.append(value)
    print(dll)
    remove_nth_node_from_end(3, dll)
    print(dll)


if __name__ == '__main__':
    main()
