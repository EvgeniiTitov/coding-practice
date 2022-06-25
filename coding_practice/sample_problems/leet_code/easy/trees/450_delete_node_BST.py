from typing import Optional


"""
Given a root node reference of a BST and a key, delete the node with the 
given key in the BST. Return the root node reference (possibly updated) 
of the BST.

Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.


Algorithm:

- If key > root.val then delete the node to delete is in the right subtree 
  root.right = deleteNode(root.right, key).

- If key < root.val then delete the node to delete is in the left subtree 
  root.left = deleteNode(root.left, key).

- If key == root.val then the node to delete is right here. Let's do it :
    - If the node is a leaf, the delete process is straightforward: root = null
    - If the node is not a leaf and has the right child, then replace the node 
    value by a successor value root.val = successor.val, and then recursively 
    delete the successor in the right subtree 
    root.right = deleteNode(root.right, root.val).
    - If the node is not a leaf and has only the left child, then replace the 
    node value by a predecessor value root.val = predecessor.val, and then 
    recursively delete the predecessor in the left subtree 
    root.left = deleteNode(root.left, root.val).

- Return root.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _find_successor(self, root: TreeNode) -> TreeNode:
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def _find_predecessor(self, root: TreeNode) -> TreeNode:
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(
        self, root: Optional[TreeNode], key: int
    ) -> Optional[TreeNode]:
        # Base case
        if not root:
            return None

        # 1) First identify the node if any that must be deleted
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # 2) Found the node, delete the current one
        else:
            # The node is a leaf
            if not root.left and not root.right:
                root = None
            elif root.right:
                # Find new value from the right - successor
                root.val = self._find_successor(root)
                # Delete the successor as we moved it up
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self._find_predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        # It is important to return the root when deleting a node in BST
        return root
