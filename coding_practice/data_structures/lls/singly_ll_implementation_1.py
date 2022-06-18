import typing as t


class IndexOutOfRangeError(Exception):
    pass


class Node:
    def __init__(self, value: t.Any) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(
        self,
        elements: t.Optional[t.Sequence[t.Any]] = None,
        key: t.Callable = lambda e: e,
    ) -> None:
        # TODO: Could remember the length and then update it
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
        if not self.head:
            return False
        if not self.head.next:
            return True
        node = self.head
        while node.next:
            value_current = node.value
            value_next = node.next.value
            if value_current > value_next:
                return False
            node = node.next
        return True

    def print(self, separator: str = ", ") -> None:
        if self.head:
            values = self._collect_all_values()
            print(separator.join(map(str, values)))

    def extend(self, ll: "LinkedList") -> None:
        if not ll.head:
            return
        if not self.head:
            self.head = ll.head
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = ll.head

    def reverse(self) -> None:
        if not self.head:
            return
        node = self.head.next
        self.head.next = None
        while node:
            next_node = node.next
            node.next = self.head
            self.head = node
            node = next_node

    def get_index_of_value(self, value: t.Any) -> t.Optional[int]:
        if not self.head:
            return None
        node = self.head
        index = 0
        while node:
            if node.value == value:
                return index
            node = node.next
            index += 1

    def get_value_at_index(self, index: int) -> t.Optional[t.Any]:
        if not self.head:
            return None
        if index >= self.length or index < 0:
            raise IndexOutOfRangeError(
                "Wrong index value. Must be [0, len(LL) - 1]"
            )
        node = self.head
        i = 0
        while node:
            if i == index:
                return node.value
            i += 1
            node = node.next

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

    def insert_value_at(self, value: t.Any, index: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        if index < 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.head
        while node.next and index > 1:
            node = node.next
            index -= 1
        new_node.next = node.next
        node.next = new_node

    def delete_value(self, value: t.Any) -> bool:
        if not self.head:
            return False
        if self.head.value == value:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
            return True
        node = self.head
        while node.next and node.next.value != value:
            node = node.next
        if node.next:
            node.next = node.next.next
            return True
        return False

    def apply_function(self, func: t.Callable) -> None:
        """
        Modify each value of the LL
        :return:
        """
        if not self.head:
            return
        node = self.head
        while node:
            try:
                node.value = func(node.value)
            except Exception as e:
                print(
                    f"Failed while applying callable {func.__name__} to "
                    f"value {node.value}. Error: {e}"
                )
                raise e
            node = node.next

    def _collect_all_values(self) -> t.List[t.Any]:
        if not self.head:
            return []
        node = self.head
        values = []
        while node:
            values.append(node.value)
            node = node.next
        return values

    def insert_value_before(self):
        # TODO: Complete me
        pass

    def insert_value_after(self):
        # TODO: Complete me
        pass

    def insert_sorted_after(self):
        # TODO: Complete me
        pass

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        if not self.head:
            return ""
        else:
            values = self._collect_all_values()
            return f"LinkedList: {' -> '.join(map(str, values))}"


if __name__ == "__main__":
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

    print("\nGetting index of value 100")
    print(ll.get_index_of_value(100))

    print("\nGetting value at index 4")
    print(ll.get_value_at_index(4))

    print("\nInserting new value -10 at index 6")
    ll.insert_value_at(-10, index=6)
    print(ll)
    print("Inserting new values 0 and 1234 at -3 and 100 indices")
    ll.insert_value_at(0, index=-3)
    ll.insert_value_at(1234, index=100)
    print(ll)

    print("\nDeleting value -10", ll.delete_value(-10))
    print(ll)
    print("Deleting value 1234", ll.delete_value(1234))
    print(ll)
    print("Deleting value -1234", ll.delete_value(-1234))
    print(ll)

    print("\nApplying function x * 2 to all nodes")
    ll.apply_function(lambda e: e * 2)
    print(ll)

    print("\nIs LL sorted?", ll.is_sorted)
    new_ll = LinkedList([1, 2, 3, 4, 5])
    print(f"Is this LL: {new_ll} sorted? {new_ll.is_sorted}")

    print("\nReversing LL")
    ll.reverse()
    print(ll)
