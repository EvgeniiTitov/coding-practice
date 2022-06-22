import typing


'''
Poor hash function could lead to collisions, i.e the same key could result in 
the same memory location for storing values
'''


class HashTable:
    def __init__(self, size: int) -> None:
        self._size = size
        self._arr = [[] for _ in range(self._size)]

    def _get_hash(self, key: str) -> int:
        h = 0
        for char in key:
            h += ord(char)
        return h % self._size

    def __setitem__(self, key, value):
        h = self._get_hash(key)

        # Check if such key already exists for this hash value, if yes update
        # the pair (key, value) with the provided value
        found = False
        for i, element in enumerate(self._arr[h]):
            if len(element) == 2 and element[0] == key:
                self._arr[h][i] = (key, value)
                found = True
                break

        if not found:
            self._arr[h].append((key, value))

    def __getitem__(self, item):
        for element in self._arr[self._get_hash(item)]:
            if element[0] == item:
                return element[1]
        # TODO: Optionally raise an exception or return None

    def __delitem__(self, key):
        h = self._get_hash(key)
        for i, element in enumerate(self._arr[h]):
            if element[0] == key:
                del self._arr[h][i]

    def __str__(self):
        return f"HashTable: {self._arr}"


def main():
    hash_map = HashTable(5)
    hash_map["one"] = 1
    hash_map["two"] = 2
    hash_map["three"] = 3
    hash_map["four"] = 4
    hash_map["five"] = 5
    print(hash_map)

    del hash_map["three"]
    print(hash_map)

    print("\nAccessing existing items:", hash_map["two"], hash_map["four"])
    print("Accessing non-existing items:", hash_map["kek"])


if __name__ == '__main__':
    main()
