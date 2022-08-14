from typing import List


"""
Summary: Single pass, comparing current interval with the previous one. If
overlap - increment the counter. Depending on the overlap type (case 2 vs 3),
the prev interval is either updated or not.

Possible cases:

1. Don't overlap
    -----
         ------

2. Overlap 1
    -----
       -------
       
3. Overlap 2

    -----
         --------------
            -----

_______________________________________________________________________________

https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest 
of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are 
non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals 
non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're 
already non-overlapping.
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not len(intervals):
            return 0

        intervals.sort(key=lambda interval: interval[0])

        intervals_removed = 0
        prev_interval = intervals[0]
        for curr_interval in intervals[1:]:
            # If there's an overlap (case 2), we don't update the prev, we just
            # increment the counter. If case 3, ignore the longer one, prev
            # is the current one (shorter)
            if prev_interval[1] > curr_interval[0]:
                if prev_interval[1] > curr_interval[1]:  # Case 3 ^
                    prev_interval = curr_interval
                intervals_removed += 1
            else:
                prev_interval = curr_interval

        return intervals_removed
