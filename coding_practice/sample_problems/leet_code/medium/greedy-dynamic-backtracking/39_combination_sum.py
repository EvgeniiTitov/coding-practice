from typing import List


"""
Summary:
    Backtracking - gradually item by item generate combinations and pick those 
    that add up to the target and prune those subtrees which result in sum() >
    target
_______________________________________________________________________________

https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen 
numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen 
numbers is different.

The test cases are generated such that the number of unique combinations that 
sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
"""


class Solution:

    # Backtracking. T: O (N ** (T/M + 1))
    # TODO: Could avoid sum() ing by keeping track of the curr sum as a param
    def combinationSum(
        self,
        candidates: List[int],
        target: int
    ) -> List[List[int]]:

        def _generate_combinations(
            curr_index: int,
            curr_combination: List[int],
            combinations: List[List[int]]
        ) -> None:
            # Base cases - as soon as we overshoot, prune this branch
            sum_ = sum(curr_combination)
            if sum_ > target:
                return
            elif sum_ == target:
                combinations.append(curr_combination.copy())

            for i in range(curr_index, length):
                curr_combination.append(candidates[i])
                _generate_combinations(i, curr_combination, combinations)
                curr_combination.pop()

        length = len(candidates)
        if length == 1 and candidates[0] > target:
            return []

        combinations = []
        _generate_combinations(0, [], combinations)
        return combinations


def main():
    print(Solution().combinationSum(
        candidates=[2, 3, 5],
        target=11
    ))


if __name__ == '__main__':
    main()
