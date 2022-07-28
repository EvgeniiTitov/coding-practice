from typing import Optional

from coding_practice.utils import build_tree_from_list


"""
Summary:
    - My solution is dumb: for each node, find its kids. If both p and q are
      in the node's children - we cool, we found the LCA.
      
    - Smarter way: if both p and q are in the right subtree - consider only
      the right subtree. If both are to the left - the left. If thats not the
      case, it means we found a node for which p and q are to the left and right!
_______________________________________________________________________________

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) node 
of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor 
is defined between two nodes p and q as the lowest node in T that has both p 
and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant 
of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # My recursive solution - seems to be working locally, fails with a weird
    # error not related to the test cases on Leetcode. Wtf?
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':

        def _find_lca(
            root: Optional[TreeNode], p: TreeNode, q: TreeNode
        ):
            if not root:
                return

            left_kids = _find_lca(root.left, p, q) if root.left else []
            if not isinstance(left_kids, list):
                return left_kids

            right_kids = _find_lca(root.right, p, q) if root.right else []
            if not isinstance(right_kids, list):
                return right_kids

            children = left_kids + right_kids + [root.val]

            if p.val in children and q.val in children:
                return root.val
            else:
                return children

        return _find_lca(root, p, q)

    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':
        root_val = root.val
        p_val = p.val
        q_val = q.val

        if p_val > root_val and q_val > root_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < root_val and q_val < root_val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':
        from queue import Queue

        p_val = p.val
        q_val = q.val
        queue = Queue()
        queue.put(root)
        while queue.qsize():
            node = queue.get()
            node_val = node.val
            if node_val > p_val and node_val > q_val:
                queue.put(node.left)
            elif node_val < p_val and node_val < q_val:
                queue.put(node.right)
            else:
                return node

        # --- OR ---

        p_val = p.val
        q_val = q.val
        node = root
        while node:
            node_val = node.val
            if node_val > p_val and node_val > q_val:
                node = node.left
            elif node_val < p_val and node_val < q_val:
                node = node.right
            else:
                return node


def main():
    tree = build_tree_from_list(
        elements=[6,2,8,0,4,7,9,None,None,3,5]
    )
    print(Solution().lowestCommonAncestor(
        root=tree,
        p=TreeNode(0),
        q=TreeNode(4)
    ))


if __name__ == '__main__':
    main()
