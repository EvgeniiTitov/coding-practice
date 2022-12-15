from typing import Optional


"""
https://leetcode.com/problems/search-in-a-binary-search-tree/

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the 
subtree rooted with that node. If such a node does not exist, return null.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Mine - correct one. T: O(log N) average. S: O(log N) average
    def searchBST(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        def _find_value_in_tree(
            root: Optional[TreeNode], val: int
        ) -> Optional[TreeNode]:
            if not root:
                return None
            if root.val == val:
                return root
            elif root.val < val:
                return _find_value_in_tree(root.right, val)
            else:
                return _find_value_in_tree(root.left, val)

        return _find_value_in_tree(root, val)

    # Iterative solution. T: O(log N) average. S: O(1) no recursive calls
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root

    # From solutions
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root

        return (
            self.searchBST(root.left, val)
            if val < root.val
            else self.searchBST(root.right, val)
        )
