from typing import Optional


"""
https://leetcode.com/problems/insert-into-a-binary-search-tree/

You are given the root node of a binary search tree (BST) and a value to 
insert into the tree. Return the root node of the BST after the insertion. 
It is guaranteed that the new value does not exist in the original BST.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # T: O(log N) average; T: O(log N) average
    def insertIntoBST(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)

        def _insert_value(root: TreeNode, val: int) -> Optional[TreeNode]:
            if root.val == val:
                return
            if val < root.val:
                if root.left:
                    return _insert_value(root.left, val)
                else:
                    root.left = TreeNode(val)
                    return root
            else:
                if root.right:
                    return _insert_value(root.right, val)
                else:
                    root.right = TreeNode(val)
                    return root

        head = root
        _insert_value(root, val)
        return head

    # From solutions
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val > root.val:
            # insert into the right subtree
            root.right = self.insertIntoBST(root.right, val)
        else:
            # insert into the left subtree
            root.left = self.insertIntoBST(root.left, val)
        return root

    # Iterative solution
    def insertIntoBST(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        head = root
        while True:
            if root.val == val:
                return
            elif val < root.val:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    return head
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    return head
