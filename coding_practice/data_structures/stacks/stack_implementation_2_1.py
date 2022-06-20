
class EmptyStackError(Exception):
    pass


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class MinStack:
    def __init__(self) -> None:
        self._top = None
        self._min = None
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    def push(self, value: int) -> None:
        if value is None:
            return

        data_node = Node(value)
        if self._top:
            data_node.next = self._top
        self._top = data_node
        if not self._min:
            self._min = data_node
        else:
            current_min_value = self._min.data
            if value < current_min_value:
                self._min = data_node
        self._size += 1

    def pop(self) -> int:
        if not self._top:
            raise EmptyStackError("Cannot pop from the empty stack")
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data

    def get_min(self) -> int:
        if not self._top:
            raise EmptyStackError("Cannot get min value from the empty stack")
        return self._min.data

    def peek(self) -> int:
        if not self._top:
            raise EmptyStackError("Cannot peek into the empty stack")
        return self._top.data

    def is_empty(self) -> bool:
        return self._size == 0

    def __str__(self) -> str:
        return f"Stack. Size: {self.size}"


def main():
    stack = MinStack()
    for number in [1, 3, 0, -1, 10, 100]:
        stack.push(number)

    print("Stack:", stack)
    print("Min value:", stack.get_min())

    print("\nAdding new smaller values")
    for number in range(5, 15, 2):
        if number % 2:
            stack.push(-number)
        else:
            stack.push(number)
        print("Min value:", stack.get_min())

    print("\nPeeking:", stack.peek())
    print("Poping:", stack.pop())

if __name__ == '__main__':
    main()
