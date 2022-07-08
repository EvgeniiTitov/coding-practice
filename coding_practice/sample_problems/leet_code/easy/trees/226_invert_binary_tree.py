from typing import Optional


"""
https://leetcode.com/problems/invert-binary-tree/
Given the root of a binary tree, invert the tree (exchange left and right
branches), and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]


Thoughts:
When thinking about recursing it seems to help to thinking bottom --> up. You 
keep digging down your tree until you hit the base case - no kids.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Recursive
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if root and not root.left and not root.right:
            return root

        from queue import Queue

        queue = Queue()
        queue.put(root)
        while queue.qsize():
            node = queue.get()
            node_left, node_right = node.left, node.right

            node.left = node_right
            node.right = node_left

            if node_left:
                queue.put(node_left)
            if node_right:
                queue.put(node_right)
        return root
