import typing as t


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


class CircularDoublyLinkedList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None

    @property
    def head_value(self) -> t.Any:
        return self._head.value if self._head else None

    @property
    def tail_value(self) -> t.Any:
        return self._tail.value if self._tail else None

    def create_cdll(self, value: t.Any) -> None:
        if self._head:
            raise Exception("CDLL is already initialized")

        node = Node(value)
        node.next = node.prev = node
        self._head = self._tail = node

    def insert_value(self, value: t.Any, position: int) -> None:
        if not self._head:
            raise Exception("Cannot insert a value to uninitialised LL")

        if position == 0:
            self._prepend(value)
        elif position == -1:
            self._append(value)
        else:
            self._insert_at_index(value, position)

    def traverse(self, line_end: str = " ") -> None:
        for node in self:
            print(node.value, end=line_end)

    def traverse_backwards(self, line_end: str = " ") -> None:
        current = self._tail
        while current:
            print(current.value, end=line_end)
            if current.prev == self._tail:
                break
            current = current.prev

    def search_value(self, value: t.Any) -> bool:
        for node in self:
            if node.value == value:
                return True
        return False

    def delete_at_index(self, position: int) -> None:
        if not self._head:
            raise Exception("Cannot delete a value from uninitialised LL")

        # If just one item in the list
        if self._head == self._tail:
            self._head.next = self._head.prev = None  # Points to itself
            self._head = self._tail = None
            return

        if position == 0:
            self._delete_first()
        elif position == -1:
            self._delete_last()
        else:
            self._delete_at_index(position)

    def delete_circular_linked_list(self):
        if not self._head:
            return
        # Get rid of circular references to allow GC
        current = self._head
        self._tail.next = None
        while current:
            current.prev = None
            current = current.next
        self._head = self._tail = None

    def _delete_first(self) -> None:
        current = self._head
        next_node = self._head.next
        # Unwire the node
        current.next = None
        current.prev = None
        # Update the references
        next_node.prev = self._tail
        self._head = next_node
        self._tail.next = next_node

    def _delete_last(self) -> None:
        last = self._tail
        before_last = self._tail.prev
        # Unwire the node
        last.next = last.prev = None
        # Update the references
        before_last.next = self._head
        self._head.prev = before_last
        self._tail = before_last

    def _delete_at_index(self, index: int) -> None:
        current = self._head
        curr_index = 0
        while curr_index < index - 1:
            curr_index += 1
            current = current.next
        # Unwire the node to delete
        current_next_next = current.next.next
        node_to_delete = current.next
        node_to_delete.next = node_to_delete.prev = None
        # Update the references
        current.next = current_next_next
        current_next_next.prev = current
        # IMPORTANT: If deleting the last, update the tail
        if current_next_next == self._head:
            self._tail = current

    def _prepend(self, value: t.Any) -> None:
        node = Node(value)
        # Connect new node to the former first node
        node.next = self._head
        self._head.prev = node
        # Connect the tail to the new first node
        self._tail.next = node
        node.prev = self._tail
        # Move the head pointer
        self._head = node

    def _append(self, value: t.Any) -> None:
        node = Node(value)
        # Connect new node to the former tail
        self._tail.next = node
        node.prev = self._tail
        # Connect the head to the new tail
        node.next = self._head
        self._head.prev = node
        # Move the tail pointer
        self._tail = node

    def _insert_at_index(self, value: t.Any, index: int) -> None:
        node = Node(value)
        # Reach the position to insert into
        current = self._head
        curr_index = 0
        while curr_index < index - 1:
            curr_index += 1
            current = current.next
        # Insert the new node between the other two nodes
        next_from_current = current.next
        current.next = node
        node.prev = current
        node.next = next_from_current
        next_from_current.prev = node
        # IMPORTANT: If inserting at the end, update the tail as well
        if next_from_current == self._head:
            self._tail = node

    def __iter__(self) -> t.Iterator[t.Any]:
        current = self._head
        while current:
            yield current
            if current.next == self._head:
                break
            current = current.next

    def __str__(self) -> str:
        values = [node.value for node in self]
        return f"< CircularDoublyLinkedList, values: {values} >"


def main():
    cdll = CircularDoublyLinkedList()

    """
    STDOUT:
    
    < CircularDoublyLinkedList, values: [] >
    < CircularDoublyLinkedList, values: [1, 2, 3, 4] >
    < CircularDoublyLinkedList, values: [1, 2, 100, 3, 4] >
    < CircularDoublyLinkedList, values: [1, 2, 100, 3, 4, 200] >
    < CircularDoublyLinkedList, values: [1, 2, 100, 3, 300, 4, 200] >
    
    Head value: 1; Tail value: 200
    
    1 2 100 3 300 4 200 
    1 2 100 3 300 4 200 
    200 4 300 3 100 2 1 
    
    Searching for 444 False
    Searching for 300 True
    < CircularDoublyLinkedList, values: [2, 100, 3, 300, 4, 200] >
    < CircularDoublyLinkedList, values: [2, 100, 3, 300, 4] >
    < CircularDoublyLinkedList, values: [2, 100, 300, 4] >
    < CircularDoublyLinkedList, values: [2, 100, 300] >
    
    Head value: 2; Tail value: 300
    
    < CircularDoublyLinkedList, values: [300] >
    
    Head value: 300; Tail value: 300
    
    < CircularDoublyLinkedList, values: [] >
    
    Head value: None; Tail value: None
    
    < CircularDoublyLinkedList, values: [100, 0] >
    """

    print(cdll)

    cdll.create_cdll(2)
    cdll.insert_value(1, 0)
    cdll.insert_value(3, -1)
    cdll.insert_value(4, -1)
    print(cdll)

    cdll.insert_value(100, 2)
    print(cdll)

    cdll.insert_value(200, 5)
    print(cdll)

    cdll.insert_value(300, 100)
    print(cdll)

    print(f"\nHead value: {cdll.head_value}; Tail value: {cdll.tail_value}")

    print()
    for node in cdll:
        print(node.value, end=" ")

    print()
    cdll.traverse()

    print()
    cdll.traverse_backwards()

    print("\n\nSearching for 444", cdll.search_value(444))
    print("Searching for 300", cdll.search_value(300))

    cdll.delete_at_index(0)
    print(cdll)

    cdll.delete_at_index(-1)
    print(cdll)

    cdll.delete_at_index(2)
    print(cdll)

    cdll.delete_at_index(3)
    print(cdll)
    print(f"\nHead value: {cdll.head_value}; Tail value: {cdll.tail_value}\n")

    cdll.delete_at_index(0)
    cdll.delete_at_index(0)
    print(cdll)
    print(f"\nHead value: {cdll.head_value}; Tail value: {cdll.tail_value}\n")

    cdll.delete_at_index(100)
    print(cdll)
    print(f"\nHead value: {cdll.head_value}; Tail value: {cdll.tail_value}\n")

    cdll.create_cdll(0)
    cdll.insert_value(100, 0)
    print(cdll)
    cdll.delete_circular_linked_list()


if __name__ == '__main__':
    main()
