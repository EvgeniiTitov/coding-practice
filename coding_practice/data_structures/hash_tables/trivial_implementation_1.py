import typing as t


'''
The most basic hash map, doesn't solve any issues such as collision etc.
'''


class TrivialHashTable:
    def __init__(self, size: int) -> None:
        self._size = size
        self._array = [None for _ in range(size)]

    def _get_hash(self, key: str) -> int:
        h = 0
        for char in key:
            h += ord(char)
        return h % self._size

    def __setitem__(self, key: str, value: t.Any) -> None:
        self._array[self._get_hash(key)] = value

    def __getitem__(self, item):
        return self._array[self._get_hash(item)]

    def __delitem__(self, key):
        self._array[self._get_hash(key)] = None

    def __str__(self) -> str:
        return f"{self._array}"


def main():
    hash_map = TrivialHashTable(30)
    hash_map["one"] = 1
    hash_map["two"] = 2
    hash_map["three"] = 3
    hash_map["four"] = 4
    hash_map["five"] = 5
    print(hash_map)


if __name__ == '__main__':
    main()
