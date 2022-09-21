from typing import List


"""
Summary:
    Brute force: Just generate all combinations of correct length (n) and pick
    those ones that add up to the target k.
    
    Backtracking: you pick the first number, say 1. Then, you need k - 1 more 
    elements for your curr_combination. The sum for the remaining k - 1 elements 
    is n - first element in curr_combination. 
    For the second element we have many choices, say we pick 2. It is not a 
    duplicate of 1 AND length of the current combination < n AND it doesn't
    exceed the desired sum (n - first element). For the last digit we have a 
    concrete constraint in terms of its value: n - first item - second item !
    
    ^ IMPORTANT: This reminds the two sum problem. We pick elements which adds 
    constraints to what could be picked later!
    
    We try to fill the combination one element at every step. Each choice we make
    at certain step might lead us to a final valid solution, if not, we simply
    backtrack/revisit our previous choice and try again. 
    
    To make sure there are no duplicates within one combination and no duplicated
    combinations, treating available numbers as a list [1, 2, 3, 4, 5, 6, 7, 8, 9]
    helps a lot. Once we've picked a number, say, 6, we do not consider anything
    to the left. 
_______________________________________________________________________________

https://leetcode.com/problems/combination-sum-iii/

Find all valid combinations of k numbers that sum up to n such that the 
following conditions are true:

- Only numbers 1 through 9 are used.
- Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain 
the same combination twice, and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 
1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
"""


class Solution:

    # Brute force (~ 60ms) - still passes all tests
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        target = n

        def _generate_combinations(
            curr_index: int,
            curr_combination: List[int],
            combinations: List[List[int]]
        ) -> None:
            # Base cases
            sum_ = sum(curr_combination)
            if sum_ == target and len(curr_combination) == k:
                combinations.append(curr_combination.copy())
            # Overshoot
            elif sum_ > target or len(curr_combination) >= k:
                return

            # ! Start from curr + 1 as the same number can't be reused twice
            for i in range(curr_index + 1, numbers_length):
                curr_combination.append(numbers[i])
                _generate_combinations(i, curr_combination, combinations)
                curr_combination.pop()

        numbers = list(range(1, 10))
        numbers_length = len(numbers)
        combinations = []
        _generate_combinations(-1, [], combinations)
        return combinations

    # Backtracking (~ 40ms)
    # This solution is almost identical to ^. We avoid calculating sum() though
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def _generate_combinations(
            remaining_target: int,
            curr_index: int,
            curr_combination: List[int],
            combinations: List[List[int]]
        ) -> None:
            # Base case
            if remaining_target == 0 and len(curr_combination) == k:
                combinations.append(curr_combination.copy())
                return
            # Got max N of elements in curr combination, can't go further
            elif remaining_target != 0 and len(curr_combination) == k:
                return

            for i in range(curr_index + 1, numbers_length):
                curr_combination.append(numbers[i])
                _generate_combinations(
                    remaining_target=remaining_target - numbers[i],
                    curr_index=i,
                    curr_combination=curr_combination,
                    combinations=combinations
                )
                curr_combination.pop()

        numbers = list(range(1, 10))
        numbers_length = len(numbers)
        combinations = []
        _generate_combinations(n, -1, [], combinations)
        return combinations


def main():
    print(Solution().combinationSum3(
        k=3,
        n=9
    ))


if __name__ == '__main__':
    main()
