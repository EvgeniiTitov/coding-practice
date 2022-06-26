import typing as t


"""
Summary: Single pass only, calculate complement, check if its available / seen,
append to a sequence storing only unique items (sets, dicts)
------------------------------------------------------------------------------

Given a list and a target. Return unique pairs of numbers that add up to the
target
"""


def find_pairs(nums: list[int], target: int) -> list[tuple[int, int]]:
    pairs = set()
    unique_nums = set(nums)
    for number in nums:
        complement = target - number
        if complement not in unique_nums:
            continue
        pair = (number, complement)
        if pair not in pairs and (complement, number) not in pairs:
            pairs.add(pair)
    return [pair for pair in pairs]


# Similar question - return the N of unique pairs
def find_n_pairs(nums: list[int], target: int) -> int:
    pairs, complements = set(), set()
    for num in nums:
        complement = target - num
        if complement in complements:
            pair = (
                (num, complement) if num >= complement else (complement, num)
            )
            if pair not in pairs:
                pairs.add(pair)
        complements.add(num)
    return len(pairs)


def main():
    numbers = [2, 1, 5, 7, -1, 4, 1, 4, 1, 3, 2, 1, 54, 8, 100, -94]
    target = 6
    print(find_pairs(numbers, target))
    print(find_n_pairs(numbers, target))


if __name__ == "__main__":
    main()
