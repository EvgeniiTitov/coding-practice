from typing import Optional, List


"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []

        def _traverse_tree(root: Optional[TreeNode]) -> None:
            if root:
                elements.append(root.val)
                _traverse_tree(root.left)
                _traverse_tree(root.right)

        _traverse_tree(root)
        return elements
