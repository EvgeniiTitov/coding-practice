from coding_practice.utils import times_called


"""
Given N number of houses along the street with some amount of money in each
You want to rob them to steal as much money as you can
However, adjacent houses cannot be robbed as it will trigger the alarm

Houses and money: A(6) B(7) C(1) D(30) E(8) F(2) G(4)

The constraint here is: adjacent houses cannot be robbed

^ That's a complex problem to solve head on as it involves a bunch of different
options. Let's break it down into smaller problems.

Potential solution could be:
BDG = 7 + 30 + 4 = 41

We could either pick the very first house or skip it:
Option1 = A + f(5), where f(5) is the remaining 5 houses (CDEFG)
Option2 = 0 + f(6), where f(6) is BCDEFG - we didn't rob the first house
res = max(Option1, Option2)

All of these reminds me of how I work with trees - you have some base cases
such as not root, and then you do something for, say, left and right subtrees. 
We could pick the max() of the returned recursive calls or whatever. The point
is when it comes to array, it is similar. Each *iteration* you can either
skip or steal (imagine a tree growing down). At some point you reach your base
case - out of bounds, so your recursive calls start shutting down.

It all comes down to identifying how to break the problem down into subproblems
and the base case(s). 
"""


@times_called
def rob_houses(houses: list[int], curr_index: int) -> int:
    # Base case - out of bounds
    if curr_index >= len(houses):
        return 0

    # Have 2 options, steal from the 1st house or skip it
    steal_1st = houses[curr_index] + rob_houses(houses, curr_index + 2)
    skip_1st = rob_houses(houses, curr_index + 1)
    return max(steal_1st, skip_1st)


def main():
    print(rob_houses([6, 7, 1, 30, 8, 2, 4], 0))


if __name__ == "__main__":
    main()
