### Trie (or prefix tree)


![alt text](../../../images/trie.gif?raw=true)
--- 

### TODO:

- Implementing autocomplete functionality (- https://stackoverflow.com/questions/46038694/implementing-a-trie-to-support-autocomplete-in-python)

- Or a spell checker (parse provided text, for each word check if it exists)

---

- The root (the first node) could potentially store every char in a large Trie

- Trie node doesn't store a value (char) explicitly, it is stored implicitly
in the children dict.

```python
class TrieNode:
    def __init__(self) -> None:
        self.children: t.MutableMapping[str, TrieNode] = {}
        self.end_of_word = False
```

