"""
LL based collision handling
"""


class ListNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None

    @property
    def pair(self) -> tuple:
        return self.key, self.value

    def update(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    def __init__(self, key_space: int = 2069) -> None:
        self._key_space = key_space
        self._storage = [None] * key_space

    def put(self, key: int, value: int) -> None:
        hash_key = key % self._key_space
        if self._storage[hash_key] is None:
            self._storage[hash_key] = ListNode(key, value)
            return
        current = self._storage[hash_key]
        while True:
            if current.key == key:
                current.update(key, value)
                return
            if not current.next:
                break
            current = current.next
        current.next = ListNode(key, value)

    def get(self, key):
        hash_key = key % self._key_space
        current = self._storage[hash_key]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key):
        hash_key = key % self._key_space
        current = previous = self._storage[hash_key]

        if current is None:
            return
        elif current.key == key:
            self._storage[hash_key] = current.next
            return

        current = current.next  # Since we checked this node's key already
        while current:
            if current.key == key:
                previous.next = current.next
                break
            previous = current
            current = current.next


def main():
    hash_map = HashMap()
    hash_map.put(1, 1)
    hash_map.put(2, 2)
    print(hash_map.get(1))
    print(hash_map.get(3))
    hash_map.put(2, 1)
    print(hash_map.get(2))
    hash_map.remove(2)
    print(hash_map.get(2))


if __name__ == "__main__":
    main()
