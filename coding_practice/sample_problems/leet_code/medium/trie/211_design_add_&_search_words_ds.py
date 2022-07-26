import typing as t


"""
Summary: 
_______________________________________________________________________________

https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and finding if a string 
matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure 
that matches word or false otherwise. word may contain dots '.' where dots 
can be matched with any letter.
 
Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]

[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""


# ----------------------------  cheat solution --------------------------------
from collections import defaultdict

# Works but exceeds the time limit, very inefficient
class WordDictionary:
    def __init__(self) -> None:
        self.words_dict = defaultdict(list)

    def addWord(self, word: str) -> None:
        self.words_dict[len(word)].append(word)

    def search(self, word: str) -> bool:
        word_length = len(word)
        for stored_word in self.words_dict[word_length]:
            matched = self._check_words_match(word, stored_word, word_length)
            if matched:
                return True
        return False

    def _check_words_match(
        self, word: str, stored_word: str, length: int
    ) -> bool:
        for i in range(length):
            if word[i] not in [".", stored_word[i]]:
                return False
        return True


# -------------------------- proper solution 1 (bugged)------------------------

class Node:
    def __init__(self) -> None:
        self.children: t.MutableMapping[str, Node] = {}
        self.is_end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        if not word:
            return
        current = self.root
        for char in word:
            if char not in current.children:
                new_node = Node()
                current.children.update({char: new_node})
            current = current.children.get(char)
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        if not word:
            return True
        return self._search(word, self.root)

    def _search(self, word: str, root: Node) -> bool:
        if not word:
            return True
        current = root
        for i, char in enumerate(word):
            if not len(current.children):
                return False

            if char == ".":
                for curr_lvl_char in current.children:
                    does_exist = self._search(
                        curr_lvl_char + word[i + 1:], current
                    )
                    if does_exist:
                        return True
            else:
                if char not in current.children:
                    return False
                current = current.children.get(char)
        return current.is_end_of_word


# ------------------------ proper solution 2 (works) --------------------------

TrieNode = t.MutableMapping[str, t.MutableMapping]
WordEnd = "$"


class WordDictionary:

    def __init__(self):
        self._trie = {}

    def addWord(self, word: str) -> None:
        if not word:
            return
        current = self._trie
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[WordEnd] = True

    def search(self, word: str) -> bool:

        def _search(word: str, node: TrieNode) -> bool:
            for i, char in enumerate(word):
                if char not in node:
                    if char == ".":
                        for node_char in node:
                            if (
                                node_char != WordEnd and
                                _search(word[i + 1:], node[node_char])
                            ):
                                return True
                    return False
                else:
                    node = node[char]

            return WordEnd in node

        if not word:
            return False
        return _search(word, self._trie)


def main():
    trie = WordDictionary()
    # trie.addWord("bad")
    # trie.addWord("dad")
    # trie.addWord("mad")
    #
    # print(trie.search("pad"))  # False
    # print(trie.search("bad"))  # True
    # print(trie.search(".ad"))  # True
    # print(trie.search("b.."))  # True

    trie.addWord("a")
    trie.addWord("a")
    print(trie.search("."))  # True
    print(trie.search("a"))  # True
    print(trie.search("aa"))  # False
    print(trie.search("a."))  # True
    print(trie.search(".a"))


if __name__ == '__main__':
    main()
