import typing as t


# TODO: Good idea to maintain a count (length of ll) that gets updated with
#       each operation


"""
Advantages Of DLL:

- Reversing the doubly linked list is very easy
- It can allocate or reallocate memory easily during its execution.
- The traversal of this doubly linked list is bidirectional which is not 
possible in a singly linked list.
- Deletion of nodes is easy as compared to a Singly Linked List. A singly 
linked list deletion requires a pointer to the node and previous node to be 
deleted but in the doubly linked list, it only required the pointer which 
is to be deleted.


Disadvantages Of DLL:

- It uses extra memory when compared to the array and singly linked list 
(extra reference).
- Since elements in memory are stored randomly, therefore the elements are 
accessed sequentially no direct access is allowed (no indexing)


Uses Of DLL:

- It is used in the navigation systems where front and back navigation is required.
- It is used by the browser to implement backward and forward navigation of 
visited web pages that is a back and forward button.
- It is also used to represent a classic game deck of cards.
- It is also used by various applications to implement undo and redo functionality.
- Doubly Linked List is also used in constructing MRU/LRU (Most/least recently used) cache.
- Also in many operating systems, the thread scheduler(the thing that chooses 
what process needs to run at which time) maintains a doubly-linked list of all 
processes running at that time.
"""


class EmptyLinkedListError(Exception):
    pass


class Node:
    def __init__(self, value: t.Any) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    @property
    def length(self) -> int:
        # TODO: Any way to calculate it quicker than O(N)?
        if not self.head:
            return 0

        head = self.head
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def append(self, data: t.Any) -> None:
        new_node = Node(data)
        new_node.prev = self.tail
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data: t.Any) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def peek_front(self) -> t.Any:
        if self.head:
            return self.head.value
        else:
            raise EmptyLinkedListError("Cannot peek into an empty LL")

    def peek_back(self) -> t.Any:
        if self.tail:
            return self.tail.value
        else:
            raise EmptyLinkedListError("Cannot peek into an empty LL")

    def pop_front(self) -> t.Any:
        if not self.head:
            raise EmptyLinkedListError("Cannot pop off an empty LL")
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.head.prev = None
        return temp.value

    def pop_back(self) -> t.Any:
        if not self.tail:
            raise EmptyLinkedListError("Cannot pop off an empty LL")
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        return temp.value

    def delete_value(self, value: t.Any) -> bool:
        if not self.head:
            raise EmptyLinkedListError("Cannot delete from an empty LL")

        # Check the ends
        if self.head.value == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return True
        elif self.tail.value == value:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return True

        current = self.head
        while current and current.value != value:
            current = current.next
        # No item to delete found
        if not current:
            return False

        # Relink the nodes skipping the one we're standing one
        current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

    def reverse(self) -> None:
        if not self.head:
            raise EmptyLinkedListError("Cannot reverse an empty LL")
        head = self.head
        head_next = head.next
        head.next = None
        head.prev = head_next
        while head_next:
            head_next.prev = head_next.next
            head_next.next = head
            head = head_next
            head_next = head_next.prev
        self.head = head

    def _accumulate_values(self) -> t.List[t.Any]:
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next

        # current = self.tail
        # while current:
        #     values.append(current.value)
        #     current = current.prev
        return values

    def __str__(self) -> str:
        values = self._accumulate_values()
        return f"DoublyLinkedList: {' '.join(map(str, values))}"


def main():
    ll = DoublyLinkedList()
    for i in range(6):
        ll.append(i)
    print(ll)
    print("Length:", ll.length)

    print("\nPrepending 10")
    ll.prepend(10)
    print(ll)
    print("Length:", ll.length)

    print(f"Head: {ll.peek_front()}; Tail: {ll.peek_back()}")

    print("\nPopping off the front:", ll.pop_front())
    print(ll)
    print("Length:", ll.length)
    print(f"Head: {ll.peek_front()}; Tail: {ll.peek_back()}")

    print("\nPopping off the back:", ll.pop_back())
    print(ll)
    print("Length:", ll.length)
    print(f"Head: {ll.peek_front()}; Tail: {ll.peek_back()}")

    print("\nReversing the list")
    ll.reverse()
    print(ll)

    print("\nDeleting 228")
    ll.delete_value(228)
    print(ll)
    print(("Deleting 2"))
    ll.delete_value(2)
    print(ll)

    ll.reverse()
    print("\nReversed back:", ll)


if __name__ == "__main__":
    main()
