import typing as t


class EmptyStackError(Exception):
    pass


class Node:
    def __init__(self, data: t.Any) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self._top = None
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    def push(self, data: t.Any) -> None:
        if data is None:
            return
        data_node = Node(data)
        if not self._top:
            self._top = data_node
        else:
            data_node.next = self._top
            self._top = data_node
        self._size += 1

    def pop(self) -> t.Any:
        if not self._top:
            raise EmptyStackError("Cannot pop from the empty stack")
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data

    def peek(self) -> t.Any:
        if not self._top:
            raise EmptyStackError("Cannot peek into the empty stack")
        return self._top.data

    def is_empty(self) -> bool:
        return self._size == 0

    def __str__(self) -> str:
        return f"Stack. Size: {self.size}"


def main():
    stack = Stack()
    for item in range(10):
        stack.push(item)
    print(stack)

    print("\nIs stack empty?", stack.is_empty())
    print("\nPoping item:", stack.pop())
    print("\nPeeking:", stack.peek())
    print("\nStack size:", stack.size)

    print("Poping the remaining items:")
    try:
        while True:
            print(stack.pop(), end=" ")
    except Exception as e:
        print(f"Caught error: {e}")


if __name__ == "__main__":
    main()
