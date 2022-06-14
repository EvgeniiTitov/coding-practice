import typing as t


class Node:
    def __init__(self, value: t.Any) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(
        self,
        elements: t.Optional[t.Sequence[t.Any]] = None,
        key: t.Callable = lambda e: e
    ) -> None:
        self._key = key
        if not elements:
            self.head = None
        else:
            node = Node(elements[0])
            self.head = node
            for element in elements[1:]:
                new_node = Node(element)
                node.next = new_node
                node = new_node

    @property
    def length(self) -> int:
        if not self.head:
            return 0

        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    @property
    def is_sorted(self) -> bool:
        # TODO:
        return True

    def print(self, separator: str = ", ") -> None:
        if self.head:
            values = self._collect_all_values()
            print(separator.join(map(str, values)))

    def extend(self):
        pass

    def reverse(self):
        pass

    def get_index_of_value(self):
        pass

    def get_value_at(self):
        pass

    def prepend(self, value: t.Any) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def append(self, value: t.Any) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node

    def insert_value_at(self):
        pass

    def insert_value_before(self):
        pass

    def insert_value_after(self):
        pass

    def delete_value(self):
        pass

    def insert_sorted_after(self):
        pass

    def apply_function(self):
        pass

    def _collect_all_values(self) -> t.List[t.Any]:
        if not self.head:
            return []
        node = self.head
        values = []
        while node:
            values.append(node.value)
            node = node.next
        return values

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        if not self.head:
            return ""
        else:
            values = self._collect_all_values()
            return f"LinkedList: {' -> '.join(map(str, values))}"


if __name__ == '__main__':
    items = [4, 5, 1, 2, 7, 3]
    ll = LinkedList(items)

    print("Length:", ll.length, len(ll))

    print("\nPrinting LL:")
    ll.print("; ")
    print(ll)

    print("\nAppending item 100")
    ll.append(100)
    print(ll)

    print("\nPrepending item 228")
    ll.prepend(228)
    print(ll)

