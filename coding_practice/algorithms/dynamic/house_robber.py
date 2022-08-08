import typing as t

from coding_practice.utils import times_called


"""
Given N number of houses along the street with some amount of money in each
You want to rob them to steal as much money as you can
However, adjacent houses cannot be robbed as it will trigger the alarm

6 7 1 30 8 2 4

The problem follows the overlapping subproblem property (draw the tree), so
could be solved using DP.


"""


Cache = t.MutableMapping[int, int]


@times_called
def rob_houses_raw(houses: list[int], curr_index: int) -> int:
    # Base case - out of bounds
    if curr_index >= len(houses):
        return 0

    # Have 2 options, steal from the 1st house or skip it
    steal_1st = houses[curr_index] + rob_houses_raw(houses, curr_index + 2)
    skip_1st = rob_houses_raw(houses, curr_index + 1)
    return max(steal_1st, skip_1st)


@times_called
def rob_houses(houses: list[int], curr_index: int, cache: Cache) -> int:
    # Base case - out of bounds
    if curr_index >= len(houses):
        return 0

    # Have 2 options, steal from the 1st house or skip it
    if curr_index not in cache:
        cache[curr_index] = max(
            houses[curr_index] + rob_houses(houses, curr_index + 2, cache),
            rob_houses(houses, curr_index + 1, cache)
        )
    return cache[curr_index]


@times_called
def rob_houses_bottom_up(houses: list[int]) -> int:
    steals = [0] * (len(houses) + 2)
    for i in range(len(houses) - 1, -1, -1):
        steals[i] = max(houses[i] + steals[i + 2], steals[i + 1])
    return steals[0]


def main():
    print(rob_houses_raw([6, 7, 1, 30, 8, 2, 4], 0))

    print(rob_houses([6, 7, 1, 30, 8, 2, 4], 0, {}))

    print(rob_houses_bottom_up([6, 7, 1, 30, 8, 2, 4]))


if __name__ == '__main__':
    main()
