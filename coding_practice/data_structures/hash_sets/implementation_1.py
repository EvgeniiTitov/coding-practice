import typing as t


"""
LL based implementation

In the Python implementation, we employed a sort of pseudo head to keep a 
reference to the actual head of the LinkedList, which could simplify a bit the 
logic by reducing the number of branchings.
"""


class Node:
    def __init__(
        self, value: t.Any, next_node: t.Optional["Node"] = None
    ) -> None:
        self.value = value
        self.next = next_node


class Bucket:
    # Acts as a Facade hiding the underlying details

    def __init__(self) -> None:
        self.head = Node(0)  # Pseudo head

    def insert(self, value: t.Any) -> None:
        if self.exists(value):
            return
        # Append new item to the beginning
        new_node = Node(value, next_node=self.head.next)
        self.head.next = new_node

    def delete(self, value: t.Any) -> None:
        previous = self.head
        current = self.head.next
        while current:
            if current.value == value:
                previous.next = current.next
            previous = current
            current = current.next

    def exists(self, value: t.Any) -> bool:
        current = self.head.next
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    # For __str__()
    def get_values_stored(self) -> t.Optional[t.List[t.Any]]:
        values = []
        current = self.head.next  # Skip pseudo head
        while current:
            values.append(current.value)
            current = current.next
        return values or None


class HashSet:
    def __init__(self) -> None:
        self._key_space = 769
        self._storage = [Bucket() for _ in range(self._key_space)]

    def add(self, item: int) -> None:
        self._storage[self._get_hash(item)].insert(item)

    def remove(self, item: int) -> None:
        self._storage[self._get_hash(item)].delete(item)

    def contains(self, item: int) -> bool:
        return self._storage[self._get_hash(item)].exists(item)

    def _get_hash(self, item: int) -> int:
        return item % self._key_space

    def __contains__(self, item: t.Any) -> bool:
        return self.contains(item)

    def __str__(self) -> str:
        stored_values = [
            bucket.get_values_stored() for bucket in self._storage
        ]
        out = []
        for bucket_values in stored_values:
            if bucket_values:
                out.extend(bucket_values)
        return f"HashSet: {' '.join(map(str, out))}"


def main():
    my_set = HashSet()

    my_set.add(0)
    for _ in range(5):
        my_set.add(1)
    my_set.add(2)
    print(my_set)

    print(2 in my_set)
    my_set.remove(2)
    print(2 in my_set)


if __name__ == "__main__":
    main()
