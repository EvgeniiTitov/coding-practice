import typing as t

"""
TODO: TBA - reimplement the interview question. I used dict instead of set?

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


def main():
    numbers = [2, 1, 5, 7, -1, 4, 1, 4, 1]
    target = 6
    print(find_pairs(numbers, target))


if __name__ == "__main__":
    main()
