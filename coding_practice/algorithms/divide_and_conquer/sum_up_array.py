import typing as t


def sum_up_array(arr: t.Sequence[int]) -> int:
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_up_array(arr[1:])


def main():
    arr = list(range(10))
    print(sum_up_array(arr))
    print(sum(arr))


if __name__ == '__main__':
    main()
