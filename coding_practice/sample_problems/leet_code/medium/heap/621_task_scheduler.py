from typing import List


"""
Summary: Use heap to prioritize the most popular task. Once a task is scheduled,
do not return it to the heap but put it in a dict to cooldown for n iterations.

Every iteration we do house keeping by decrementing the cooldown counters for 
the tasks (slow) OR just remember till what cycle a task could not be returned
to the heap, i.e. potentially get rescheduled.

All tasks could be on cooldown, heap is empty, then we are idle.

Iterate till you have something on the heap or cooling down
_______________________________________________________________________________

https://leetcode.com/problems/task-scheduler/

Given a characters array tasks, representing the tasks a CPU needs to do, 
where each letter represents a different task. Tasks could be done in any order. 
Each task is done in one unit of time. For each unit of time, the CPU could 
complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period 
between two same tasks (the same letter in the array), that is that there must 
be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all 
the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
"""


# -------------------------- FIRST ITERATION ----------------------------------

# Passes but often fails with Exceeds Time Limit
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        from collections import defaultdict

        task_frequency = defaultdict(int)
        for task in tasks:
            task_frequency[task] += 1

        heap = []
        for task, task_freq in task_frequency.items():
            heap.append((-task_freq, task))
        heapq.heapify(heap)

        cool_down_tasks = {}
        tasks_out = []
        while len(heap) or len(cool_down_tasks):
            cur_task_key = None
            if len(heap):
                tasks_left, task = heapq.heappop(heap)
                tasks_out.append(task)
                tasks_left += 1
                # Reschedule for later only if it could be done more times
                if tasks_left < 0:
                    cool_down_tasks[(tasks_left, task)] = n
                    cur_task_key = (tasks_left, task)
            else:
                tasks_out.append("idle")

            # House keeping - check cooling tasks if any could be rescheduled
            # Decrement all counters except the current task if any scheduled
            if len(cool_down_tasks):
                for k in list(cool_down_tasks):
                    if cur_task_key and cur_task_key == k:
                        continue
                    cool_down_tasks[k] -= 1
                    if cool_down_tasks[k] <= 0:
                        del cool_down_tasks[k]
                        heapq.heappush(heap, k)

        print(tasks_out)
        return len(tasks_out)


# -----------------------------------------------------------------------------

# Passes all the tests - the trick is to avoid doing house keeping by
# decrementing the counters, rather remember until what cycle a task could
# not be rescheduled!
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        from collections import defaultdict

        task_frequency = defaultdict(int)
        for task in tasks:
            task_frequency[task] += 1

        heap = []
        for task, task_freq in task_frequency.items():
            heap.append((-task_freq, task))
        heapq.heapify(heap)

        counter = 0
        cool_down_tasks = {}
        tasks_out = []  # Could be omitted
        while len(heap) or len(cool_down_tasks):
            curr_task_key = None
            if len(heap):
                tasks_left, task = heapq.heappop(heap)
                tasks_out.append(task)
                tasks_left += 1
                if tasks_left < 0:
                    cool_down_tasks[(tasks_left, task)] = counter + n
                    curr_task_key = (tasks_left, task)
            else:
                tasks_out.append("idle")

            if len(cool_down_tasks):
                for k in list(cool_down_tasks.keys()):
                    if curr_task_key and k == curr_task_key:
                        continue
                    if counter >= cool_down_tasks[k]:
                        del cool_down_tasks[k]
                        heapq.heappush(heap, k)

            counter += 1

        return counter


def main():
    print(
        Solution().leastInterval(
            tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"],
            # tasks=["A","A","A","B","B","B"],
            n=2,
        )
    )


if __name__ == "__main__":
    main()
