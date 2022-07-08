from coding_practice.utils import timer


# O(n)
def linear_search(array: list[int], target: int) -> bool:
    for item in array:
        if item == target:
            return True
    return False


# O(log n) if array is sorted
def binary_search(array: list[int], target: int) -> bool:
    left, right = 0, len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return True
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return False


@timer
def time_searching_algorithms(array: list[int], target: int) -> None:
    # linear_search(array, target)  # 100M; 3.65 sec work mac
    print(binary_search(array, target))  # 100M; 1.87e-05 sec work mac


def main():
    l = list(range(100_000_000))
    time_searching_algorithms(l, l[-1])


if __name__ == "__main__":
    main()
