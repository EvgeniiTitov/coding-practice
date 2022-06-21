import random
import typing as t

from coding_practice.utils import timer


def selection_sort(arr: list[int]) -> None:
    '''
    Could be slightly optimized to avoid unnecessary swaps
    for i in range(len(my_list)):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    '''
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


def merge_sort(arr: list[int]) -> None:
    # TODO: Complete me
    pass


ALGORITHMS = {
    "selection_sort": selection_sort,
}


@timer
def time_sorting_algorithm(
    algorithm: t.Literal["brute_force"],
    array: list[int]
) -> None:
    ALGORITHMS[algorithm](array)


def main():
    array = [random.randint(0, 100) for _ in range(5_000)]
    time_sorting_algorithm("selection_sort", array)


if __name__ == '__main__':
    main()
