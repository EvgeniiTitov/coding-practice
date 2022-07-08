from typing import Optional


"""
Summary: No point traversing the whole tree if left/right not in the range! 
Nonlocal for variables with closures, no need for lists/dicts etc

_______________________________________________________________________________

https://leetcode.com/problems/range-sum-of-bst/


Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> int:
        if not root:
            return 0

        sum_ = 0

        def _traverse_the_tree(root: Optional[TreeNode]) -> None:
            nonlocal sum_
            if not root:
                return
            current = root.val
            if low <= current <= high:
                sum_ += current

            if low < current:
                _traverse_the_tree(root.left)

            if current < high:
                _traverse_the_tree(root.right)

        _traverse_the_tree(root)
        return sum_

    def rangeSumBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> int:

        sum_ = 0
        stack = [root]

        while len(stack):
            root = stack.pop(-1)
            if not root:
                continue  # Break instead of continue results in error.

            current = root.val
            if low <= current <= high:
                sum_ += current

            if low < current:
                stack.append(root.left)

            if current < high:
                stack.append(root.right)

        return sum_
