from collections import OrderedDict
import typing as t


"""
OrderedDict - appends item to the right. So, right is out head in this case.
- When limit is reached, .popitem(last=False) pops the item from the left.
- When getting an item, move it to the head by .move_to_end(key)
"""


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._cache = OrderedDict()

    def put(self, key: t.Hashable, value: int) -> None:
        if key in self._cache:
            del self._cache[key]  # This bit is required, why?
        self._cache[key] = value
        if len(self._cache) > self._capacity:
            self._cache.popitem(last=False)

    def get(self, key: t.Hashable) -> int:
        if key not in self._cache:
            return -1
        value = self._cache.get(key)
        self._cache.move_to_end(key)
        return value

    def clear(self) -> None:
        self._cache.clear()

    def __len__(self) -> int:
        return len(self._cache)

    def __str__(self) -> str:
        return f"LRUCache: stored keys: {list(self._cache.keys())}"


def main():
    """
    Adding 0. Cache: LRUCache: stored keys: [0]
    Adding 1. Cache: LRUCache: stored keys: [0, 1]
    Adding 2. Cache: LRUCache: stored keys: [0, 1, 2]
    Adding 3. Cache: LRUCache: stored keys: [0, 1, 2, 3]
    Adding 4. Cache: LRUCache: stored keys: [0, 1, 2, 3, 4]
    Adding 5. Cache: LRUCache: stored keys: [1, 2, 3, 4, 5]
    Adding 6. Cache: LRUCache: stored keys: [2, 3, 4, 5, 6]
    Adding 7. Cache: LRUCache: stored keys: [3, 4, 5, 6, 7]
    Adding 8. Cache: LRUCache: stored keys: [4, 5, 6, 7, 8]
    Adding 9. Cache: LRUCache: stored keys: [5, 6, 7, 8, 9]

    Getting 6: 6
    LRUCache: stored keys: [5, 7, 8, 9, 6]

    Getting 7: 7
    LRUCache: stored keys: [5, 8, 9, 6, 7]

    Cache cleared. LRUCache: stored keys: []
    """
    cache = LRUCache(5)
    for i in range(10):
        cache.put(i, i)
        print(f"Adding {i}. Cache: {cache}")

    print("\nGetting 6:", cache.get(6))
    print(cache)
    print("\nGetting 7:", cache.get(7))
    print(cache)

    cache.clear()
    print("\nCache cleared.", cache)


if __name__ == "__main__":
    main()
