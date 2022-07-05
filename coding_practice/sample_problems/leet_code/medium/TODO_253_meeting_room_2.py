from typing import List


# TODO: Close but not quite right yet

"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals intervals where 
intervals[i] = [starti, endi], return the minimum number of conference rooms required.


Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
_________________
   _____
         _____

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

__________
   __________
        __________________
                          _________
                               ___________________

______
      _________
               ________


_____
     ________________________
               _____________
                        _______________

N or rooms = max N of overlapping meetings?
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda e: e[0])
        intervals = [
            set(range(interval[0], interval[1] + 1)) for interval in intervals
        ]
        max_intersections = 0
        temp_intersections = 0
        left, right = 0, 1
        while right < len(intervals):
            left_p_interval = intervals[left]
            right_p_interval = intervals[right]

            intersection = left_p_interval.intersection(right_p_interval)

            if not intersection or len(intersection) == 1:
                left = right
                right += 1
                # max_intersections = max(max_intersections, temp_intersections)
                # temp_intersections = 0
                continue

            temp_intersections += 1
            while right < len(intervals) - 1:
                right += 1
                right_p_interval = intervals[right]
                another_intersection = intersection.intersection(right_p_interval)
                if another_intersection and len(another_intersection) > 1:
                    temp_intersections += 1
                else:
                    break

            max_intersections = max(max_intersections, temp_intersections)
            left = right
            right += 1
            temp_intersections = 0

        return max_intersections + 1


def main():
    # intervals = [[0, 30], [5, 10], [15, 20]]
    intervals = [[1,8],[6,20],[9,16],[13,17]]
    # intervals = [[0, 10], [3, 13], [7, 20], [21, 26], [24, 30]]
    print(Solution().minMeetingRooms(intervals))


if __name__ == '__main__':
    main()
