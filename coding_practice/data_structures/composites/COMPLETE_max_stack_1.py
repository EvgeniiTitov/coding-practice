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

    def __init__(self):
        # Imitates out stack
        self._dll = DoublyLL()

        # To keep track of DLL nodes for each value
        self._values_nodes_mapping = defaultdict(set)

        # To keep track of the largest values stored on the heap
        self._max_elements_heap = []
        heapq.heapify(self._max_elements_heap)

    def push(self, x: int) -> None:
        # Add new number to the stack
        node = self._dll.prepend(x)
        # Keep track of its node
        self._values_nodes_mapping[x].add(node)
        # Update the heap
        heapq.heappush(self._max_elements_heap, -x)

    def top(self) -> int:
        return self._dll.top()

    def peekMax(self) -> int:
        return -self._max_elements_heap[0]

    def pop(self) -> int:
        # Pop the node off the stack
        node = self._dll.pop()
        value = node.value

        # Remove the node associated with its value
        self._values_nodes_mapping[value].remove(node)

        # Update the heap
        more_values = len(self._values_nodes_mapping[value]) > 0
        if not more_values:
            heapq.heappop(self._max_elements_heap)

        return value

    def popMax(self) -> int:
        # Get the current largest value on the stack
        max_value = -self._max_elements_heap[0]

        # Get the top-most node on the stack associated with such value
        node = self._values_nodes_mapping[max_value].pop()  # THIS IS WRONG - RETURNS THE FIRST, NEED THE LAST!

        # Remove the node from the stack
        self._dll.unwire_node(node)

        # Update the heap
        more_values = len(self._values_nodes_mapping[max_value]) > 0
        if not more_values:
            heapq.heappop(self._max_elements_heap)

        return max_value

    def __str__(self) -> str:
        return f"MaxStack. Values: {self._dll.get_values()}"


def main():
    # stack = MaxStack()
    # stack.push(5)
    # stack.push(1)
    # stack.push(5)
    # stack.push(0)
    #
    # print(stack)
    # print(stack.top())
    # print(stack.peekMax())
    #
    # print()
    # print(stack.pop())
    # print(stack.pop())
    # print(stack)
    # print(stack.peekMax())
    # ---

    # stack = MaxStack()
    # stack.push(5)
    # stack.push(7)
    # stack.push(1)
    # stack.push(7)
    # stack.push(5)
    # stack.push(0)
    #
    # print(stack)
    # print(stack.peekMax())
    #
    # print()
    # print(stack.pop())
    # print(stack)
    #
    # print()
    # print(stack.popMax())
    # print(stack)
    # ---

    stack = MaxStack()
    stack.push(5)
    stack.push(1)
    stack.push(5)

    print(stack.top())
    print(stack.popMax())
    print(stack.top())
    print(stack.peekMax())
    print(stack.pop())
    print(stack.top())

    # ---

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
    # stack = MaxStack()
    # stack.push(-2)
    # print(stack.popMax())
    #
    # stack.push(-45)
    # stack.push(-82)
    # stack.push(29)
    #
    # print(stack.pop())


if __name__ == '__main__':
    main()
