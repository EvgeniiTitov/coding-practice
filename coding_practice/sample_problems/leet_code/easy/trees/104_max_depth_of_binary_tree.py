from typing import Optional


"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Thoughts:
Simple DFS. Measure depth of the left and right subtrees, pick the greatest

Time complexity : we visit each node exactly once, thus the time complexity is
 O(N), where NN is the number of nodes.
 
Space complexity : in the worst case, the tree is completely unbalanced, e.g. 
each node has only left child node, the recursion call would occur N times 
(the height of the tree), therefore the storage to keep the call stack would 
be O(N). But in the best case (the tree is completely balanced), the height of
the tree would be log(N). Therefore, the space complexity in this case would 
be O(log(N)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Mine recursive
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        def _measure_tree_depth(node: TreeNode) -> int:
            depth = 1
            depth_left = _measure_tree_depth(node.left) if node.left else 0
            depth_right = _measure_tree_depth(node.right) if node.right else 0
            deepest_subtree = max(depth_left, depth_right)
            depth += deepest_subtree
            return depth

        return _measure_tree_depth(root)

    # Recursive from the solutions
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

    # Iteration based solution
    # Stack allows to simulate DFS well. We add node, then we pop it, add 2
    # children (left and right). Then we pop left, add its children to the
    # stack and so on.
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root:
            stack.append((1, root))

        depth = 0
        while len(stack):
            current_depth, node = stack.pop()
            if node:
                depth = max(current_depth, depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth
