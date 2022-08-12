from typing import Iterator, TypeVar
from collections import deque


T = TypeVar("T")
R = TypeVar("R")
Pair = tuple[T, R]


class VectorClock:
    def __init__(self, length: int) -> None:
        self._length = length
        self._queue = deque()

    @property
    def length(self) -> int:
        return len(self._queue)

    @property
    def pairs(self) -> list[Pair]:
        pairs = []
        for item in self._queue:
            pairs.append(item)
        return pairs

    def add_vector_pair(self, pair: Pair) -> None:
        self._queue.append(pair)
        if len(self._queue) > self._length:
            self._queue.popleft()

    def get_vectors(self) -> Iterator[Pair]:
        for item in self._queue:
            yield item

    def __str__(self) -> str:
        return f"VectorClock: {self.pairs}"


def main():
    vector_clock = VectorClock(3)
    vector_clock.add_vector_pair(("one", 1))
    vector_clock.add_vector_pair(("two", 2))
    vector_clock.add_vector_pair(("three", 3))
    print(vector_clock)

    vector_clock.add_vector_pair(("four", 4))
    print(vector_clock)

    vector_clock.add_vector_pair(("five", 5))
    print(vector_clock)

    print()
    for pair in vector_clock.get_vectors():
        print(pair)


if __name__ == '__main__':
    main()
