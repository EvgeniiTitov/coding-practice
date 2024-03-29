import typing as t
from queue import Queue


__all__ = ["build_tree_from_list", "print_tree_inorder"]


class TreeNode:
    def __init__(
        self,
        val: t.Any = 0,
        left: t.Optional["TreeNode"] = None,
        right: t.Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"TreeNode: val {self.val}"


def build_tree_from_list(elements: t.List[t.Any]) -> t.Optional[TreeNode]:
    if not len(elements):
        return

    queue: "Queue[TreeNode]" = Queue()
    root = TreeNode(elements.pop(0))
    queue.put(root)
    while queue.qsize():
        node = queue.get()

        try:
            left_child_element = elements.pop(0)
        except IndexError:
            left_child_element = None
        if left_child_element is not None:
            node.left = TreeNode(left_child_element)
            queue.put(node.left)

        try:
            right_child_element = elements.pop(0)
        except IndexError:
            right_child_element = None
        if right_child_element is not None:
            node.right = TreeNode(right_child_element)
            queue.put(node.right)

    return root


def print_tree_inorder(tree: TreeNode) -> None:
    tree_elements = _traverse_tree_inorder(tree)
    print(tree_elements)


def _traverse_tree_inorder(tree: TreeNode) -> t.List[t.Any]:
    elements = []
    if tree.left:
        elements.extend(_traverse_tree_inorder(tree.left))
    elements.append(tree.val)
    if tree.right:
        elements.extend(_traverse_tree_inorder(tree.right))
    return elements


if __name__ == "__main__":
    tree = build_tree_from_list(
        elements=[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    )
    print(tree.left.right.right)
    print_tree_inorder(tree)
