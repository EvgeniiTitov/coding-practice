from typing import Optional, List

from coding_practice.utils import build_tree_from_list, print_tree_inorder


"""
Summary: BFS approach top-down left-right using a queue and an entity 
representing the end of a level.
_______________________________________________________________________________

https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes'
values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from queue import Queue
        LEVEL_END = "end"

        if not root:
            return []
        if root and not root.left and not root.right:
            return [[root.val]]

        queue = Queue()
        queue.put(root)
        queue.put(LEVEL_END)
        out = []
        current_level = []
        while queue.qsize():
            item = queue.get()

            if item == LEVEL_END and not queue.qsize():
                break
            elif item == LEVEL_END:
                queue.put(LEVEL_END)
                out.append(current_level)
                current_level = []
                continue

            current_level.append(item.val)

            if item.left:
                queue.put(item.left)
            if item.right:
                queue.put(item.right)

        if len(current_level):
            out.append(current_level)

        return out


def main():
    tree = build_tree_from_list(
        elements=[3,9,20,None,None,15,7]
    )
    print(Solution().levelOrder(tree))


if __name__ == '__main__':
    main()
