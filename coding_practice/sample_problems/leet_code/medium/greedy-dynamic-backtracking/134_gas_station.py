from typing import List, Tuple


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/gas-station/

There are n gas stations along a circular route, where the amount of gas at 
the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to 
travel from the ith station to its next (i + 1)th station. You begin the 
journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's 
index if you can travel around the circuit once in the clockwise direction, 
otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back 
to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""


class Solution:

    # Nice dude I sure could come up with this fucking stupid ass solution fuck off
    # TODO: Explanation https://leetcode.com/problems/gas-station/discuss/1004074/Greedy-Method-or-Explanation-%2B-Visual-or-Python
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank, curr_tank = 0, 0
        starting_index = 0
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                starting_index = i + 1
                curr_tank = 0

        return starting_index if total_tank >= 0 else -1

    # Correct but Time Limit Exceeded 33/37 as its O(N2)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def _get_gas_cost_at_index(index: int) -> Tuple[int, int]:
            length = len(gas)
            idx = index % length
            return gas[idx], cost[idx]

        def _drive_from_gas_station(index: int) -> bool:
            nb_stations = len(gas)
            left_over_gas = 0
            for _ in range(nb_stations):
                curr_gas, curr_cost = _get_gas_cost_at_index(index)
                gas_left = curr_gas - curr_cost + left_over_gas

                if gas_left < 0:  # <=?
                    return False

                left_over_gas = gas_left
                index += 1

            return True

        candidates = []
        for i, (curr_gas, curr_cost) in enumerate(zip(gas, cost)):
            if curr_gas >= curr_cost:
                candidates.append((i, curr_gas, curr_cost))

        if not len(candidates):
            return -1

        candidates.sort(key=lambda item: item[2])  # Use heap?

        while len(candidates):
            candidate = candidates.pop(0)
            index, _, _ = candidate
            is_possible = _drive_from_gas_station(index)
            if is_possible:
                return index

        return -1

    # Heap didn't help, still 33/37, still T: O(2)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        import heapq

        def _get_gas_cost_at_index(index: int) -> Tuple[int, int]:
            length = len(gas)
            idx = index % length
            return gas[idx], cost[idx]

        def _drive_from_gas_station(index: int) -> bool:
            nb_stations = len(gas)
            left_over_gas = 0
            for _ in range(nb_stations):
                curr_gas, curr_cost = _get_gas_cost_at_index(index)
                gas_left = curr_gas - curr_cost + left_over_gas

                if gas_left < 0:  # <=?
                    return False

                left_over_gas = gas_left
                index += 1

            return True

        candidates = []
        for i, (curr_gas, curr_cost) in enumerate(zip(gas, cost)):
            if curr_gas >= curr_cost:
                candidates.append((curr_cost, curr_gas, i))

        if not len(candidates):
            return -1

        heapq.heapify(candidates)

        while len(candidates):
            candidate = heapq.heappop(candidates)
            _, _, index = candidate
            is_possible = _drive_from_gas_station(index)
            if is_possible:
                return index

        return -1


def main():
    print(Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))


if __name__ == "__main__":
    main()
