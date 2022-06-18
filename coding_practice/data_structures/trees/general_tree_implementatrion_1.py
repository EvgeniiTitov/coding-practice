import typing as t


"""
stdout:
 Electronics
    Laptop
       Mac
       Surface
       Thinkpad
    Cell Phone
       iPhone
       Google Pixel
       vivo
    TV
       Samsung
       LG
"""


class TreeNode:
    def __init__(self, value: t.Any) -> None:
        self.data = value
        self.children: t.List[TreeNode] = []
        self.parent = None

    def add_child(self, child: "TreeNode") -> None:
        child.parent = self
        self.children.append(child)

    def print_tree(self, indentation: int = 0) -> None:
        """
        Could calculate Node's level by going up and using it for indentation
        p = self.parent
        level = 0
        while p:
            level += 1
            p.parent
        """
        print("   " * indentation, self.data)
        if len(self.children):
            for child in self.children:
                child.print_tree(indentation + 1)

    def __str__(self) -> str:
        return f"TreeNode value: {self.data}"


def add_items_as_children(
    root: TreeNode, children_values: t.Sequence[t.Any]
) -> None:
    for children_value in children_values:
        root.add_child(TreeNode(children_value))


def main():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    add_items_as_children(laptop, ("Mac", "Surface", "Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    add_items_as_children(cellphone, ("iPhone", "Google Pixel", "vivo"))

    tv = TreeNode("TV")
    add_items_as_children(tv, ("Samsung", "LG"))

    for child in (laptop, cellphone, tv):
        root.add_child(child)

    root.print_tree()


if __name__ == "__main__":
    main()
