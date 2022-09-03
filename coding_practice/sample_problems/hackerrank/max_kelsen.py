import string


def numbers_to_letters(s: str) -> str:
    indices = range(1, 27)
    letters = [chr(i) for i in range(65, 91)]
    number_char_mapping = dict(zip(indices, letters))

    words = s.split("+")
    out = []
    for word in words:
        current_word = []
        word_chars = word.split(" ")
        for word_char in word_chars:
            current_word.append(number_char_mapping[int(word_char)])
        out.append("".join(current_word))

    return " ".join(out)

# -----------------------------------------------------------------------------

class LanguageStudent:
    def __init__(self) -> None:
        self.languages = []

    def add_language(self, language: str) -> None:
        self.languages.append(language)


class LanguageTeacher(LanguageStudent):
    def __init__(self):
        super().__init__()

    def teach(self, student: LanguageStudent, language: str) -> bool:
        if language in self.languages:
            # Student might already know the language
            if language not in student.languages:
                student.languages.append(language)
            return True
        else:
            return False

# -----------------------------------------------------------------------------

from typing import Any, Optional, List


class TreeNode:
    def __init__(
        self,
        value: Any,
        parent: Optional["TreeNode"] = None,
        children: Optional[List["TreeNode"]] = None
    ) -> None:
        self.value = value
        self.parent = parent
        self.children = children or []


class CategoryTree:

    def __init__(self):
        self._categories = dict()

    def add_category(self, category: str, parent: Optional[str]) -> None:
        if not parent:
            # If adding a category that already exists
            if category in self._categories:
                raise KeyError
            category_tree = TreeNode(category)
            self._categories[category] = category_tree
        else:
            parent_node = self._categories[parent]  # What if down in the tree?
            child_node = TreeNode(category, parent=parent_node)
            parent_node.children.append(child_node)

    def get_children(self, parent: str) -> List[str]:
        parent_node = self._categories[parent]
        out = []
        for child in parent_node.children:
            out.append(child.value)
        return out


class CategoryTree:

    def __init__(self):
        self._root = TreeNode(None)
        self._categories = dict()

    def add_category(self, category: str, parent: Optional[str]) -> None:
        if not parent:
            if category in self._root.children:
                raise KeyError
            category_tree = TreeNode(category, parent=self._root)
            self._root.children.append(category_tree)
            self._categories[category] = category_tree
        else:
            category_root = self._categories[category]
            child_node = TreeNode(category, parent=category_root)
            category_root.children.append(child_node)

    def get_children(self, parent: str) -> List[str]:
        parent_node = self._categories[parent]
        out = []
        for child in parent_node.children:
            out.append(child.value)
        return out


# -----------------------------------------------------------------------------
# Just keep track of nodes and their kids. Then get the number of all nodes
# with children kekl
def count_internal_nodes(tree):
    tree_dict = dict()
    for child, parent in enumerate(tree):
        if parent == -1:
            continue

        if parent not in tree_dict:
            tree_dict[parent] = [child]
        else:
            tree_dict[parent].append(child)

    internal_nodes = 0
    for parent, child in tree_dict.items():
        if len(child):
            internal_nodes += 1

    return internal_nodes


if __name__ == "__main__":
    # print(numbers_to_letters('20 5 19 20+4 15 13 5'))

    # ----

    # teacher = LanguageTeacher()
    # teacher.add_language("English")
    #
    # student = LanguageStudent()
    # print(teacher.teach(student, "English"))
    #
    # print(student.languages)

    # ----

    # c = CategoryTree()
    # c.add_category('A', None)
    # c.add_category('B', 'A')
    # c.add_category('C', 'A')
    # print(','.join(c.get_children('A') or []))

    # ---

    tree = [1, 3, 1, -1, 3]
    print(count_internal_nodes(tree))  # should print 2