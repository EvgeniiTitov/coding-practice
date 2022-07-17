from typing import Optional


"""
Summary: Recursion or iterative. Compare the roots and left's left/right's left
and left's right/right's right

! NOTES:
Recursive; T: O(N), visit each node ones. S: O(N) - recursion stack for
unbalanced tree

Iterative BFS; T: O(N), visit each node ones; S: O(N) - worst case for
perfectly balanced tree we store entire lvl in the Q, last lvl is N nodes
_______________________________________________________________________________

https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check if 
they are the same or not.

Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Recursive; T: O(N), visit each node ones. S: O(N) - recursion stack for
    # unbalanced tree
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q or q and not p:
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False

        same_left = self.isSameTree(p.left, q.left)
        if not same_left:
            return False
        same_right = self.isSameTree(p.right, q.right)
        if not same_right:
            return False
        return True

    # Iterative BFS; T: O(N), visit each node ones; S: O(N) - worst case for
    # perfectly balanced tree we store entire lvl in the Q, last lvl is N nodes
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q or q and not p:
            return False
        if not p and not q:
            return True

        from queue import Queue
        queue = Queue()
        queue.put((p, q))
        while queue.qsize():
            node_1, node_2 = queue.get()

            if node_1 and not node_2 or node_2 and not node_1:
                return False

            if not node_1 and not node_2:
                continue

            if node_1.val != node_2.val:
                return False

            queue.put((node_1.left, node_2.left))
            queue.put((node_1.right, node_2.right))

        return True
