from typing import Optional


"""
Summary: If a subtree is imbalanced -> the whole tree is imbalanced. 
_______________________________________________________________________________

https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as - a binary tree 
in which the left and right subtrees of every node differ in height by no 
more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._is_balanced(root)[0]

    def _is_balanced(self, root: Optional[TreeNode]) -> tuple:
        if not root:
            return True, 0

        is_left_balanced, left_depth = self._is_balanced(root.left)
        is_right_balanced, right_depth = self._is_balanced(root.right)

        current_height = 1 + max(left_depth, right_depth)

        # If left or right is imbalanced -> whole tree is imbalanced
        if not is_left_balanced or not is_right_balanced:
            return False, current_height

        # Left and right could be balanced, but of different heights
        if abs(left_depth - right_depth) > 1:
            return False, current_height

        # Subtrees are balanced and their height diff <= 1
        return True, current_height

    # Shorter one
    def isBalanced(self, root):

        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1

