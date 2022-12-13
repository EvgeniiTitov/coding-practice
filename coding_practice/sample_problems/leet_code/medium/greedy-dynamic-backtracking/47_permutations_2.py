from typing import List, Set, Tuple


"""
Summary: Generate permutations by picking a number, getting remaining nums 
around it and calling recursively. At some point we run out of remaining nums,
so we generated a permutation. To enforce uniqueness, you could use a set.
_______________________________________________________________________________

https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates, return 
all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def _generate_permutations(
            remaining_nums: List[int],
            curr_permutation: List[int],
            permutations: Set[Tuple]
        ) -> None:
            # Base case
            if not len(remaining_nums):
                permutations.add(tuple(curr_permutation))
                return

            # Probe the solution space
            # TODO: You start from index 0 every call, is it correct? Yes
            for i, num in enumerate(remaining_nums):
                nums_left = remaining_nums[: i] + remaining_nums[i + 1:]
                curr_permutation.append(num)
                _generate_permutations(
                    nums_left, curr_permutation, permutations
                )
                curr_permutation.pop()

        permutations = set()
        _generate_permutations(nums, [], permutations)
        return [list(permutation) for permutation in permutations]

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict

        def _generate_unique_permutations(
            num_counts: dict,
            curr_permutation: List[int],
            permutations: List[List[int]]
        ) -> None:
            if len(curr_permutation) == len(nums):
                permutations.append(curr_permutation[:])
                return

            for num, count in num_counts.items():
                if count > 0:
                    curr_permutation.append(num)
                    num_counts[num] -= 1
                    _generate_unique_permutations(
                        num_counts, curr_permutation, permutations
                    )
                    num_counts[num] += 1
                    curr_permutation.pop()

        permutations = []
        num_counts = defaultdict(int)
        for num in nums:
            num_counts[num] += 1

        _generate_unique_permutations(num_counts, [], permutations)
        return permutations


def main():
    print(Solution().permuteUnique(nums=[1, 2, 3]))


if __name__ == '__main__':
    main()
