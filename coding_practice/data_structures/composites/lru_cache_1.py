import typing as t


"""
Here head and tail are dummy nodes, which allows to avoid dealing with some
annoying edge cases
"""


class Node:
    def __init__(self) -> None:
        self.key = 0
        self.value = 0
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache: t.MutableMapping[int, Node] = {}
        self._size = 0
        self._head = Node()
        self._tail = Node()
        self._head.next = self._tail
        self._tail.prev = self._head

    def put(self, key: int, value: int) -> None:
        node = self._cache.get(key)
        if not node:
            new_node = Node()
            new_node.key = key
            new_node.value = value
            # Add new node
            self._cache[key] = new_node
            self._prepend_new_node(new_node)
            self._size += 1
            # Keep track of the size evicting if reached the limit
            if self._size > self._capacity:
                tail = self._pop_tail_node()
                del self._cache[tail.key]
                self._size -= 1
        else:
            node.value = value
            self._move_node_to_head(node)

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        node = self._cache.get(key)
        self._move_node_to_head(node)
        return node.value

    @staticmethod
    def _unwire_node(node: Node) -> None:
        node_next = node.next
        node_prev = node.prev
        node_prev.next = node_next
        node_next.prev = node_prev

    def _move_node_to_head(self, node: Node) -> None:
        self._unwire_node(node)
        self._prepend_new_node(node)

    def _prepend_new_node(self, node: Node) -> None:
        node.next = self._head.next
        self._head.next.prev = node
        node.prev = self._head
        self._head.next = node

    def _pop_tail_node(self) -> Node:
        tail_node = self._tail.prev
        self._unwire_node(tail_node)
        return tail_node

    def __str__(self) -> str:
        items = []
        head = self._head
        head = head.next
        while head != self._tail:
            items.append((head.key, head.value))
            head = head.next
        return f"LRUCache: stored keys: {items}"


def main():
    """
    Adding 0. Cache: LRUCache: stored keys: [(0, 0)]
    Adding 1. Cache: LRUCache: stored keys: [(1, 1), (0, 0)]
    Adding 2. Cache: LRUCache: stored keys: [(2, 2), (1, 1), (0, 0)]
    Adding 3. Cache: LRUCache: stored keys: [(3, 3), (2, 2), (1, 1), (0, 0)]
    Adding 4. Cache: LRUCache: stored keys: [(4, 4), (3, 3), (2, 2), (1, 1), (0, 0)]
    Adding 5. Cache: LRUCache: stored keys: [(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)]
    Adding 6. Cache: LRUCache: stored keys: [(6, 6), (5, 5), (4, 4), (3, 3), (2, 2)]
    Adding 7. Cache: LRUCache: stored keys: [(7, 7), (6, 6), (5, 5), (4, 4), (3, 3)]
    Adding 8. Cache: LRUCache: stored keys: [(8, 8), (7, 7), (6, 6), (5, 5), (4, 4)]
    Adding 9. Cache: LRUCache: stored keys: [(9, 9), (8, 8), (7, 7), (6, 6), (5, 5)]

    Getting 6: 6
    LRUCache: stored keys: [(6, 6), (9, 9), (8, 8), (7, 7), (5, 5)]

    Getting 7: 7
    LRUCache: stored keys: [(7, 7), (6, 6), (9, 9), (8, 8), (5, 5)]
    """
    cache = LRUCache(5)
    for i in range(10):
        cache.put(i, i)
        print(f"Adding {i}. Cache: {cache}")

    print("\nGetting 6:", cache.get(6))
    print(cache)
    print("\nGetting 7:", cache.get(7))
    print(cache)


if __name__ == "__main__":
    main()
