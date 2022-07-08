"""
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:
-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""


# ---- Iteration 1 ------
# class MinStack:
#
#     def __init__(self):
#         self._stack = []
#         self._min_value = None
#
#     def push(self, val: int) -> None:
#         if not self._min_value:
#             self._min_value = val
#         else:
#             self._min_value = min(self._min_value, val)
#         self._stack.append(val)
#
#     def pop(self) -> None:
#         if len(self._stack):
#             value = self._stack.pop()
#             self._update_min_value(value)  # Linear time
#             return value
#
#     def top(self) -> int:
#         if len(self._stack):
#             poped_value = self._stack[-1]
#             return poped_value
#
#     def getMin(self) -> int:
#         return self._min_value
#
#     def _update_min_value(self, removed_value: int) -> None:
#         if removed_value == self._min_value and len(self._stack):
#             self._min_value = min(self._stack)  # That's not linear time


# ----- Iteration 2 -----
class MinStack:
    def __init__(self):
        self.stack = []  # has val, and current_min

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            last_val, last_min = self.stack[-1]
            if val < last_min:
                self.stack.append((val, val))
            else:
                self.stack.append((val, last_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


def main():
    stack = MinStack()
    stack.push(3)
    stack.push(1)
    stack.push(2)
    # stack.push(-3)
    print(stack._stack)
    # print(stack.top())
    # print(stack.getMin())
    # print(stack.pop())
    # print(stack.getMin())
    # print(stack.top())


if __name__ == "__main__":
    main()
