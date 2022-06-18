import typing as t
import random

'''
Binary tree - every node has at most 2 child nodes.

Binary Search Tree (BST) - special case of a binary tree where elements have
some special order. Say, child on the left has value < whereas child on the
right >. No duplicates, elements are always unique. Good for searching O(log n)

When searching a BST, there are 2 ways:
    - Breadth first search
    - Depth first search
        - In order traversal
            First visit left subtree
        - Pre order traversal
        - Post order traversal

Could be used to implement a set like data structure (duplicates are discarded)
Could be used to sort an array of numbers
'''

random.seed(0)


class BinarySearchTreeNode:
    def __init__(self, data: t.Any) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data: t.Any) -> None:
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self) -> t.List[t.Any]:
        """
        ! NOTE: Returns elements in ascending order
        """
        elements = []
        if self.left:
            elements.extend(self.left.in_order_traversal())
        elements.append(self.data)
        if self.right:
            elements.extend(self.right.in_order_traversal())
        return elements

    def pre_order_traversal(self) -> t.List[t.Any]:
        elements = [self.data]
        if self.left:
            elements.extend(self.left.pre_order_traversal())
        if self.right:
            elements.extend(self.right.pre_order_traversal())
        return elements

    def post_order_traversal(self) -> t.List[t.Any]:
        elements = []
        if self.left:
            elements.extend(self.left.post_order_traversal())
        if self.right:
            elements.extend(self.right.post_order_traversal())
        elements.append(self.data)
        return elements

    def search(self, value: t.Any) -> bool:
        if value == self.data:
            return True
        elif value > self.data:
            if not self.right:
                return False
            else:
                return self.right.search(value)
        else:
            if not self.left:
                return False
            else:
                return self.left.search(value)

    def find_min(self) -> int:
        if not self.left:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self) -> int:
        if not self.right:
            return self.data
        else:
            return self.right.find_max()

    def calculate_sum(self) -> int:
        if not self.left and not self.right:
            return self.data
        # return sum(self.in_order_traversal())  # That's cheeky
        left_subtree = self.left.calculate_sum() if self.left else 0
        right_subtree = self.right.calculate_sum() if self.right else 0
        return left_subtree + self.data + right_subtree

    def delete(self, value: t.Any) -> t.Optional["BinarySearchTreeNode"]:
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
            # If there's no left, no worries, this value is not in the tree
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if not self.left and not self.right:
                return
            elif not self.left:
                return self.right
            elif not self.right:
                return self.left

            # Min from the right
            min_value_right = self.right.find_min()
            self.data = min_value_right
            self.right = self.right.delete(min_value_right)

            # Max from the left
            # TODO:

        return self

    def print_tree(self, indentation: int = 0) -> None:
        if self.right:
            self.right.print_tree(indentation + 1)
        print(f"\n{'    ' * indentation} {self.data}")
        if self.left:
            self.left.print_tree(indentation + 1)


def build_tree(elements: t.Sequence[t.Any]) -> BinarySearchTreeNode:
    root = BinarySearchTreeNode(elements[0])
    for element in elements[1:]:
        root.add_child(element)
    return root


def main():
    numbers = [random.randint(0, 100) for _ in range(10)]
    print("Numbers:", numbers)
    tree = build_tree(numbers)

    print("\nIn order traversal")
    print(tree.in_order_traversal())

    print("\nPre order traversal")
    print(tree.pre_order_traversal())

    print("\nPost order traversal")
    print(tree.post_order_traversal())

    print(f"\nSearching for {100}. Is found: {tree.search(100)}")
    print(f"Searching for {228}. Is found: {tree.search(228)}")

    print("\nThe tree sum:", tree.calculate_sum(), sum(numbers))

    print("\nThe min value:", tree.find_min(), min(numbers))
    print("The max value:", tree.find_max(), max(numbers))

    print("\n\nPrinting the tree:")
    tree.print_tree()

    print(f"\nDeleting the number {97}")
    tree.delete(97)

    print("\n\nPrinting the tree after deleting the item")
    tree.print_tree()


if __name__ == '__main__':
    main()
