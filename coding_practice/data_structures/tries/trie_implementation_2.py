import typing as t


"""
Notice that the trie node doesn't store a value (char), it is stored implicitly
in the children dict.
"""


class TrieNode:
    def __init__(self) -> None:
        self.children: t.MutableMapping[str, TrieNode] = {}
        self.end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                new_node = TrieNode()
                current.children.update({char: new_node})
            current = current.children.get(char)
        current.end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children.get(char)
        return current.end_of_word

    def starts_with(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children.get(char)
        return True


def main():
    trie = Trie()
    for word in ("app", "apple", "applause", "kekl"):
        trie.insert(word)

    print("Does the word apple exist?", trie.search("apple"))
    print("Does the word ape exist?", trie.search("ape"))
    print("\nDoes the prefix appl exist?", trie.starts_with("appl"))
    print("Does the prefix appx exist?", trie.starts_with("appx"))


if __name__ == "__main__":
    main()
