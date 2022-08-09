from typing import List


"""
Summary: Use stack to keep merging overlapping intervals. Previous (on the
stack) and current overlap? Yes, pop the prev, merge, push back. Else, just push
to the stack.
_______________________________________________________________________________

https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


class Solution:

    # T: O(N log N); S: O(N)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        Interval = List[int]

        intervals.sort(key=lambda e: e[0])

        def _check_if_overlap(
            interval_1: Interval, interval_2: Interval
        ) -> bool:
            start_1, end_1 = interval_1
            start_2, end_2 = interval_2
            return end_1 >= start_2

        def _merge(interval_1: Interval, interval_2: Interval) -> Interval:
            start_1, end_1 = interval_1
            start_2, end_2 = interval_2
            return [start_1, max(end_1, end_2)]

        stack = [intervals.pop(0)]
        for interval in intervals:
            prev_interval = stack[-1]
            if _check_if_overlap(prev_interval, interval):
                stack.pop()
                stack.append(_merge(prev_interval, interval))
            else:
                stack.append(interval)

        return stack


def main():
    print(
        Solution().merge(
            # intervals=[[1,3],[2,6],[8,10],[15,18]]
            # intervals=[[1,4],[4,5]],
            intervals=[[1, 4], [2, 3]]
        )
    )


if __name__ == "__main__":
    main()
