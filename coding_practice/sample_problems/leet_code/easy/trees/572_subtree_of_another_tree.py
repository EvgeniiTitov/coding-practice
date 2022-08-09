from typing import Optional


"""
Summary: The idea is to run the check from every node in the tree -> BFS using
a queue. From each node, run your recursive checking function.

+ there are some cheesy solutions with converting the trees to strings and
checking if subtree in tree
_______________________________________________________________________________

https://leetcode.com/problems/subtree-of-another-tree/

Given the roots of two binary trees root and subRoot, return true if there is 
a subtree of root with the same structure and node values of subRoot and 
false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and 
all of this node's descendants. The tree could also be considered as a 
subtree of itself.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:

        from queue import Queue

        def _check_if_subtree(
            root: Optional[TreeNode], sub_root: Optional[TreeNode]
        ) -> bool:
            if not root and not sub_root:
                return True
            if root and not sub_root or sub_root and not root:
                return False
            if root.val != sub_root.val:
                return False

            is_left_valid = _check_if_subtree(root.left, sub_root.left)
            is_right_valid = _check_if_subtree(root.right, sub_root.right)

            return is_left_valid and is_right_valid

        queue = Queue()
        queue.put(root)
        is_subroot = False
        while queue.qsize():
            node = queue.get()

            is_curr_node_subroot = _check_if_subtree(node, subRoot)
            if is_curr_node_subroot:
                is_subroot = True

            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)

        return is_subroot
