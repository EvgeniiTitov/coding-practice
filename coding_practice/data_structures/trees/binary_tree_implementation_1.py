import typing as t


'''

        node
       /    \
      /      \
    node    node
'''


class BinaryTree:

    def __init__(self, value: t.Optional[t.Any] = None) -> None:
        self.value = value
        if value:
            self.left_node = BinaryTree()
            self.right_node = BinaryTree()
        else:
            self.left_node = None
            self.right_node = None

    def height(self) -> int:
        """
        Returns the height of the tree
        """
        if not self.value:
            return 0
        return max(self.left_node._height(), self.right_node._height())

    def _height(self) -> int:
        if not self.value:
            return 0
        return max(self.left_node._height(), self.right_node._height()) + 1

    def size(self) -> int:
        """
        Returns the number of nodes
        """
        if not self.value:
            return 0
        return 1 + self.left_node.size() + self.right_node.size()

    def occurs_in_tree(self, value: t.Any) -> bool:
        pass

    def occurs_in_bst(self, value: t.Any) -> bool:
        pass

    def insert_in_bst(self):
        pass

    def _delete_in_bst(self):
        pass

    def print_binary_tree(self):
        pass

    def _print_binary_tree(self):
        pass

    def pre_order_traversal(self):
        pass

    def in_order_traversal(self):
        pass

    def post_order_traversal(self):
        pass

    def evaluate(self):
        pass
