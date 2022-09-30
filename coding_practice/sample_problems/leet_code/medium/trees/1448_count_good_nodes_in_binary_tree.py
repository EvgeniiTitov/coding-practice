from coding_practice.utils import build_tree_from_list


"""
Summary:
    Iterate over the tree (BFS/DFS) while keeping track of the current path to
    each node / current largest encountered on the path to each node!
_______________________________________________________________________________

https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Given a binary tree root, a node X in the tree is named good if in the path 
from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Iterative. T: O(N) - visit every node once
    def goodNodes(self, root: TreeNode) -> int:
        from queue import Queue

        if not root.left and not root.right:
            return 1

        good_nodes_count = 1
        queue = Queue()
        if root.left:
            queue.put((root.left, [root.val]))
        if root.right:
            queue.put((root.right, [root.val]))
        while queue.qsize():
            node, path_to_node = queue.get()
            node_val = node.val
            largest_seen = max(path_to_node)  # O(N) --> TODO: just max value

            if node_val >= largest_seen:
                good_nodes_count += 1
                path_to_node = path_to_node + [node_val]
            else:
                path_to_node = path_to_node.copy()

            if node.left:
                queue.put((node.left, path_to_node))
            if node.right:
                queue.put((node.right, path_to_node))

        return good_nodes_count

    # Iterative. T: O(N) - visit every node once
    # Better S complexity: O(N) - if tree is full, last lvl contains N/2 nodes
    def goodNodes(self, root: TreeNode) -> int:
        from queue import Queue

        queue = Queue()
        queue.put((root, float("-inf")))
        good_nodes_count = 0
        while queue.qsize():
            node, previous_max = queue.get()
            if node.val >= previous_max:
                good_nodes_count += 1

            previous_max = max(previous_max, node.val)
            if node.left:
                queue.put((node.left, previous_max))
            if node.right:
                queue.put((node.right, previous_max))

        return good_nodes_count

    # Recursive. T: O(N); S: O(N)
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):
            nonlocal num_good_nodes
            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.right:
                dfs(node.right, max(node.val, max_so_far))
            if node.left:
                dfs(node.left, max(node.val, max_so_far))

        num_good_nodes = 0
        dfs(root, float("-inf"))
        return num_good_nodes


def main():
    # tree_root = build_tree_from_list([3, 1, 4, 3, None, 1, 5])
    # tree_root = build_tree_from_list([3, 3, None, 4, 2])
    # tree_root = build_tree_from_list([2, None, 4, 10, 8, None, None, 4])
    tree_root = build_tree_from_list([9, None, 3, 6])
    print(Solution().goodNodes(root=tree_root))


if __name__ == '__main__':
    main()
