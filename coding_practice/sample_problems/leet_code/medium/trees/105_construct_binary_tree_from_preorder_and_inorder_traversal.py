from typing import List, Optional

from coding_practice.utils import build_tree_from_list


# TODO: Understand me and write summary


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder 
traversal of a binary tree and inorder is the inorder traversal of the same tree, 
construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""


# def pre_order(tree: "TreeNode", items: List[int]) -> None:
#     items.append(tree.val)
#
#     if tree.left:
#         pre_order(tree.left, items)
#
#     if tree.right:
#         pre_order(tree.right, items)
#
#
# def in_order(tree: "TreeNode", items: List[int]) -> None:
#     if tree.left:
#         in_order(tree.left, items)
#
#     items.append(tree.val)
#
#     if tree.right:
#         in_order(tree.right, items)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:

        def _build_tree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_order_index

            # Base case
            if left > right:
                return None

            root_value = preorder[pre_order_index]
            root = TreeNode(root_value)

            pre_order_index += 1

            root.left = _build_tree(left, inorder_mapping[root_value] - 1)
            root.right = _build_tree(inorder_mapping[root_value] + 1, right)

            return root

        length = len(preorder)
        if not length:
            return None
        elif length == 1:
            return TreeNode(preorder[0])

        pre_order_index = 0
        inorder_mapping = {}
        for index, value in enumerate(inorder):
            inorder_mapping[value] = index

        return _build_tree(0, length - 1)


def main():
    root = build_tree_from_list(elements=[3, 9, 20, None, None, 15, 7])
    # items = []
    # in_order(root, items)
    # print("In order:", items)
    #
    # items = []
    # pre_order(root, items)
    # print("Pre order:", items)


if __name__ == '__main__':
    main()
