import typing as t


"""
Summary: The idea is to use a dick to keep track of keys - O(1) to check if 
a key exists. DoublyLL node as a value. Use doubly LL to manage evictions etc
_______________________________________________________________________________

https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a 
Least Recently Used (LRU) cache.

Implement the LRUCache class:

- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. 
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds 
  the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
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

    # T: O(1)
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

    # T: O(1)
    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        node = self._cache.get(key)
        self._move_node_to_head(node)
        return node.value

    def _unwire_node(self, node: Node) -> None:
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
