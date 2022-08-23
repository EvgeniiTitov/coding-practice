import typing as t


"""
When it comes to dealing with circular linked lists, regardless whether its
singly or doubly ll, we want to have a HEAD and a TAIL:

           -------------------<-----------------^
           |                                    |
           
HEAD --> 1 | 111 --> 2 | 222 --> 3 | 333 --> 4 | 444
 001      001          111         222         333

                                                ^
TAIL -------------------------------------------|
 333


Inserting a new node:
    - At the beginning (prepending)
    - At the end (appending)
    - At a certain location (index, etc) (inserting) 
When appending/prepending we need to update not only the HEAD, TAIL but also
maintain the circle of references.


When deleting a node:
    - Deleting the first node
    - Deleting the last node
    - Deleting at the certain location


The __del__() method is a known as a destructor method in Python. It is called 
when all references to the object have been deleted i.e when an object is 
garbage collected. Note : A reference to objects is also deleted when the 
object goes out of reference or when the program ends.
To delete this circular monstrosity we need to get rid of the circular links.
"""


class Node:
    def __init__(self, value: t.Any) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"< Node, value: {self.value} >"


class CircularSinglyLinkedList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None

    def create_circular_linked_list(self, value: t.Any) -> None:
        node = Node(value)
        node.next = node  # Points to itself
        self._head = self._tail = node

    def insert_value(self, value: t.Any, position: int) -> None:
        if not self._head:
            raise Exception("Create CSLL first before inserting a value")

        if position == 0:
            self._prepend(value)
        elif position == -1:
            self._append(value)
        else:
            # We could wrap around, no checking the position lols
            self._insert_at_index(value, position)

    def delete_at_index(self, index: int) -> bool:
        if not self._head:
            return False

        # If just one element in the list left
        if self._head == self._tail:
            self._head.next = None  # Node points to itself!
            self._head = self._tail = None
            return True

        if index == 0:
            self._delete_first()
        elif index == -1:
            self._delete_last()
        else:
            self._delete_at_index(index)
        return True

    def search_value(self, value: t.Any) -> bool:
        if not self._head:
            raise Exception("Nothing to search in the empty CSLL")

        current = self._head
        while current:
            if current.value == value:
                return True
            if current.next == self._head:
                return False
            current = current.next

    def delete_circular_linked_list(self):
        self._head = None
        self._tail.next = None
        self._tail = None

    def _prepend(self, value: t.Any) -> None:
        node = Node(value)
        node.next = self._head
        self._head = node
        self._tail.next = node  # Connect the end to the new beginning

    def _append(self, value: t.Any) -> None:
        node = Node(value)
        node.next = self._tail.next
        self._tail.next = node
        self._tail = node

    def _insert_at_index(self, value: t.Any, index: int) -> None:
        current = self._head
        curr_index = 0
        while curr_index < index - 1:
            curr_index += 1
            current = current.next

        next_node = current.next
        node = Node(value)
        current.next = node
        node.next = next_node

    def _delete_first(self) -> None:
        next_node = self._head.next
        self._head.next = None
        self._tail.next = next_node
        self._head = next_node

    def _delete_last(self) -> None:
        current = self._head
        while current.next != self._tail:
            current = current.next
        first_node = self._tail.next
        self._tail.next = None
        self._tail = current
        self._tail.next = first_node

    def _delete_at_index(self, index: int) -> None:
        current = self._head
        curr_index = 0
        while curr_index < index - 1:
            curr_index += 1
            current = current.next

        next_next = current.next.next
        current.next.next = None
        current.next = next_next

    def __iter__(self) -> t.Iterator[t.Any]:
        current = self._head
        while current:
            yield current
            # Avoid cycling
            if current.next == self._head:  # OR self._tail.next
                break
            current = current.next

    def __str__(self) -> str:
        values = [value.value for value in self]
        return f"< CircularSinglyLL, node values: {values} >"


def main():
    circular_ll = CircularSinglyLinkedList()
    circular_ll.create_circular_linked_list(1)
    print(circular_ll)

    circular_ll.insert_value(0, 0)
    circular_ll.insert_value(2, -1)
    circular_ll.insert_value(3, -1)
    circular_ll.insert_value(2, 2)
    print(circular_ll)

    print("Searching value 4:", circular_ll.search_value(4))
    print("Searching value 3:", circular_ll.search_value(3))

    circular_ll.delete_at_index(0)
    print(circular_ll)

    circular_ll.delete_at_index(-1)
    print(circular_ll)

    circular_ll.delete_at_index(-1)
    print(circular_ll)

    circular_ll.insert_value(3, -1)
    circular_ll.insert_value(4, -1)
    print(circular_ll)

    circular_ll.delete_at_index(2)
    print(circular_ll)

    circular_ll.delete_at_index(100)
    print(circular_ll)

    circular_ll.delete_at_index(0)
    print(circular_ll)

    circular_ll.delete_at_index(10)
    print(circular_ll)


if __name__ == '__main__':
    main()
