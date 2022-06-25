#### Hash sets

There are two key questions that one should address, in order to implement the 
HashSet data structure, namely hash function and collision handling.

- hash function: the goal of the hash function is to assign an address to store 
a given value. Ideally, each unique value should have a unique hash value.

- collision handling: since the nature of a hash function is to map a value 
from a space A into a corresponding value in a smaller space B, it could 
happen that multiple values from space A might be mapped to the same value 
in space B. This is what we call collision. Therefore, it is indispensable 
for us to have a strategy to handle the collision.


Overall, there are several strategies to resolve the collisions:

- Separate Chaining: for values with the same hash key, we keep them in a 
bucket, and each bucket is independent of each other.
- Open Addressing: whenever there is a collision, we keep on probing on the 
main space with certain strategy until a free slot is found.
- 2-Choice Hashing: we use two hash functions rather than one, and we pick 
the generated address with fewer collision.

___

##### Approach 1 - LinkedList as Bucket
The common choice of hash function is the modulo operator, 
i.e. hash = value mod base. Here, the base of modulo operation would determine 
the number of buckets that we would have at the end in the HashSet.

Theoretically, the more buckets we have (hence the larger the space would be), 
the less likely that we would have collisions. The choice of base is a 
trade off between the space and the collision.

In addition, it is generally advisable to use a prime number as the base 
of modulo, e.g. 769, in order to reduce the potential collisions.

As to the design of bucket, again there are several options. One could 
simply use another Array as bucket to store all the values. However, one 
drawback with the Array data structure is that it would take O(N) time 
complexity to remove or insert an element (array reallocation in memory), 
rather than the desired O(1).

Since for any update operation, we would need to scan the entire bucket first 
to avoid any duplicate, a better choice for the implementation of bucket 
would be the LinkedList, which has a constant time complexity for the 
insertion as well as deletion, once we locate the position to update.

___
##### Approach 2: Binary Search Tree (BST) as Bucket

In the above approach, one of the drawbacks is that we have to scan the entire 
linked list in order to verify if a value already exists in the bucket (i.e. 
the lookup operation).

To optimize the above process, one of the strategies could be that we maintain
a sorted list as the bucket. With the sorted list, we could obtain the O(logN) 
time complexity for the lookup operation, with the binary search algorithm, 
rather than a linear O(N) complexity as in the above approach.

On the other hand, if we implement the sorted list in a continuous space such 
as Array, it would incur a linear time complexity for the update operations 
(e.g. insert and delete), since we would need to shift the elements.

So the question is can we have a data structure that have O(logN) time 
complexity, for the operations of search, insert and delete? -> BST, that will
serve as a bucket.

