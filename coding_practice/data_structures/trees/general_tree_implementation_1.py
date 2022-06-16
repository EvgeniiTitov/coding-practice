import typing as t


'''
TBC
'''


class Tree:

    def __init__(self, value: t.Optional[t.Any] = None) -> None:
        self.value = value
        self._children: list[Tree] = []

    def set_children(self, children: "list[Tree]") -> None:
        if not self.value:
            return
        self._children = children


def main() -> None:
    pass


if __name__ == '__main__':
    main()
