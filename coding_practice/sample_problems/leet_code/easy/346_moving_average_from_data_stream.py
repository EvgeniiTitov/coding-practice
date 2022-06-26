import typing as t


'''
Summary: We care only about numbers within the window -> discard the ones that 
outside of it. Queue works fine, add to the right, pop off the left if len(q) >
window size. deque() works nice for this as its optimised for operations at its
ends
------------------------------------------------------------------------------

https://leetcode.com/problems/moving-average-from-data-stream/

Given a stream of integers and a window size, calculate the moving average
of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.


Example 1:
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
'''


# Accumulates all values, which is not required, we just need those ones that
# are within the window
class MovingAverage:

    def __init__(self, size: int):
        self._size = size
        self._stack = []

    def next(self, val: int) -> float:
        self._stack.append(val)
        sum_ = sum(self._stack[-self._size:])
        if len(self._stack) < self._size:
            denominator = len(self._stack)
        else:
            denominator = self._size
        return sum_ / denominator


from collections import deque

# S: O(1)
class MovingAverage:

    def __init__(self, size: int):
        self._size = size
        self._queue = deque()

    def next(self, val: int) -> float:
        # Drop unnecessary items
        if len(self._queue) >= self._size:
            self._queue.popleft()

        self._queue.append(val)

        sum_ = sum(self._queue)
        queue_size = len(self._queue)
        denominator = min(queue_size, self._size)
        return sum_ / denominator
