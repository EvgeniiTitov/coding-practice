from typing import List


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/detect-squares/

You are given a stream of points on the X-Y plane. Design an algorithm that:

- Adds new points from the stream into a data structure. Duplicate points are 
allowed and should be treated as different points.
- Given a query point, counts the number of ways to choose three points from 
the data structure such that the three points and the query point form an 
axis-aligned square with positive area.
- An axis-aligned square is a square whose edges are all the same length and 
are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:
DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares 
with point point = [x, y] as described above.
 
Example 1:
Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
                               //   - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
                               //   - The first, second, and third points
                               //   - The first, third, and fourth points
"""


from collections import defaultdict

Point = tuple[int, int]

class DetectSquares:

    def __init__(self):
        self._points_counter = defaultdict(int)
        self._xs = defaultdict(list)
        self._ys = defaultdict(list)

    def add(self, point: List[int]) -> None:
        x, y = point
        self._points_counter[(x, y)] += 1
        self._xs[x].append((x, y))
        self._ys[y].append((x, y))

    def count(self, point: List[int]) -> int:
        x, y = point
        if x not in self._xs or y not in self._ys:
            return 0
        else:
            return self._count_squares(x, y)

    def _count_squares(self, point_x: int, point_y: int) -> int:
        x_points = self._xs[point_x]
        y_points = self._ys[point_y]
        total_squares = 0
        for x1, y1 in x_points:
            for x2, y2 in y_points:
                required_point = (x2, y1)
                # Get the forth point if exists
                if not required_point in self._points_counter:
                    continue

                # Validate the points form a square
                if self._is_a_square(
                    (point_x, point_y), (x1, y1), (x2, y2), required_point
                ):
                    # TODO: Same coord can have multiple points!
                    total_squares += 1

        return total_squares

    def _is_a_square(self, p1: Point, p2: Point, p3: Point, p4: Point) -> bool:
        # TODO: Complete me - https://www.geeksforgeeks.org/check-given-four-points-form-square/#:~:text=Approach%3A%20The%20idea%20is%20to,to%20%E2%88%9A2%20times%20d.
        pass


def main():
    detector = DetectSquares()
    detector.add([3, 10])
    detector.add([11, 2])
    detector.add([3, 2])
    print(detector.count([11, 10]))


if __name__ == '__main__':
    main()
