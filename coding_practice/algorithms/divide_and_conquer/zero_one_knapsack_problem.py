import typing as t


"""
Zero One Knapsack Problem

Given the weights and profits of N items
Find the max profit within given capacity of C
Items cannot be broken (unlike the fractional knapsack problem)

Say, we have:
    Mango (weight: 3, profit: 31)
    Apple (weight: 1, profit: 26)
    Orange (weight: 2, profit: 17)
    Banana (weight: 5, profit: 72)
    
Subproblems:
- Pick 1 items + the remaining
- Skip 1 items + the remaining    
    i.e.
- option_1 = 31 + f(2, 3, 4), where 2,3,4 are indices and 31 is mango's profit
- option_2 = 0 + f(2, 3, 4)
  return max(option_1, option_2)

Base cases:
    - You ran out of fruits, i.e. index >= len(fruits)
    - You ran out of capacity
  

Tree structure again - instead of leaves you consider different combinations of
taking / not taking items at each iteration/index

Say capacity is 6

                            items, 2, 2 (take item)
                            
            items, 3, 1 (take item)
            
                            items, 3, 2 (dont take item)

items, 6, 0

                            items, 5, 2 (take item)
                            
            items, 6, 1 (dont take item)
  
                            items, 6, 2 (dont take item) 
"""


class Item:
    def __init__(self, name: str, profit: float, weight: float) -> None:
        self.name = name
        self.profit = profit
        self.weight = weight


def do_zero_knapsack(
    items: list[Item], capacity: float, index: int = 0
) -> float:
    if index >= len(items):
        return 0
    if capacity <= 0:
        return 0

    curr_item = items[index]
    curr_item_weight = curr_item.weight
    curr_item_value = curr_item.profit

    if curr_item_weight <= capacity:
        option_1 = curr_item_value + do_zero_knapsack(
            items, capacity - curr_item_weight, index + 1
        )
        option_2 = 0 + do_zero_knapsack(items, capacity, index + 1)
        return max(option_1, option_2)
    else:
        return 0  # + do_zero_knapsack(items, capacity, index + 1) why?


def main():
    items = [
        Item("Mango", 31, 3),
        Item("Apple", 26, 1),
        Item("Orange", 17, 2),
        Item("Banana", 72, 5)
    ]
    capacity = 3
    print(do_zero_knapsack(items, capacity))


if __name__ == '__main__':
    main()
