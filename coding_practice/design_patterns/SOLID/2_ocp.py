import typing as t
from enum import Enum, auto


"""
ProductFilterer IS BAD, WE COULD KEEP ADDING NEW FILTERING FUNCTIONS
"""


class Color(Enum):
    RED = auto()
    GREEN = auto()
    WHITE = auto()


class Size(Enum):
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def __str__(self):
        return f"Product: {self.name} {self.color} {self.size}"


class ProductFilterer:
    @staticmethod
    def filter_by_color(products: t.Sequence[Product], color):
        for p in products:
            if p.color == color:
                yield p

    @staticmethod
    def filter_by_size(products: t.Sequence[Product], size):
        for p in products:
            if p.size == size:
                yield p

    # THIS DOES NOT SCALE


def main():
    product_1 = Product("fork", Color.WHITE, Size.MEDIUM)
    product_2 = Product("knife", Color.WHITE, Size.MEDIUM)

    for product in ProductFilterer.filter_by_color(
        (product_2, product_1), Color.WHITE
    ):
        print(product)


if __name__ == "__main__":
    main()
