import typing as t


"""
Summary: Dictionary with list as values. Use BS to efficiently find the
timestamp
_______________________________________________________________________________

https://leetcode.com/problems/time-based-key-value-store/

Design a time-based key-value data structure that can store multiple values 
for the same key at different time stamps and retrieve the key's value at a 
certain timestamp.

Implement the TimeMap class:
- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key with the 
  value at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was 
  called previously, with timestamp_prev <= timestamp. If there are multiple 
  such values, it returns the value associated with the largest timestamp_prev. 
  If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();

timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along 
with timestamp = 1.

timeMap.get("foo", 1);         // return "bar"

timeMap.get("foo", 3);         // return "bar", since there is no value 
corresponding to foo at timestamp 3 and timestamp 2, then the only 
value is at timestamp 1 is "bar".

timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along 
with timestamp = 4.

timeMap.get("foo", 4);         // return "bar2"

timeMap.get("foo", 5);         // return "bar2"
"""

# ---------------------- HEAD ON SOLUTION NO OPTIMISATION ---------------------


# Exceeds time limit after 44/47 tests
class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self._data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._data[key].append((timestamp, value))
        self._data[key].sort(key=lambda e: e[0])  # Find insert index

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._data:
            return ""
        values = self._data[key]
        time_diff = float("inf")
        closest_value_index = None
        for i, (value_timestamp, value) in enumerate(values):
            if value_timestamp > timestamp:
                continue

            curr_value_time_diff = abs(timestamp - value_timestamp)
            if curr_value_time_diff < time_diff:
                time_diff = curr_value_time_diff
                closest_value_index = i

        if closest_value_index is not None:
            return values[closest_value_index][-1]
        else:
            return ""


# ------------------------------- OPTIMIZED -----------------------------------

# TODO: Sorting causes Exceeded Time Limit  - I guess we assume timestamp is
#       always growing

class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self._data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._data:
            return ""

        values = self._data[key]
        left, right = 0, len(values) - 1
        while left <= right:
            middle_index = (left + right) // 2
            timestamp_middle, value_middle = values[middle_index]
            if timestamp_middle <= timestamp:
                left = middle_index + 1
            else:
                right = middle_index - 1

        return "" if timestamp < values[right][0] else values[right][1]



def main():
    time_map = TimeMap()
    # time_map.set("foo", "bar", 1)
    # print(time_map.get("foo", 1))
    # print(time_map.get("foo", 3))
    #
    # time_map.set("foo", "bar2", 4)
    # print(time_map.get("foo", 4))
    # print(time_map.get("foo", 5))

    time_map.set("love", "high", 10)
    time_map.set("love", "low", 20)
    print(5, time_map.get("love", 5))  # ""
    print(10, time_map.get("love", 10))  # high
    print(15, time_map.get("love", 15))  # high
    print(20, time_map.get("love", 20))  # low
    print(25, time_map.get("love", 25))  # low

if __name__ == '__main__':
    main()
