from typing import List
import heapq
import math


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on 
the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance 
(i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be 
unique (except for the order that it is in).

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is 
just [[-2,2]].
"""


class Point:
    def __init__(self, coordinates: List[int]) -> None:
        self.x, self.y = coordinates
        self.distance_to_origin = self._calculate_distance_to_origin()

    def _calculate_distance_to_origin(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other: "Point") -> bool:
        return self.distance_to_origin == other.distance_to_origin

    def __str__(self) -> str:
        return (
            f"Point. ({self.x}, {self.y}). "
            f"Distance to origin: {self.distance_to_origin: .3f}"
        )


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pass


def main():
    points = [[1, 3], [-2, 2]]
    p1 = Point(points[0])
    p2 = Point(points[1])
    print(p1)
    print(p2)
    print("Distance equal?", p1 == p2)


if __name__ == '__main__':
    main()
