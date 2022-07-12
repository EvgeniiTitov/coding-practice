import typing as t


"""
When inserting a string into a trie we first check if the root node has the
first letter of the string we want to insert.
"""


class TrieNode:
    def __init__(self):
        self.children: t.MutableMapping[str, TrieNode] = {}
        self._end_of_string = False

    @property
    def is_end_of_string(self) -> bool:
        return self._end_of_string

    def mark_as_end(self) -> None:
        self._end_of_string = True

    def unmark_as_end(self) -> None:
        self._end_of_string = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_string(self, string: str) -> bool:
        if not string:
            return False

        current = self.root
        for char in string:
            node = current.children.get(char)
            if not node:
                node = TrieNode()
                current.children.update({char: node})
            current = node
        current.mark_as_end()
        return True

    def search_string(self, string: str) -> bool:
        if not string:
            return True

        current = self.root
        for char in string:
            node = current.children.get(char)
            if not node:
                return False
            current = node

        return True if current.is_end_of_string else False

    @staticmethod
    def delete_string(root: TrieNode, string: str, index: int = 0) -> bool:
        char = string[index]
        current = root.children.get(char)

        if len(current.children) > 1:
            Trie.delete_string(current, string, index + 1)
            return False

        # At the last node of the string we want to delete while this string
        # is a prefix of another string. If the last node has references to
        # other characters, unmark it as end; Else delete the node entirely
        if index == len(string) - 1:
            if len(current.children) >= 1:
                current.unmark_as_end()
                return False
            else:
                root.children.pop(char)
                return True

        # Some other string is a prefix of the current string we're deleting
        if current.is_end_of_string:
            Trie.delete_string(current, string, index + 1)
            return False

        # Check if someone is dependent on the char we want to delete
        is_safe_to_delete = Trie.delete_string(current, string, index + 1)
        if is_safe_to_delete:
            root.children.pop(char)
            return True
        else:
            return False


def main():
    trie = Trie()
    print("Inserted apple:", trie.insert_string("apple"))
    print("Inserted applause:", trie.insert_string("applause"))

    print("\nChecking if apply exists:", trie.search_string("apple"))
    print("Checking if app exists:", trie.search_string("app"))

    print("\nDeleting apple")
    Trie.delete_string(trie.root, "apple")
    print("Checking if apple exists:", trie.search_string("apple"))


if __name__ == '__main__':
    main()
