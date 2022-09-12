import typing as t
from queue import Queue


# TODO: Complete me (stopped 261)


"""
TODO: I don't like we call traversal for Nones, unnecessary calls, just check
TODO: To aggregate values pass a list to a function and keep adding there
TODO: To use a generator instead implement the traversal iteratively


"""


class AVLNode:
    def __init__(self, data: t.Any) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def pre_order_traversal(root: t.Optional[AVLNode]) -> None:
    if not root:
        return
    print(root.data)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)


def in_order_traversal(root: t.Optional[AVLNode]) -> None:
    if not root:
        return
    pre_order_traversal(root.left)
    print(root.data)
    pre_order_traversal(root.right)


def post_order_traversal(root: t.Optional[AVLNode]) -> None:
    if not root:
        return
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)
    print(root.data)


def level_order_traversal(root: t.Optional[AVLNode], sep: str = "\n") -> None:
    if not root:
        return

    queue = Queue()
    queue.put(root)
    while queue.qsize():
        node = queue.get()
        print(node.data, end=sep)
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)
    print()


def _insert_bst_node_no_balancing(root: AVLNode, child: AVLNode) -> None:
    if child.data == root.data:
        return
    elif child.data < root.data:
        if not root.left:
            root.left = child
        else:
            _insert_bst_node_no_balancing(root.left, child)
    else:
        if not root.right:
            root.right = child
        else:
            _insert_bst_node_no_balancing(root.right, child)


def build_avl_from_iterable(items: t.Sequence[t.Any]) -> t.Optional[AVLNode]:
    if not len(items):
        return
    root = AVLNode(items[0])
    for item in items[1:]:
        node = AVLNode(item)
        _insert_bst_node_no_balancing(root, node)
    return root


def search_value(root: AVLNode, value: t.Any) -> bool:
    if not root:
        return False
    if root.data == value:
        return True
    if value < root.data:
        if not root.left:
            return False
        else:
            return search_value(root.left, value)
    else:
        if not root.right:
            return False
        else:
            return search_value(root.right, value)


def main():
    items = [70, 50, 90, 30, 60, 20, 40, 80, 100]
    root = build_avl_from_iterable(items)
    level_order_traversal(root, sep=" ")
    print("Searching value 200", search_value(root, 200))
    print("Searching value 20", search_value(root, 20))


if __name__ == '__main__':
    main()
