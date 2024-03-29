from typing import Optional


"""
Summary:
    Recursive solution:
    Time complexity : O(n). Because we traverse the entire input tree once, 
    the total run time is O(n), where n is the total number of nodes in the tree.
    
    Space complexity : The number of recursive calls is bound by the height of the tree. 
    In the worst case, the tree is linear and the height is in O(n). Therefore, 
    space complexity due to recursive calls on the stack is O(n) in the worst case.
_______________________________________________________________________________

https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # From solution - recursive
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def _compare_trees(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            if not left or not right:  # One of them is null
                return False
            return (
                left.val == right.val
                and _compare_trees(left.right, right.left)
                and _compare_trees(left.left, right.right)
            )

        return _compare_trees(root, root)

    # This is interesting
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        from queue import Queue

        queue = Queue()
        queue.put(root)
        queue.put(root)

        while queue.qsize():
            node_1 = queue.get()
            node_2 = queue.get()

            if not node_1 and not node_2:
                continue
            if not node_1 or not node_2:
                return False
            if node_1.val != node_2.val:
                return False

            queue.put(node_1.left)
            queue.put(node_2.right)
            queue.put(node_1.right)
            queue.put(node_2.left)

        return True
