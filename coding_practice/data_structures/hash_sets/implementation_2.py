import typing as t


"""
BST based implementation
"""


class TreeNode:
    def __init__(self, value: t.Any) -> None:
        self.val = value
        self.left = None
        self.right = None


class BSTree:
    def __init__(self) -> None:
        self.root = None

    @staticmethod
    def find_successor(root: TreeNode) -> TreeNode:
        root = root.right
        while root.left:
            root = root.left
        return root

    @staticmethod
    def find_predecessor(root: TreeNode) -> TreeNode:
        root = root.left
        while root.right:
            root = root.right
        return root

    def search_bst(
        self, root: t.Optional[TreeNode], val: t.Any
    ) -> t.Optional[TreeNode]:
        if not root or root.val == val:
            return root
        if val < root.val:
            return self.search_bst(root.left, val)
        else:
            return self.search_bst(root.right, val)

    def insert_into_bst(
        self, root: t.Optional[TreeNode], val: t.Any
    ) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val == val:
            return root
        elif val < root.val:
            root.left = self.insert_into_bst(root.left, val)
        else:
            root.right = self.insert_into_bst(root.right, val)
        return root

    def delete_node_in_bst(
        self, root: t.Optional[TreeNode], val: t.Any
    ) -> TreeNode:
        if not root:
            return root
        if val < root.val:
            root.left = self.delete_node_in_bst(root.left, val)
        elif val > root.val:
            root.right = self.delete_node_in_bst(root.right, val)
        else:  # Found the value to delete
            if not root.right and not root.left:
                root = None
            elif root.right:
                root.val = self.find_successor(root.right)
                root.right = self.delete_node_in_bst(root.right, root.val)
            else:
                root.val = self.find_predecessor(root.left)
                root.left = self.delete_node_in_bst(root.left, root.val)
        return root

    def collect_stored_values(
        self, root: t.Optional[TreeNode]
    ) -> t.List[t.Any]:
        if not root:
            return []
        elements = [root.val]  # pre-order traversal
        if root.left:
            elements += self.collect_stored_values(root.left)
        if root.right:
            elements += self.collect_stored_values(root.right)
        return elements


class Bucket:
    def __init__(self) -> None:
        self.tree = BSTree()

    def insert(self, value: t.Any) -> None:
        self.tree.root = self.tree.insert_into_bst(self.tree.root, value)

    def delete(self, value: t.Any) -> None:
        self.tree.root = self.tree.delete_node_in_bst(self.tree.root, value)

    def exists(self, value: t.Any) -> bool:
        return self.tree.search_bst(self.tree.root, value) is not None

    def get_stored_values(self) -> t.List[t.Any]:
        return self.tree.collect_stored_values(self.tree.root)


class HashSet:
    def __init__(self, key_range: int = 769) -> None:
        self._key_range = key_range
        self._storage = [Bucket() for _ in range(key_range)]

    def _get_hash(self, key: int) -> int:
        return key % self._key_range

    def add(self, key: int) -> None:
        self._storage[self._get_hash(key)].insert(key)

    def remove(self, key: int) -> None:
        self._storage[self._get_hash(key)].delete(key)

    def contains(self, key: int) -> bool:
        return self._storage[self._get_hash(key)].exists(key)

    def __contains__(self, item):
        return self.contains(item)

    def __str__(self) -> str:
        values = []
        for bucket in self._storage:
            values.extend(bucket.get_stored_values())
        return f"HashSet storing: {' '.join(map(str, values))}"


def main():
    s = HashSet()
    s.add(1)
    for _ in range(5):
        s.add(2)
    s.add(3)
    print(s)

    s.remove(3)
    s.remove(10)
    print(s)

    print(s.contains(2), 2 in s)


if __name__ == "__main__":
    main()
