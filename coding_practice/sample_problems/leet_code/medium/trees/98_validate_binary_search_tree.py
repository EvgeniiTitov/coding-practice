from typing import Optional

from coding_practice.utils import build_tree_from_list


"""
Summary:
    Brute force: In-order tree traversal to accumulate all items in the BST
    in ascending order (if its a valid BST). Then, validate the ascending order
    
    ! Recursive tree traversal with allowed ranges for each subtree! Very cool
    
_______________________________________________________________________________

https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Working brute force. T: O(N); S: O(N)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def _in_order_traversal(root: TreeNode, elements: list[int]) -> None:
            if root.left:
                _in_order_traversal(root.left, elements)
            elements.append(root.val)
            if root.right:
                _in_order_traversal(root.right, elements)

        if not root:
            return True

        elements = []  # S: O(N)
        _in_order_traversal(root, elements)  # T: O(N)

        for i in range(len(elements) - 1):  # T: O(N)
            curr_element = elements[i]
            next_element = elements[i + 1]
            if curr_element >= next_element:
                return False
        return True

    # That's pretty cool
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def _validate_tree(
            root: Optional[TreeNode], min_limit: float, max_limit: float
        ) -> bool:
            # Empty trees are valid BSTs
            if not root:
                return True

            # The current node's value must be within the allowed range
            if root.val <= min_limit or root.val >= max_limit:
                return False

            is_left_valid = _validate_tree(root.left, min_limit, root.val)
            is_right_valid = _validate_tree(root.right, root.val, max_limit)
            return is_left_valid and is_right_valid

        return _validate_tree(root, float("-inf"), float("inf"))

    # 72/80, wrong as it marks this 5,4,6,None,None,3,7 as valid
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def _validate_bst(root: TreeNode) -> bool:
            if root.left:
                is_left_valid = _validate_bst(root.left)
            else:
                is_left_valid = True

            if root.right:
                is_right_valid = _validate_bst(root.right)
            else:
                is_right_valid = True

            if is_left_valid and is_right_valid:
                left_cond = root.val > root.left.val if root.left else True
                right_cond = root.val < root.right.val if root.right else True
                return left_cond and right_cond
            else:
                return False

        if not root:
            return True

        return _validate_bst(root)


def main():
    root = build_tree_from_list(
        # [2, 1, 3]
        [5, 1, 4, None, None, 3, 6]
    )
    print(Solution().isValidBST(root))


if __name__ == '__main__':
    main()
