from typing import Optional

from coding_practice.utils import build_tree_from_list


"""
Summary:
    Brute force like approach - collect all root values in the tree using
    in-order traversal (ascending order). Then pick the Kth element.
    
    Smart way - no need to traverse all nodes, we need only first K nodes,
    so in-order traversal from the smallest to Kth element. We go down left
    till we reach the smallest node, then we start counting
_______________________________________________________________________________

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree, and an integer k, return the kth 
smallest value (1-indexed) of all the values of the nodes in the tree.

DFS? 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Dumb way yet passes all the tests (128 ms). T: O(N)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Collect all items: In-order? left current right
        def _collect_items_in_order(root: Optional[TreeNode]) -> list[int]:
            items = []
            if root.left:
                items.extend(_collect_items_in_order(root.left))
            items.append(root.val)
            if root.right:
                items.extend(_collect_items_in_order(root.right))
            return items

        items = _collect_items_in_order(root)
        return items[k - 1]

    # Smart way but poorly implemented (51 ms). T: O(k)?
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def _find_kth_smallest(root: TreeNode) -> None:
            nonlocal kth_value, curr_index

            if root.left:
                _find_kth_smallest(root.left)

            if curr_index == k and kth_value is None:
                kth_value = root.val
                return
            curr_index += 1

            if root.right:
                _find_kth_smallest(root.right)

        curr_index = 1
        kth_value = None
        _find_kth_smallest(root)

        return kth_value

    # Iterative solution
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            # ! Reach the smallest value while accumulating the nodes
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1

            if not k:
                return root.val

            root = root.right


def main():
    values = [5, 3, 6, 2, 4, None, None, 1]
    tree = build_tree_from_list(values)
    print(Solution().kthSmallest(
        root=tree,
        k=6
    ))


if __name__ == '__main__':
    main()
