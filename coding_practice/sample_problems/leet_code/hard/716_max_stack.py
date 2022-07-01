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
"""


# This won't work because when you pop max, all the item on top keep referring
# to its value, so they would need to be updated!
class MaxStack:

    def __init__(self):
        self._stack = []

    def push(self, x):
        if not len(self._stack):
            self._stack.append((x, 0))
        else:
            current_max_idx = self._stack[-1][-1]
            current_max_val = self._stack[current_max_idx][0]
            i = len(self._stack) if x >= current_max_val else current_max_idx
            self._stack.append((x, i))

    def pop(self):
        # When we just pop, the next item on the stack will hold reference to
        # the next greatest item within the stack
        return self._stack.pop()[-1]

    def top(self):
        return self._stack[-1][0]

    def peekMax(self):
        return self._stack[self._stack[-1][-1]][0]

    def popMax(self):
        """
        When we pop max value, which might be somewhere within the stack, all
        items coming after it will be referencing it as the max value --> hence
        when popping it off, we need to iterate over the items to the right
        and fix the references to the new max
        """
        current_max_idx = self._stack[-1][-1]
        current_max_value = self._stack[current_max_idx][0]
        # TODO: Do the thing

    def __str__(self) -> str:
        return f"MaxStack: {self._stack}"



def main():
    mstack = MaxStack()
    for item in [1, 3, 2, 4, 2, -4]:
        mstack.push(item)
    print(mstack)


if __name__ == '__main__':
    main()
