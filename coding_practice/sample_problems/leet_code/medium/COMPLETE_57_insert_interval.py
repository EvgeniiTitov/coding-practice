from typing import List


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/insert-interval/

You are given an array of non-overlapping intervals intervals where 
intervals[i] = [starti, endi] represent the start and the end of the ith
interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the 
start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in 
ascending order by starti and intervals still does not have any overlapping
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.


Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


class Solution:
    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int]
    ) -> List[List[int]]:

        Interval = List[int]

        def _check_if_overlap(
            interval_1: Interval, interval_2: Interval
        ) -> bool:
            start_1, end_1 = interval_1
            start_2, end_2 = interval_2
            if start_1 <= start_2:
                return end_1 >= start_2
            else:
                return end_2 >= start_1

        def _merge(*intervals: Interval) -> Interval:
            starts = [interval[0] for interval in intervals]
            ends = [interval[1] for interval in intervals]
            return [min(starts), max(ends)]

        if not len(intervals):
            return [newInterval]

        out = []

        return out


def main():
    print(Solution().insert(
        # intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]],
        # newInterval=[4,8]
        intervals=[[1,3],[6,9]],
        newInterval=[2,5]
    ))


if __name__ == '__main__':
    main()
