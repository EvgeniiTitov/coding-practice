import typing as t


"""
Summary:

_______________________________________________________________________________

https://leetcode.com/problems/max-stack/

Design a max stack data structure that supports the stack operations and 
supports finding the stack's maximum element.

Implement the MaxStack class:
- MaxStack() Initializes the stack object.
- void push(int x) Pushes element x onto the stack.
- int pop() Removes the element on top of the stack and returns it.
- int top() Gets the element on the top of the stack without removing it.
- int peekMax() Retrieves the maximum element in the stack without removing it.
- int popMax() Retrieves the maximum element in the stack and removes it. 
  If there is more than one maximum element, only remove the top-most one.

You must come up with a solution that supports O(1) for each top call 
and O(logn) for each other call? 


Approach 2: DLL + TreeMap


"""

# Iteration 1 - list based. Doesn't satisfy time complexity, yet simple
class MaxStack:

    def __init__(self):
        self._stack = []

    def push(self, x: int) -> None:
        self._stack.append(x)

    def pop(self) -> int:
        return self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def peekMax(self) -> int:
        return max(self._stack)  # O(N)

    # Reversing to pop the top most item if there're 1+ same items
    def popMax(self) -> int:  # O(N)
        self._stack.reverse()

        # 1. Build in approach
        max_index = self._stack.index(max(self._stack))

        # 2. Finding max element manually
        max_value = float("-inf")
        max_index = -1
        for i in range(len(self._stack)):
            if self._stack[i] >= max_value:
                max_value = self._stack[i]
                max_index = i

        item = self._stack.pop(max_index)
        self._stack.reverse()
        return item

    def __str__(self) -> str:
        return f"MaxStack: {self._stack}"


# Iteration 2


def main():
    stack = MaxStack()
    for item in (1, 3, 0, 5, 10, 1, 10, 3, 10, 2, 4, -6):
        stack.push(item)
    print(stack)
    print("Peeking max:", stack.peekMax())
    print("Popping max:", stack.popMax())
    print(stack)


if __name__ == '__main__':
    main()
