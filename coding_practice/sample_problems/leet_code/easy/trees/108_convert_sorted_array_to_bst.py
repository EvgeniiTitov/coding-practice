from typing import List, Optional

from coding_practice.utils import print_tree_inorder


"""
Summary:
    1. Recursive - the array is sorted --> good indication the root will be 
    in the middle. Then keep building the left and right subtrees considering
    the left and right subsets from the middle value you picked as the root
_______________________________________________________________________________

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def _build_tree(
            node: TreeNode, values: List[int], is_left: bool
        ) -> None:

            # Base case
            if not len(values):
                return

            middle_index = len(values) // 2
            middle_value = values[middle_index]
            new_node = TreeNode(middle_value)
            left_values_subset = values[: middle_index]
            right_values_subset = values[middle_index + 1:]
            if is_left:
                node.left = new_node
            else:
                node.right = new_node

            _build_tree(new_node, left_values_subset, is_left=True)
            _build_tree(new_node, right_values_subset, is_left=False)

        if not len(nums):
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])

        root_index = len(nums) // 2
        root_value = nums[root_index]
        root = TreeNode(root_value)
        left_subset = nums[: root_index]
        right_subset = nums[root_index + 1:]

        _build_tree(root, left_subset, is_left=True)
        _build_tree(root, right_subset, is_left=False)

        return root

    # Same but different
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not len(nums):
            return

        middle_index = len(nums) // 2
        return TreeNode(
            val=nums[middle_index],
            left=self.sortedArrayToBST(nums=nums[: middle_index]),
            right=self.sortedArrayToBST(nums=nums[middle_index + 1:])
        )


def main():
    root = Solution().sortedArrayToBST(nums=[-10, -3, 0, 5, 9])
    print_tree_inorder(root)
    print(root.val)
    print(root.left.val)
    print(root.right.val)


if __name__ == '__main__':
    main()
