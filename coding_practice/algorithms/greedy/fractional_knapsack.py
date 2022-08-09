class Item:
    def __init__(self, weight: float, value: float) -> None:
        if weight == 0.0:
            raise ValueError("Weight must be positive")
        self.weight = weight
        self.value = value

    @property
    def density(self) -> float:
        return self.value / self.weight


def get_item_ratios(items: list[Item], capacity: float) -> float:
    items.sort(key=lambda item: item.density, reverse=True)

    used_capacity = 0
    total_value = 0
    for item in items:
        if used_capacity + item.weight <= capacity:
            used_capacity += item.weight
            total_value += item.value
        else:
            # Can only take a fraction of the next most valuable item
            remaining_capacity = capacity - used_capacity
            used_capacity += remaining_capacity
            total_value += remaining_capacity * item.density

        if used_capacity == capacity:
            break

    return total_value


def main():
    items = [
        Item(weight=20, value=100),
        Item(weight=30, value=120),
        Item(weight=10, value=60),
    ]
    capacity = 50
    print(get_item_ratios(items, capacity))


if __name__ == "__main__":
    main()
