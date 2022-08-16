from typing import Optional, List

from coding_practice.utils import build_tree_from_list


"""
Summary: create a container to keep track of all paths (pass to recursive calls
or abuse closure). Keep recursively going down aggregating the possible paths.
When you reached the node that has no kids, done, append the path to the 
container. The recursive calls do not return anything, we're just finding all
possible paths
_______________________________________________________________________________

https://leetcode.com/problems/binary-tree-paths/

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # T: O(N) - each node is visited once; S: O(N)
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def _find_paths(root: TreeNode, curr_path: str):
            if curr_path:
                curr_path += f"->{root.val}"
            else:
                curr_path = f"{root.val}"

            # If reached the leaf node, save the constructed path
            if not root.left and not root.right:
                paths.append(curr_path)

            if root.left:
                _find_paths(root.left, curr_path)
            if root.right:
                _find_paths(root.right, curr_path)

        if not root:
            return [""]
        elif root and not root.left and not root.right:
            return [str(root.val)]

        paths = []
        _find_paths(root, "")

        return paths

    # Same ^ but passing paths container as a parameter to avoid abusing closures
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def _find_paths(root: TreeNode, curr_path: str, paths: List[str]):
            if curr_path:
                curr_path += f"->{root.val}"
            else:
                curr_path = f"{root.val}"

            # If reached the leaf node, save the constructed path
            if not root.left and not root.right:
                paths.append(curr_path)

            if root.left:
                _find_paths(root.left, curr_path, paths)
            if root.right:
                _find_paths(root.right, curr_path, paths)

        if not root:
            return [""]
        elif root and not root.left and not root.right:
            return [str(root.val)]

        paths = []
        _find_paths(root, "", paths)

        return paths

    # Iterative solution
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:
                paths.append(path)

            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))

            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return paths


def main():
    tree = build_tree_from_list(
        elements=[1, 2, 3, None, 5]
    )
    print(Solution().binaryTreePaths(tree))


if __name__ == '__main__':
    main()
