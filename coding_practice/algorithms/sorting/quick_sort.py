import random


random.seed(123)


# TODO: Add in-place implementation
# https://stackoverflow.com/questions/18262306/quicksort-with-python


def quicksort_array(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    smaller = [element for element in arr if element < pivot]
    greater = [element for element in arr if element > pivot]
    return quicksort_array(smaller) + [pivot] + quicksort_array(greater)


def main():
    arr = [random.randint(0, 100) for _ in range(20)]
    print("Array:", arr)
    print("Sorted array:", quicksort_array(arr))


if __name__ == "__main__":
    main()
