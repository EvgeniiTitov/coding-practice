

"""
Given total amount of money and coins of different denominations. Find the min
number of coins required to make up the given amount.

A good example of a greedy algorithm where each iteration we try to find the
best local solution, which will lead to the best global solution.
"""


def get_coins(amount: int, coins: list[int]) -> list[int]:
    if amount == 0:
        return []

    coins.sort()
    coins_required = []
    current_denomination_idx = len(coins) - 1
    while amount:
        try:
            current_denomination = coins[current_denomination_idx]
        except IndexError:
            print("Ran out of coins, cannot match the amount required")
            raise

        if amount >= current_denomination:
            coins_required.append(current_denomination)
            amount -= current_denomination
        else:
            current_denomination_idx -= 1

    return coins_required


def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 1000]
    amount = 1239

    print(get_coins(amount, coins))


if __name__ == '__main__':
    main()
