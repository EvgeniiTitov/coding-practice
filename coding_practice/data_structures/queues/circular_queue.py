import typing as t


"""
The circular queue is a linear data structure in which the operations are 
performed based on FIFO (First In First Out) principle and the last position 
is connected back to the first position to make a circle. It is also called 
"Ring Buffer".

In a normal Queue, we can insert elements until queue becomes full. But once 
queue becomes full, we can not insert the next element even if there is a 
space in front of queue.

One of the benefits of the circular queue is that we can make use of the 
spaces in front of the queue. In a normal queue, once the queue becomes full, 
we cannot insert the next element even if there is a space in front of the 
queue ( ??? that's confusing, when we get elements from the queue, we get them
from the front, aka the new space is created before the head pointer, not after
the tail pointer)
But using the circular queue, we can use the space to store new values.

Circular Queue works by the process of circular increment i.e. when we try to 
increment the pointer and we reach the end of the queue, we start from the 
beginning of the queue.

-> Applications of Circular Queue:
    - CPU scheduling
    - Memory management
    - Traffic Management

-> How to build:
To build a circular queue we could form a virtual ring structure using an array
via index manipulation. Given an array of a fixed size, any element could be
considered a head. As long as we know the len of the queue, we could instantly
locate its tail: 
            tail_index = (head_index + count - 1) mod capacity,
where:
    capacity - array size
    count - length of the queue
    head/tail index - indices of head and tail within the array respectively

Say capacity is 5: [...|...|...|...|...]

Enqueue: for first item, i = (0 + 0) % capacity = 0
Enqueue: second item, i = (0 + 1) % capacity = 1
Enqueue: third item, i = (0 + 2) % c = 2
Enqueue: forth item, i = (0 + 3) % c = 3
Enqueue: fifth item, i = (0 + 4) % c = 4
Enqueue: count reached the max capacity

When dequeueing - the head goes right! So it floats across the array.
Dequeue: head index = (0 + 1) % capacity = 1, count 4
Dequeue: head index = (1 + 1) % capacity = 2, 3

Then when we append, the head stays where it is, we just wrap at the end of 
the array to come back to the beginning until the max capacity is reached again


-> Some further explanations:
- The purpose of a Circular Queue is to minimize the number of times the 
application calls malloc() and to make scanning memory blocks more efficient. 
The malloc() operation is an expensive operation. The system needs to find a 
contiguous block of memory that is the desired size and this takes time, 
especially in low memory conditions. This means that implementing a circular 
queue as a linked list, where each node is effectively malloc'd independently,
is the wrong choice.
The benefits of a Circular Queue are that the memory for the queue is 
allocated once at a fixed size and that iterating through the queue is a 
simple matter of iterating contiguous blocks of memory.

- Implementing a circular queue using linked lists defeats the purpose of 
circular queues (Space Reusability)
"""


class CircularQueue:
    def __init__(self, capacity: int) -> None:
        self._queue = [None] * capacity
        self._head_index = 0
        self._count = 0
        self._cap = capacity

    def enqueue(self, value: t.Any) -> bool:
        if self._count == self._cap:  # Queue is full
            return False
        self._queue[(self._head_index + self._count) % self._cap] = value
        self._count += 1
        return True

    def dequeue(self) -> bool:
        if not self._count:  # Queue is empty
            return False
        self._head_index = (self._head_index + 1) % self._cap
        self._count -= 1
        return True

    def front(self) -> t.Optional[t.Any]:
        if not self._count:
            print("Queue is empty")
            return None
        return self._queue[self._head_index]

    def rear(self) -> t.Optional[t.Any]:
        if not self._count:
            return None
        return self._queue[(self._head_index + self._count - 1) % self._cap]

    def is_empty(self) -> bool:
        return self._count == 0

    def is_full(self) -> bool:
        return self._count == self._cap

    def __len__(self) -> int:
        return self._count

    def __str__(self) -> str:
        return f"CircularQueue: {self._queue}"


def main():
    queue = CircularQueue(5)
    print(queue)

    '''
    CircularQueue: [None, None, None, None, None]

    Adding elements
    Enqueued: 0
    Enqueued: 1
    Enqueued: 2
    Enqueued: 3
    Enqueued: 4
    CircularQueue: [0, 1, 2, 3, 4]
    Queue size: 5
    Is full: True
    Head index: 0
    
    Dequeuing 3 items
    CircularQueue: [0, 1, 2, 3, 4]
    Head index: 3
    
    Adding more elements
    Enqueued: 10
    Enqueued: 11
    Enqueued: 12
    CircularQueue: [10, 11, 12, 3, 4]
    Head index: 3
    '''

    print("\nAdding elements")
    for i in range(10):
        if not queue.is_full():
            queue.enqueue(i)
            print("Enqueued:", i)
        else:
            break
    print(queue)
    print("Queue size:", len(queue))
    print("Is full:", queue.is_full())
    print(f"Head index: {queue._head_index}")

    print("\nDequeuing 3 items")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print(queue)
    print(f"Head index: {queue._head_index}")

    print("\nAdding more elements")
    for i in range(10, 20):
        if not queue.is_full():
            queue.enqueue(i)
            print("Enqueued:", i)
        else:
            break
    print(queue)
    print(f"Head index: {queue._head_index}")


if __name__ == '__main__':
    main()
