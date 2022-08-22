from typing import List


# TODO: Greedy


"""
Summary / Thoughts:
    Regular D&C or DP doesn't seem to work within the allowed timeframe. 
    
    You need to think greedily, i.e. each step lets pick the best local solution and
    see if it works. If not, try the next best, etc? Nice idea, look at the
    backtracking solution with slight optimisation eliminating inadequete jumps 
    out of bounds
    
    I've been solving the problem left-right, could we do right-left?
    The observation to make here is that we only ever jump to the right. 
    This means that if we start from the right of the array, every time we 
    will query a position to our right, that position has already be determined 
    as being GOOD or BAD. This means we don't need to recurse anymore, as we 
    will always hit the memo table
    
_______________________________________________________________________________

https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially positioned at the 
array's first index, and each element in the array represents your maximum 
jump length at that position.

Return true if you can reach the last index, or false otherwise. (CAN OR NOT)

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum 
jump length is 0, which makes it impossible to reach the last index.
"""


class Solution:

    # SOLUTION: DP bottom up
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 1:
            return True

        indices = [None] * len(nums)
        indices[-1] = True

        # Starting from -2 from the end, consider the right subset of values
        # checking if you could jump to a GOOD index (leads to the end), if yes
        # then the i index is GOOD as well

        for i in range(length - 2, -1, -1):
            # Adequate furthest jump to avoid out of bounds
            furthest_jump = min(i + nums[i], length - 1)

            for j in range(i + 1, furthest_jump + 1):
                if indices[j] is True:
                    indices[i] = True
                    break

        return indices[0] is True


    # SOLUTION: Backtracking. Time Limit Exceeded. Without cache: (75 tests)
    # With cache 170 / 170, the last one failed LOL
    # T: O(2 ^ N); S: O(2N) = O(N) (recursion + _cache)
    def canJump(self, nums: List[int]) -> bool:

        def _cache(func):
            _cache  = {}
            def wrapper(index: int) -> bool:
                if index not in _cache:
                    _cache[index] = func(index)
                return _cache[index]
            return wrapper

        @_cache
        def _reach_last_step(curr_index: int) -> bool:
            # Base case
            if curr_index == destination:
                return True
            elif curr_index > destination:  # Jumped over the last step
                return False

            # To avoid overshooting, calculate the furthest adequate jump
            furthest_jump = min(curr_index + nums[curr_index], length - 1)

            # Greedily pick the furthest jump available from the current step,
            # if doesn't work pick the next best etc probing all options
            for i in range(furthest_jump, curr_index, -1):
                if _reach_last_step(i):
                    return True

            return False

        length = len(nums)
        if length == 1:
            return True

        destination = length - 1
        return _reach_last_step(0)


    # My greedy attempt. Same performance as DP below (75 tests)
    # T: O(2 ^ N); S: O(N)
    def canJump(self, nums: List[int]) -> bool:

        def _reach_last_step(curr_index: int) -> bool:
            # Base case
            if curr_index == destination:
                return True
            elif curr_index > destination:  # Jumped over the last step
                return False

            curr_options = nums[curr_index]

            if curr_options == 0:
                return False
            else:
                # Greedily pick the best solution first, then the second best
                for i in range(curr_options, 0, -1):
                    next_index = curr_index + i
                    reached = _reach_last_step(next_index)
                    if reached:
                        return True

            return False

        length = len(nums)
        if length == 1:
            return True

        destination = length - 1
        return _reach_last_step(0)

    # My DP. Time Limit Exceeded even with the cache. The overall approach is
    # faulty (75 tests, 73 without the cache).
    # T: O(2 ^ N); S: O(N)
    def canJump(self, nums: List[int]) -> bool:

        def _cache(func):
            _cache  = {}
            def wrapper(index: int) -> bool:
                if index not in _cache:
                    _cache[index] = func(index)
                return _cache[index]
            return wrapper

        @_cache
        def _reach_last_step(curr_index: int) -> bool:
            # Base case
            if curr_index == destination:
                return True
            elif curr_index > destination:  # Jumped over the last step
                return False

            curr_options = nums[curr_index]

            if curr_options == 0:
                return False
            else:
                for i in range(1, curr_options + 1):
                    next_index = curr_index + i
                    reached = _reach_last_step(next_index)
                    if reached:
                        return True

            return False

        length = len(nums)
        if length == 1:
            return True

        destination = length - 1
        return _reach_last_step(0)


def main():
    print(Solution().canJump(
        nums=[2, 3, 1, 1, 4]
        # nums=[3, 2, 1, 0, 4]
    ))


if __name__ == '__main__':
    main()
