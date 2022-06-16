import typing as t


class EmptyStackError(Exception):
    pass


class Stack:

    def __init__(self) -> None:
        self._data = []

    @property
    def is_empty(self) -> bool:
        return len(self._data) == 0

    def peek(self):
        if self.is_empty:
            raise EmptyStackError("Stack is empty")
        return self._data[-1]

    def push(self, value: t.Any) -> None:
        self._data.append(value)

    def pop(self):
        if self.is_empty:
            raise EmptyStackError("Stack is empty")
        return self._data.pop(-1)

    def __len__(self) -> int:
        return len(self._data)

    def __str__(self) -> str:
        return f"Stack: {self._data}"


def main() -> None:
    s = Stack()
    for i in range(5):
        s.push(i)
    print(s)
    print(f"Pooping: {s.pop()}")
    print(f"Peeking: {s.peek()}")
    print(f"Is empty? {s.is_empty}")
    s.push(228)
    print(s)
    

if __name__ == '__main__':
    main()
