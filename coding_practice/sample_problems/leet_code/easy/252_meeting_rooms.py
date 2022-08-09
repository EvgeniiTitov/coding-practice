from typing import List


"""
Summary: Sorting is the key, then iterate over pairs
_______________________________________________________________________________

https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals where intervals[i] = [starti, endi], 
determine if a person could attend all meetings. (i.e. they do not overlap?)

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
"""


class Solution:

    # Brute force head on
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda time: time[0])  # N Log N

        def _check_if_meetings_overlap(first_meeting, second_meeting) -> bool:
            first_start, first_end = first_meeting
            second_start, second_end = second_meeting
            if first_end > second_start:
                return True
            return False

        for i in range(len(intervals) - 1):
            first_meeting = intervals[i]
            next_meeting = intervals[i + 1]
            if _check_if_meetings_overlap(first_meeting, next_meeting):
                return False
        return True


def main():
    print(Solution().canAttendMeetings(intervals=[[0, 30], [5, 10], [15, 20]]))


if __name__ == "__main__":
    main()
