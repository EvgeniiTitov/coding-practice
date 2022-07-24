from typing import List


"""
Summary: Iterate through days keeping the ones you need to find a warmer day
for and their index in the stack. For each new day, check if its warmer than 
the days in the stack. If yes, you the diff in indices to calculate the nb 
of days between them

To keep track of all of that, use a list of the same length as the original one
where each day has a certain index
_______________________________________________________________________________

https://leetcode.com/problems/daily-temperatures/

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to 
wait after the ith day to get a warmer temperature. If there is no future day 
for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [-1] * len(temperatures)
        stack = [(0, temperatures.pop(0))]
        for i, temperature in enumerate(temperatures, start=1):
            j, prev_day_temp = stack[-1]

            if temperature > prev_day_temp:
                stack.pop()
                out[j] = i - j  # Get diff in days using indices

                while len(stack):
                    j, prev_day_temp = stack[-1]
                    if temperature > prev_day_temp:
                        stack.pop()
                        out[j] = i - j
                    else:
                        break

            stack.append((i, temperature))

        # No warmer days for these guys sadkek
        if len(stack):
            for index, temp in stack:
                out[index] = 0

        return out


def main():
    print(Solution().dailyTemperatures(
        temperatures=[73,74,75,71,69,72,76,73]
    ))


if __name__ == '__main__':
    main()
