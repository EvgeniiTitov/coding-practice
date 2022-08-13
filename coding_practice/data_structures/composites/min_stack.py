from collections import deque


"""
(item, curr_min)

(9, 2)
(2, 2)
(7, 5)
(5, 5)
"""


class MinStack:

    def __init__(self):
        self._stack = deque()

    def push(self, val: int) -> None:
        if not len(self._stack):
            self._stack.append([val, val])
        else:
            _, curr_min = self._stack[-1]
            new_min = min(curr_min, val)
            self._stack.append([val, new_min])

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def get_min(self) -> int:
        return self._stack[-1][1]


def main():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)

    print(stack.get_min())
    print(stack.pop())
    print(stack.top())
    print(stack.get_min())


if __name__ == '__main__':
    main()
