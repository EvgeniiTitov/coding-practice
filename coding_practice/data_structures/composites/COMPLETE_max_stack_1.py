import typing as t
import heapq
from collections import defaultdict


# TODO: Close but not quite, needs further debugging...


"""
Summary:

Stack is a DLL. 
Heap to keep track of the largest element on the stack
A dictionary with keys being values stored on the stack (ints), and values 
being a set of nodes in which a value is stored

Getting max value of the heap is O(1)
Getting the node in which the max value is stored is O(1)
_______________________________________________________________________________

https://leetcode.com/problems/max-stack/

Design a max stack data structure that supports the stack operations and 
supports finding the stack's maximum element.

Implement the MaxStack class:
- MaxStack() Initializes the stack object.
- void push(int x) Pushes element x onto the stack.
- int pop() Removes the element on top of the stack and returns it.
- int top() (PEEK) Gets the element on the top of the stack without removing it.
- int peekMax() Retrieves the maximum element in the stack without removing it.
- int popMax() Retrieves the maximum element in the stack and removes it. 
  If there is more than one maximum element, only remove the top-most one.

You must come up with a solution that supports 
O(1) for each top call and 
O(log n) for each other call.
"""


class LLNode:
    def __init__(
        self,
        value: t.Any,
        next: t.Optional["LLNode"] = None,
        prev: t.Optional["LLNode"] = None
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLL:
    """
    dll = DoublyLL()

    for i in range(5):
        dll.prepend(i)
    print(dll)

    dll.pop()
    print(dll)

    dll.prepend(7)
    print(dll)

    second_node = dll._head.next
    print(second_node.value)

    dll.unwire_node(second_node)
    print(dll)

    Stdout:
    DLL. Items: [4, 3, 2, 1, 0]
    DLL. Items: [3, 2, 1, 0]
    DLL. Items: [7, 3, 2, 1, 0]
    3
    DLL. Items: [7, 2, 1, 0]
    """
    def __init__(self) -> None:
        self._head = None
        self._tail = None

    def prepend(self, value: t.Any) -> LLNode:
        new_node = LLNode(value)
        if not self._head:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        return new_node

    def pop(self) -> t.Optional[LLNode]:
        if not self._head:
            return

        node = self._head
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            next_node = self._head.next
            next_node.prev = None
            self._head.next = None
            self._head = next_node
        return node

    def top(self) -> t.Optional[t.Any]:
        if self._head:
            return self._head.value
        else:
            return None

    def unwire_node(self, node: LLNode) -> None:
        prev = node.prev
        next = node.next

        if not prev and not next:
            # Node is a single node in LL
            self._head = self._tail = None
        elif not prev:
            # Node is a head
            node.next = None
            next.prev = None
            self._head = next
        elif not next:
            # Node is a tail
            prev.next = None
            node.prev = None
            self._tail = prev
        else:
            # Node is in the middle
            prev.next = next
            next.prev = prev

    def get_values(self) -> t.List[t.Any]:
        values = []
        curr = self._head
        while curr:
            values.append(curr.value)
            curr = curr.next
        return values

    def __str__(self) -> str:
        return f"DLL. Items: {self.get_values()}"


class MaxStack:

    """
    Might not need to store node on the heap!
    """

    def __init__(self):
        self._max_elements_heap = []
        heapq.heapify(self._max_elements_heap)
        self._dll = DoublyLL()
        self._values_nodes_mapping = defaultdict(set)

    def push(self, x: int) -> None:
        node = self._dll.prepend(x)
        # Heap doesn't support duplicates, append only if unique number
        if x in self._values_nodes_mapping:
            self._values_nodes_mapping[x].add(node)
        else:
            self._values_nodes_mapping[x].add(node)
            heapq.heappush(self._max_elements_heap, -x)

    def pop(self) -> int:
        node = self._dll.pop()
        value = node.value
        self._values_nodes_mapping[value].remove(node)

        max_value = -self._max_elements_heap[0]
        if value == max_value and len(self._values_nodes_mapping[value]) == 0:
            heapq.heappop(self._max_elements_heap)

        return value

    def top(self) -> int:
        return self._dll.top()

    def peekMax(self) -> int:
        max_value  = self._max_elements_heap[0]
        return -max_value

    def popMax(self) -> int:
        max_value = -self._max_elements_heap[0]
        such_values_stored = len(self._values_nodes_mapping[max_value])
        if such_values_stored == 1:
            heapq.heappop(self._max_elements_heap)
            node = self._values_nodes_mapping[max_value].pop()  # O(1) as set
        else:
            node = self._values_nodes_mapping[max_value].pop()
        self._dll.unwire_node(node)
        return max_value

    def __str__(self) -> str:
        return f"MaxStack. Values: {self._dll.get_values()}"


def main():
    # stack = MaxStack()
    # stack.push(5)
    # stack.push(1)
    # stack.push(5)
    #
    # # print(stack)
    # # print("Peeking:", stack.top())
    # # print("Popping:", stack.pop())
    # # print(stack)
    # #
    # # print("PeeingMax:", stack.peekMax())
    # # print(stack)
    # #
    # # print("Popping max:", stack.popMax())
    # # print(stack)
    #
    # print(stack)
    #
    # print(stack.top())
    # print(stack.popMax())
    # print(stack)
    # print(stack.top())
    # print("Peeking max:", stack.peekMax())

    # -----------
    stack = MaxStack()
    stack.push(-2)
    print(stack.popMax())

    stack.push(-45)
    stack.push(-82)
    stack.push(29)

    print(stack.pop())


if __name__ == '__main__':
    main()
