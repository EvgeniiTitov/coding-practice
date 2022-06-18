from typing import Optional, List


'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 
Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Time complexity is O(n)
Space complaxity is O(n)
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # My solution
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        def _traverse_tree_inorder(root: TreeNode) -> List[int]:
            elements = []
            if root.left:
                elements.extend(_traverse_tree_inorder(root.left))
            elements.append(root.val)
            if root.right:
                elements.extend(_traverse_tree_inorder(root.right))
            return elements

        return _traverse_tree_inorder(root)

    # Solution from comments
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree_vals = []

        def inorder(tree):
            if tree:
                inorder(tree.left)
                tree_vals.append(tree.val)
                inorder(tree.right)

        inorder(root)
        return tree_vals
