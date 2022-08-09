import random


random.seed(0)


"""
Merge Sort

D&C - divide the input array in two halves and keep halving recursively until
they become too small, i.e. len(arr) == 1, so it cannot be further divided

Merge halves by sorting them.

_______________________________________________________________________________

Say, we have an array: 6 4 3 7 5 1 2

Start breaking it down into subarray until the base case is met (len == 1)

6 4 3 7  |  5 1 2

6 4  |  3 7  |  5 1  |  2

6  |  4  |  3  |  7  |  5  |  1  |  2  - at this point we cannot divide further

Start merging them the way we divided it. When merging sort the subarray:

4 6  |  3 7  |  1 5   |  2

3 4 6 7  |  1 2 5

1 2 3 4 5 6 7

"""


def _merge(array: list[int], left: int, middle: int, right: int) -> None:
    nb_elements_left = middle - left + 1
    nb_element_right = right - middle  # +1?

    left_subarray = [0] * nb_elements_left
    right_subarray = [0] * nb_element_right

    # Copy elements to the appropriate sub arrays
    for i in range(nb_elements_left):
        left_subarray[i] = array[i]

    for i in range(nb_element_right):
        right_subarray[i] = array[middle + 1 + i]

    # Merge temporary arrays into the passed array, same logic as merging 2 LLs
    i = 0  # Initial index left subarray
    j = 0  # Initial index of right subarray
    k = left
    while i < nb_elements_left and j < nb_element_right:
        if left_subarray[i] <= right_subarray[j]:
            array[k] = left_subarray[i]
            i += 1
        else:
            array[k] = right_subarray[j]
            j += 1
        k += 1

    # Check if any elements left and append to the array
    while i < nb_elements_left:
        array[k] = left_subarray[i]
        i += 1
        k += 1

    while j < nb_element_right:
        array[k] = right_subarray[j]
        j += 1
        k += 1


def merge_sort(array: list[int], left: int, right: int) -> None:
    if left < right:
        middle = (left + right) // 2
        merge_sort(array, left, middle)
        merge_sort(array, left + 1, right)
        _merge(array, left, middle, right)


def main():
    # TODO: Doesn't work

    array = [random.randint(0, 100) for _ in range(20)]
    print("Array:", array)
    merge_sort(array, 0, len(array) - 1)
    print("Sorted array:", array)


if __name__ == "__main__":
    main()
