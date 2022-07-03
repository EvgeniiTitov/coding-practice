from typing import Optional


"""
Summary: Global variable diameter that every recursive call compares to and
modifies if it found a bigger diameter
_______________________________________________________________________________

https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any 
two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of 
edges between them.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # T: O(N) - every node is visited; S: O(N)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # ~Global like variable that every recursive function call will compare
        # against
        diameter = 0

        def _measure_diameter(root: Optional[TreeNode]) -> int:
            # The function does 2 things:
            # 1. It always recalculates the diameter looking for the largest value
            # 2. It returns the longer branch + 1 (current node)
            if not root:
                return 0

            nonlocal diameter
            right_diameter = _measure_diameter(root.right) if root.right else 0
            left_diameter = _measure_diameter(root.left) if root.left else 0
            diameter = max(diameter, right_diameter + left_diameter)

            # Return the larger branch + current node
            return max(left_diameter, right_diameter) + 1

        _measure_diameter(root)
        return diameter

    # Example how to avoid global like variable, just pass and return the D
    # to every recursive call
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def _measure_diameter(root: Optional[TreeNode], max_diameter: int):
            if not root:
                return [0, max_diameter]

            right_diameter, max_diameter = _measure_diameter(
                root.right, max_diameter
            )
            left_diameter, max_diameter = _measure_diameter(
                root.left, max_diameter
            )
            diameter = max(max_diameter, right_diameter + left_diameter)
            return max(left_diameter, right_diameter) + 1, diameter

        return _measure_diameter(root, max_diameter=0)[-1]
