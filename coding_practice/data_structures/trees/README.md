- #### Every node stores some data and has 2 reference: left and right
```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---
- #### Tree traversals:

```python
In order traversal:

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

OR

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    tree_vals = []
    def inorder(tree):
        if tree:
            inorder(tree.left)
            tree_vals.append(tree.val)
            inorder(tree.right)

    inorder(root)
    return tree_vals
```

```python
Pre order traversal:

def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    elements = []
    def _traverse_tree(root: Optional[TreeNode]) -> None:
        if root:
            elements.append(root.val)
            _traverse_tree(root.left)
            _traverse_tree(root.right)

    _traverse_tree(root)
    return elements
```

```python
Post order traversal:

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    elements = []
    def _traverse_tree(root: Optional[TreeNode]) -> None:
        if root:
            _traverse_tree(root.left)
            _traverse_tree(root.right)
            elements.append(root.val)

    _traverse_tree(root)
    return elements

OR iteratively:

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    elements = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            elements.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return elements[::-1]
```

---

- #### Searching BST

```python
def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    
    def _find_value_in_tree(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            return _find_value_in_tree(root.right, val)
        else:
            return _find_value_in_tree(root.left, val)

    return _find_value_in_tree(root, val)

OR iteratively:

def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    while root and root.val != val:
        root = root.left if root.val > val else root.right
    return root
```

---

- #### Inserting into BST

```python
def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    
    if root.val == val:
        return root
    
    if val > root.val:
        # insert into the right subtree
        root.right = self.insertIntoBST(root.right, val)
    else:
        # insert into the left subtree
        root.left = self.insertIntoBST(root.left, val)
    return root

OR iteratively:

def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    head = root
    while True:
        if root.val == val:
            return head
        elif val < root.val:
            if root.left:
                root = root.left
            else:
                root.left = TreeNode(val)
                return head
        else:
            if root.right:
                root = root.right
            else:
                root.right = TreeNode(val)
                return head
```

---

- #### Deleting from BST

```python
Finding successor and predecessor:

def find_successor(self, root: TreeNode) -> TreeNode:
    root = root.right
    while root.left:
        root = root.left
    return root.val

def find_predecessor(self, root: TreeNode) -> TreeNode:
    root = root.left
    while root.right:
        root = root.right
    return root.val
```

```python
Node deletion:

def deleteNode(self, root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
    # Base case
    if not root:
        return None

    # 1) First identify the node if any that must be deleted
    if value > root.val:
        root.right = self.deleteNode(root.right, value)
    elif value < root.val:
        root.left = self.deleteNode(root.left, value)
    # 2) Found the node, delete the current one
    else:
        # The node is a leaf
        if not root.left and not root.right:
            root = None
        elif root.right:
            # Find new value from the right - successor
            root.val = self._find_successor(root)
            # Delete the successor as we moved it up
            root.right = self.deleteNode(root.right, root.val)
        else:
            root.val = self._find_predecessor(root)
            root.left = self.deleteNode(root.left, root.val)

    # It is important to return the root when deleting a node in BST
    return root
```

---

- #### Symmetric tree

![alt text](../../../images/symtree1.jpg?raw=true)

The idea here is that each recursive call does not get a single node as we're used to,
but rather it gets 2 nodes from each left and right subtrees!

```python
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def _compare_trees(left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right:  # One of them is null
            return False
        return (
            left.val == right.val
            and _compare_trees(left.right, right.left)
            and _compare_trees(left.left, right.right)
        )

    return _compare_trees(root, root)

OR iteratively:

def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    from queue import Queue

    queue = Queue()
    queue.put(root)
    queue.put(root)
    while queue.qsize():
        node_1 = queue.get()
        node_2 = queue.get()
        if not node_1 and not node_2:
            continue
        if not node_1 or not node_2:
            return False
        if node_1.val != node_2.val:
            return False
        queue.put(node_1.left)
        queue.put(node_2.right)
        queue.put(node_1.right)
        queue.put(node_2.left)

    return True
```

---

- #### Tree depth

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    def _measure_tree_depth(node: TreeNode) -> int:
        depth = 1
        depth_left = _measure_tree_depth(node.left) if node.left else 0
        depth_right = _measure_tree_depth(node.right) if node.right else 0
        deepest_subtree = max(depth_left, depth_right)
        depth += deepest_subtree
        return depth
    return _measure_tree_depth(root)

OR shorter:

def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    else:
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1

OR iteratively:

def maxDepth(self, root: Optional[TreeNode]) -> int:
    stack = []
    if root:
        stack.append((1, root))

    max_depth = 0
    while len(stack):
        current_depth, root = stack.pop()
        if root:
            max_depth = max(max_depth, current_depth)
            stack.append((current_depth + 1, root.left))
            stack.append((current_depth + 1, root.right))

    return max_depth
```

---

- #### Invert a tree

An inverted form of a Binary Tree is another Binary Tree with left and right 
children of all non-leaf nodes interchanged. You may also call it the mirror 
of the input tree.

![alt text](../../../images/invert-binary-tree.png?raw=true)

```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    left = self.invertTree(root.left)
    right = self.invertTree(root.right)
    root.left = right
    root.right = left
    return root

OR iteratively:

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    from queue import Queue
    queue = Queue()
    queue.put(root)
    while queue.qsize():
        node = queue.get()
        node_left, node_right = node.left, node.right
        node.left = node_right
        node.right = node_left
        if node_left:
            queue.put(node_left)
        if node_right:
            queue.put(node_right)
    return root
```

---

- #### Tree diameter

The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.

![alt text](../../../images/btree_diameter.png?raw=true)

```python
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    diameter = 0

    def _measure_diameter(root: Optional[TreeNode]) -> int:
        nonlocal diameter
        right_diameter = _measure_diameter(root.right) if root.right else 0
        left_diameter = _measure_diameter(root.left) if root.left else 0
        diameter = max(diameter, right_diameter + left_diameter)

        # Return the larger branch + current node
        return max(left_diameter, right_diameter) + 1

    _measure_diameter(root)
    return diameter
```

---

- #### Tree sum / sum within range

Calculate the sum of values of all nodes with a value in the inclusive range
```python
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
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

OR iteratively:

def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    sum_ = 0
    stack = [root]
    while len(stack):
        root = stack.pop()
        if not root:
            continue
        current = root.val
        if low <= current <= high:
            sum_ += current
        if low < current:
            stack.append(root.left)
        if current < high:
            stack.append(root.right)
    return sum_
```

---

- Height balanced tree

A binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Balanced tree             |  Imbalanced tree
:-------------------------:|:-------------------------:
![](../../../images/balanced_tree.jpg?raw=true)  |  ![](../../../images/inbalanced_tree.jpg?raw=true)

```python
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    return self._is_balanced(root)[0]

def _is_balanced(self, root: Optional[TreeNode]) -> tuple:
    if not root:
        return True, 0

    is_left_balanced, left_depth = self._is_balanced(root.left)
    is_right_balanced, right_depth = self._is_balanced(root.right)

    current_height = 1 + max(left_depth, right_depth)

    # If left or right is imbalanced -> whole tree is imbalanced
    if not is_left_balanced or not is_right_balanced:
        return False, current_height

    # Left and right could be balanced, but of different heights
    if abs(left_depth - right_depth) > 1:
        return False, current_height
    
    # Subtrees are balanced and their height diff <= 1
    return True, current_height
```

--- 

- Lowest Common Ancestor (LCA) in BST

LCA - The lowest common ancestor is defined between two nodes p and q as the 
lowest node in T that has both p and q as descendants (where we allow a node 
to be a descendant of itself).

There are a dumb and a smart way to do it:

1. Find kids of all nodes, and if there is a node for which p and q are the kids,
we found the LCA.

2. Smart say is to find a node for which p and q are to the left and right!

```python
# Recursive
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

# Iterative
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
```