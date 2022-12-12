from typing import List


"""
Summary: 
    Similar to 39, but we can have duplicated numbers in candidates. 
    
    Backtracking: Sorting candidates allows to group the same numbers together,
        so we could skip them to avoid generating the same combinations. The
        rest is your typical backtracking - base cases + probing the space for
        the solutions. 
_______________________________________________________________________________

https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""


class Solution:

    # Here you avoid generating duplicates by writing a smart algorithm, which
    # doesn't generate them
    # T: O(N ^ 2); S: O(N)
    def combinationSum2(
        self,
        candidates: List[int],
        target: int
    ) -> List[List[int]]:

        def _generate_combinations(
            curr_index: int,
            curr_combination: List[int],
            remaining: int,
            combinations: List[List[int]]
        ) -> None:
            # Base case
            if remaining == 0:  # Reached the target
                combinations.append(curr_combination.copy())
                return

            for i in range(curr_index, length):

                # ! Skip adjacent duplicates, while addressing the edge case
                if i > curr_index and candidates[i] == candidates[i - 1]:
                    continue

                num = candidates[i]

                # ! Optimization: To the right only bigger numbers, sorted
                if remaining - num < 0:
                    break

                curr_combination.append(num)
                _generate_combinations(
                    curr_index=i + 1,
                    curr_combination=curr_combination,
                    remaining=remaining - num,
                    combinations=combinations
                )
                curr_combination.pop()

        candidates.sort()
        length = len(candidates)
        combinations = []
        _generate_combinations(0, [], target, combinations)
        return combinations

    # Here you avoid generating duplicates by using a data structure, which
    # doesn't allow them - a set.
    def combinationSum2(
        self,
        candidates: List[int],
        target: int
    ) -> List[List[int]]:

        def _generate_combinations(
            curr_index: int,
            curr_sum: int,
            curr_combination: List[int],
            generated_combinations: set[tuple]
        ) -> None:

            # Base cases:
            if curr_index == length:
                if curr_sum == target:
                    generated_combinations.add(tuple(curr_combination))
                return
            elif curr_sum == target:
                generated_combinations.add(tuple(curr_combination))
                return
            elif curr_sum > target:
                return

            for i in range(curr_index + 1, length):
                next_number = candidates[i]
                curr_combination.append(next_number)
                _generate_combinations(
                    i, curr_sum + next_number,
                    curr_combination, generated_combinations
                )
                curr_combination.pop()

        candidates.sort()
        length = len(candidates)
        combinations: set[tuple] = set()
        _generate_combinations(-1, 0, [], combinations)
        return [list(combination) for combination in combinations]


def main():
    print(Solution().combinationSum2(
        candidates=[2, 5, 2, 2],
        target=7
    ))


if __name__ == '__main__':
    main()
