from typing import List


"""
Summary: Check if meetings overlap by sorting the list using start time and then
checking ith and i + 1 meetings
_______________________________________________________________________________

https://www.lintcode.com/problem/920/

Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.


(0,8),(8,10) is not conflict at 8

Example1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict

Example2:
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
"""


# ----- LINTCODE task -----
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals = [(interval.start, interval.end) for interval in intervals]
        intervals.sort(key=lambda e: e[0])

        for i in range(len(intervals) - 1):
            current_meeting = intervals[i]
            next_meeting = intervals[i + 1]

            current_start, current_end = current_meeting
            next_start, next_end = next_meeting

            if current_end > next_start:
                return False
        return True


# ----- LEETCODE one -----
class Solution:
    # T: O(N log N)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda e: e[0])
        for i in range(len(intervals) - 1):
            current_meeting = intervals[i]
            next_meeting = intervals[i + 1]

            current_start, current_end = current_meeting
            next_start, next_end = next_meeting

            if current_end > next_start:
                return False
        return True

    # Brute force
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        def overlap(interval1: List[int], interval2: List[int]) -> bool:
            return (
                interval1[0] >= interval2[0]
                and interval1[0] < interval2[1]
                or interval2[0] >= interval1[0]
                and interval2[0] < interval1[1]
            )

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if overlap(intervals[i], intervals[j]):
                    return False
        return True


def main():
    # intervals = [Interval(*times) for times in [(0, 30), (5, 10), (15, 20)]]
    # intervals = [Interval(*times) for times in [(5, 8), (9, 15), (16, 24)]]
    # print(Solution().can_attend_meetings(intervals))
    print(Solution().canAttendMeetings([[7, 10], [2, 4]]))


if __name__ == "__main__":
    main()
