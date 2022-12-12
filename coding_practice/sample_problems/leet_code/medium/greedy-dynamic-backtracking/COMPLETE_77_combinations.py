from typing import List, Set, Tuple


# TODO: Big learning opportunity - how to keep only unique combinations of
#       items? [[1, 2], [2, 1]] --> [[1, 2]] OR [[2, 1]]


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers 
chosen from the range [1, n].

You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to 
be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
"""


class Solution:
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     pass

    # Hack solution using set to remove duplicates
    # TLE
    def combine(self, n: int, k: int) -> List[List[int]]:

        def _generate_combinations(
            curr_combination: List[int],
            available_nums: List[int],
            all_combinations: Set[Tuple[int]]
        ) -> None:
            # Base case

            # Thats fucking terrible
            if len(curr_combination) == combination_length:
                curr_combination_tuple = tuple(sorted(curr_combination))
                if curr_combination_tuple not in all_combinations:
                    all_combinations.add(tuple(curr_combination))

            if not len(available_nums):
                return

            # Probe the solution space
            for i, num in enumerate(available_nums):
                curr_combination.append(num)
                remaining_nums = available_nums[: i] + available_nums[i + 1:]
                _generate_combinations(
                    curr_combination, remaining_nums, all_combinations
                )
                curr_combination.pop()

        combination_length = k
        numbers_to_chose_from = range(1, n + 1)
        combinations = set()
        _generate_combinations([], list(numbers_to_chose_from), combinations)
        return [list(combination) for combination in combinations]


def main():
    print(Solution().combine(n=4, k=2))


if __name__ == '__main__':
    main()
