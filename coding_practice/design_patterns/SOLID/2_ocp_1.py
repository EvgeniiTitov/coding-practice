import abc
import typing as t
from enum import Enum, auto


T = t.TypeVar("T")


class Color(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()


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


# -----------------------------------------------------------------------------
class BaseSpecification(abc.ABC):

    @abc.abstractmethod
    def is_satisfied(self, item) -> bool:
        ...


class BaseFilter(abc.ABC):

    @abc.abstractmethod
    def filter(
            self, items: t.Sequence[T], spec: BaseSpecification
    ) -> t.Iterator[T]:
        ...
# -----------------------------------------------------------------------------
# Interface implementations are different, and yet they are polymorphic


class ColorSpecification(BaseSpecification):

    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item: Product) -> bool:
        return self.color == item.color


class SizeSpecification(BaseSpecification):

    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item: Product) -> bool:
        return self.size == item.size


class ANDSpecification(BaseSpecification):

    def __init__(self, *specs):
        self.specs = specs

    def is_satisfied(self, item) -> bool:
        return all(
            [step.is_satisfied(item) for step in self.specs]
        )


class Filter(BaseFilter):

    def filter(
            self, items: t.Sequence[T], spec: BaseSpecification
    ) -> t.Iterator[T]:
        for item in items:
            if spec.is_satisfied(item):
                yield item


def main():
    products = [
        Product("apple", Color.GREEN, Size.SMALL),
        Product("zucchini", Color.GREEN, Size.MEDIUM),
        Product("melon", Color.YELLOW, Size.MEDIUM),
        Product("watermelon", Color.RED, Size.LARGE)
    ]
    color_spec = ColorSpecification(Color.GREEN)
    size_spec = SizeSpecification(Size.MEDIUM)
    custom_filter = Filter()

    print("Green products:")
    for product in custom_filter.filter(products, color_spec):
        print(product)

    print("\nMedium size products:")
    for product in custom_filter.filter(products, size_spec):
        print(product)

    print("\nGreen and medium size products:")
    and_spec = ANDSpecification(color_spec, size_spec)
    for product in custom_filter.filter(products, and_spec):
        print(product)


if __name__ == '__main__':
    main()
