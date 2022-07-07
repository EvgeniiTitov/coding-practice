from typing import List
import heapq


"""
Summary: Sort based on starting time. Single pass, for each meeting we need a 
room - check if one is available (min heap based on end time). If heap empty,
add a new room. If not, check if we could use this room. if yes, reuse the room,
else add a new one. At the end check the len of the heap to get total N of rooms
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

    # Mine with hints. T: O(N2);
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: item[0])

        def _get_next_room():
            counter = 0
            while True:
                yield counter
                counter += 1

        room_counter = _get_next_room()
        allocated_rooms = {}
        for interval in intervals:
            start_time, end_time = interval

            if not len(allocated_rooms):
                allocated_rooms[next(room_counter)] = end_time
            else:
                # This O(N), would be cool to do O(log N)
                for room_number, room_end_time in allocated_rooms.items():
                    if start_time >= room_end_time:
                        allocated_rooms[room_number] = end_time
                        break
                else:
                    allocated_rooms[next(room_counter)] = end_time
        return len(allocated_rooms)

    # Mine with hints using heap: T: O(N log N); S: O(N)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: item[0])

        # We could store all allocated rooms on a min heap - end time. Then,
        # whenever we need to find a room for a new meeting (they are sorted),
        # we check heap[0]. If still busy, add a new room, add to the heap
        rooms = []
        heapq.heapify(rooms)
        for interval in intervals:
            start_time, end_time = interval

            # No rooms available at all, get a new one
            if not len(rooms):
                heapq.heappush(rooms, end_time)
            else:
                soonest_free_room_end_time = rooms[0]
                if start_time >= soonest_free_room_end_time:
                    heapq.heappushpop(rooms, end_time)
                else:
                    heapq.heappush(rooms, end_time)
        return len(rooms)


    # DOESN'T WORK - Brute force approach
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        This one DOESN'T work as it detects this as 2 intersections but its
        just 1 (concurrent).
        __________________________
           ________
                      _______
        """
        intervals.sort(key=lambda item: item[0])

        length = len(intervals)
        max_intersections = 0
        for i in range(length):
            temp_intersections = 0
            interval_1 = intervals[i]
            for j in range(i + 1, length):
                interval_2 = intervals[j]
                if self._check_if_intersect(interval_1, interval_2):
                    temp_intersections += 1
            max_intersections = max(max_intersections, temp_intersections)
        return max_intersections or 1

    def _check_if_intersect(
        self,
        interval1: List[int],
        interval2: List[int]
    ) -> bool:
        return (
            interval1[0] < interval2[1] < interval1[1]
            or interval1[0] < interval2[0] < interval1[1]
        )

    # DOESN'T WORK - 2 pointers counting max N of itersections
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
    # intervals = [[1,8],[6,20],[9,16],[13,17]]
    # intervals = [[0, 10], [3, 13], [7, 20], [21, 26], [24, 30]]
    intervals = [[13,15],[1,13]]
    print(Solution().minMeetingRooms(intervals))


if __name__ == '__main__':
    main()
