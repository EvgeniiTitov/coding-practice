import collections
import typing as t


class Queue:

    def __init__(self) -> None:
        self._buffer = collections.deque()

    @property
    def is_empty(self) -> bool:
        return self.size() == 0

    def put(self, item: t.Any) -> None:
        # TODO: How to implement blocking vs non-blocking?
        self._buffer.appendleft(item)

    def get(self) -> t.Any:
        # TODO: How to implement blocking vs non-blocking?
        if not self.is_empty:
            return self._buffer.pop()

    def size(self) -> int:
        return len(self._buffer)

    def __str__(self) -> str:
        return f"Queue: {self._buffer}"


def main() -> None:
    q = Queue()
    for i in range(5):
        q.put(i)
    print(q)
    print(f"Is empty? {q.is_empty}")
    print(f"Queue size: {q.size()}")
    print(f"Getting item: {q.get()}")


if __name__ == '__main__':
    main()
