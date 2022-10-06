import typing


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/logger-rate-limiter/

Design a logger system that receives a stream of messages along with their 
timestamps. Each unique message should only be printed at most every 10 seconds 
(i.e. a message printed at timestamp t will prevent other identical messages 
from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) Returns true if the 
message should be printed in the given timestamp, otherwise returns false.
 
Example 1:
Input
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", 
"shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
Output
[null, true, true, false, false, false, true]

Explanation
Logger logger = new Logger();
logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
"""

# TODO: Queue to push out stale message and a set/dict to check if we've seen the message at O(1) time

from collections import deque


class Logger:

    """
    Logic to get rid of stale messages, i.e. those messages whose timestamp is
    older than current - 10.
    """
    TTL = 10

    def __init__(self):
        self._queue = deque()
        self._seen_messages = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self._seen_messages:
            self._seen_messages.add(message)
            self._queue.appendleft((timestamp, message))
            return True



# -----------------------------------------------------------------------------

# Dictionary approach. T: O(1); S: O(M), where M - the size of all messages
# The problem  is the dict can grow indefinitely as it has a bunch of stale
# messages that ideally should be removed. A separate thread or something to do it.

class Logger:

    def __init__(self):
        self._received_messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # New message, store it, its timestamp and return True
        if message not in self._received_messages:
            self._received_messages[message] = timestamp
            return True

        # We've already printed this message, check when was it done
        prev_timestamp = self._received_messages[message]
        delta = timestamp - prev_timestamp
        if delta >= 10:
            self._received_messages[message] = timestamp
            return True
        else:
            return False


def main():
    logger = Logger()
    print(logger.shouldPrintMessage(1, "foo"))
    print(logger.shouldPrintMessage(2, "bar"))
    print(logger.shouldPrintMessage(3, "foo"))
    print(logger.shouldPrintMessage(8, "bar"))
    print(logger.shouldPrintMessage(10, "foo"))
    print(logger.shouldPrintMessage(11, "foo"))


if __name__ == '__main__':
    main()
