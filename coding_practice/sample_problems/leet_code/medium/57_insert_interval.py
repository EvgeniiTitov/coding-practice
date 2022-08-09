from typing import List


"""
Summary: newInterval might overlap multiple or no intervals at all. Aggregate
all intervals it overlap (either by extending newInterval itself, which is 
smart or in a list) and then when you go beyond newInterval range (interval 
start > newInterval end), append it to list out along side the remaining
intervals
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

    # Single pass
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
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

        if not len(intervals):
            return [newInterval]

        out = []
        new_interval_appended = False
        for interval in intervals:
            interval_start, interval_end = interval

            # No intersection
            if interval_end < newInterval[0]:
                out.append(interval)
            elif interval_start > newInterval[1]:
                # Once we've made beyond the new interval, add it to out list
                if not new_interval_appended:
                    out.append(newInterval)
                    new_interval_appended = True

                out.append(interval)
            # If they overlap - merge (enlarge the newInterval itself)
            elif _check_if_overlap(interval, newInterval):
                newInterval[0] = min(interval_start, newInterval[0])
                newInterval[1] = max(interval_end, newInterval[1])

        # In case interval is within another one. Interval [1,5], newIntr [2,3]
        if not new_interval_appended:
            out.append(newInterval)

        return out

    # That is not good, unnecessary sorting at the end, we need just one pass
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
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
        overlap_found = False
        while len(intervals):
            interval = intervals.pop(0)
            if not _check_if_overlap(interval, newInterval):
                out.append(interval)
            else:
                overlap_found = True
                overlapping_intervals = [interval]
                while len(intervals):
                    next_interval = intervals[0]
                    if _check_if_overlap(next_interval, newInterval):
                        overlapping_intervals.append(intervals.pop(0))
                    else:
                        break

                overlapping_intervals.append(newInterval)
                merged = _merge(*overlapping_intervals)
                out.append(merged)

        if not overlap_found:
            out.append(newInterval)
            out.sort(key=lambda e: e[0])

        return out


def main():
    print(
        Solution().insert(
            intervals=[[1, 5]],
            newInterval=[2, 3]
            # intervals=[[1,3],[6,9]],
            # newInterval=[2,5]
        )
    )


if __name__ == "__main__":
    main()
