from typing import List


"""
Summary:
    Brute force:
    generate_permutations() - generates the entire sequence of lexicographically
    increasing permutations. The problem in question though asks for the next
    lexicographically greater permutation. 
    
    The next permutation of an array of integers is the next lexicographically 
    greater permutation of its integer. More formally, if all the permutations 
    of the array are sorted in one container according to their lexicographical 
    order, then the next permutation of that array is the permutation that 
    follows it in the sorted container. If such arrangement is not possible, 
    the array must be rearranged as the lowest possible order (i.e., sorted 
    in ascending order).

    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does 
    not have a lexicographical larger rearrangement.
    
    Single Pass Approach (very smart):
    
    - For a sequence in descending order, no next larger permutation is
    possible. Say, [9, 5, 4, 3, 1]. We need to find the first pair of numbers
    a[i] and a[i - 1] starting from the right, so that a[i] > a[i - 1], meaning
    there is an ascending subsequence. Once found, we can notice that no
    rearrangements to the right of a[i - 1] can create a greater permutation
    since that subarray is in descending order --> we need to rearrange the 
    numbers to the right of a[i - 1] including itself (because there is a small
    ascending sequence right at the beginning). 
    What kind of rearrangement produces the next larger number? The one larger
    than the current one - we need to replace a[i - 1] with the number to its
    right, which is just larger than itself (coming from the right subset).
    
    Initial
    [1, 5, 8, 4, 7, 6, 5, 3, 1]
    
    Starting from the right looking for an ascending subsequence (4, 7). 
    
    From 4 start looking for the smallest number greater than 4. Its 5. Swap
    [1, 5, 8, 5, 7, 6, 4, 3, 1]
    
    The numbers after 5 now need to be reversed to ensure the smallest perm
    1, 5, 8, 5, 1, 3, 4, 6, 7
    
_______________________________________________________________________________

https://leetcode.com/problems/next-permutation/

A permutation of an array of integers is an arrangement of its members into a 
sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: 
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically 
greater permutation of its integer. More formally, if all the permutations of 
the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in 
the sorted container. If such arrangement is not possible, the array must be 
rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does 
not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
"""


def generate_permutations(arr: list[int]) -> list[list[int]]:
    """
    Generates the entire lexicographically increasing sequence of permutations.
    If given: [1, 2, 3]
    Returns: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """

    def _generate_permutations(
        curr_nums: list[int],
        curr_permutation: list[int],
        permutations: list[list[int]]
    ) -> None:
        if not len(curr_nums):
            permutations.append(curr_permutation.copy())
            return

        for i, num in enumerate(curr_nums):
            curr_permutation.append(curr_nums[i])
            remaining_nums = curr_nums[:i] + curr_nums[i + 1:]
            _generate_permutations(remaining_nums, curr_permutation, permutations)
            curr_permutation.pop()

    permutations = []
    _generate_permutations(arr, [], permutations)
    return permutations


class Solution:

    # Single pass. T: O(N)
    def nextPermutation(self, nums: List[int]) -> None:
        length = len(nums)
        i, j = length - 1, length - 1

        # Find the first ascending pair
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        # If i == 0, the entire nums is in descending order, reverse
        if i == 0:
            nums.reverse()
            return

        # Find the last number greater than the i - 1 (first num in asending pair)
        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1

        # Swap the numbers (the first in ascending pair, the furthers to the
        # right greater than k)
        nums[k], nums[j] = nums[j], nums[k]

        # Reverse the second part
        left, right = k + 1, length - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


    # Brute force. T: O(N!)
    # Sort the nums, generate ALL permutations in increasing order, find the
    # one you were given, the next one is the one we're looking for
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)

        permutations = generate_permutations(sorted_nums)

        next_lexico_greater_perm = None
        length = len(permutations)
        for i, permutation in enumerate(permutations):
            if permutation == nums:
                next_lexico_greater_perm = (
                    permutations[i + 1] if i != length - 1 else permutations[0]
                )
        nums[:] = next_lexico_greater_perm


def main():
    # print(generate_permutations([1, 2, 3]))
    nums = [1, 1, 5]
    Solution().nextPermutation(nums=nums)
    print(nums)


if __name__ == '__main__':
    main()
