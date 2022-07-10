from typing import Optional, List


"""
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []

        def _traverse_tree(root: Optional[TreeNode]) -> None:
            if root:
                _traverse_tree(root.left)
                _traverse_tree(root.right)
                elements.append(root.val)

        _traverse_tree(root)
        return elements

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                elements.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return elements[::-1]
