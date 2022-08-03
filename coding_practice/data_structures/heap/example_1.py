import heapq
import random


"""
heapq work on lists directly, in place. 

Elements could be inserted 1 by 1 or if there is always a list -> heapify()

A heap doesn't have to be sorted to satisfy the heap property, BUT since every
sorted list does satisfy the property, running heapify() on a sorted list won't
change it.

- To read the smallest element: [0]
- To pop the smallest element preserving the heap property: heappop()
- To push an element preserving the heap property: heappush()

These are useful in some algorithms since they’re more efficient than doing 
the two operations separately:
- heapreplace() is equivalent to heappop() followed by heappush()
- heappushpop() is equivalent to heappush() followed by heappop()
"""


random.seed(2)


def main():
    items = [random.randint(0, 100) for _ in range(10)]
    print("Items:", items)

    heapq.heapify(items)
    print("Item heapified:", items)

    print("\nPopping the smallest element:", heapq.heappop(items))
    print("Heap after:", items)

    print("\nPushing 0 to the heap")
    heapq.heappush(items, 0)
    print("Heap after:", items)


if __name__ == "__main__":
    main()
