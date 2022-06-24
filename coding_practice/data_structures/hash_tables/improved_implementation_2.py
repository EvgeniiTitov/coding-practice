import typing as t

'''
There are two main issues that we should tackle, in order to design an
efficient hashmap data structure:
    1). hash function design and
    2). collision handling.

1). hash function design: the purpose of hash function is to map a key value
to an address in the storage space, similarly to the system that we assign
a postcode to each mail address. As one can image, for a good hash function,
it should map different keys evenly across the storage space, so that we don't
end up with the case that the majority of the keys are concentrated in
a few spaces.

2). collision handling: essentially the hash function reduces the vast key
space into a limited address space. As a result, there could be the case where
two different keys are mapped to the same address, which is what we call
'collision'. Since the collision is inevitable, it is important that we have
a strategy to handle the collision.


Approach 1: Modulo + Array

Intuition
As one of the most intuitive implementations, we could adopt the modulo
operator as the hash function, since the key value is of integer type. In 
addition, in order to minimize the potential collisions, it is advisable to 
use a prime number as the base of modulo, e.g. 2069.

We organize the storage space as an array where each element is indexed with 
the output value of the hash function.

In case of collision, where two different keys are mapped to the same address, 
we use a bucket to hold all the values. The bucket is a container that hold 
all the values that are assigned by the hash function. We could use either a 
LinkedList or an Array to implement the bucket data structure.
'''


class Bucket:
    def __init__(self) -> None:
        self._bucket: t.List[t.Tuple[t.Any, t.Any]] = []

    def get(self, key: t.Any) -> t.Any:
        for k, v in self._bucket:
            if k == key:
                return v
        return -1

    def update(self, key: t.Any, value: t.Any) -> None:
        found = False
        for i, pair in enumerate(self._bucket):
            if pair[0] == key:
                self._bucket[i] = (key, value)
                found = True
                break
        if not found:
            self._bucket.append((key, value))

    def remove(self, key: t.Any) -> None:
        for i, pair in enumerate(self._bucket):
            if pair[0] == key:
                del self._bucket[i]


class HashMap:
    def __init__(self, key_space: int = 2069) -> None:
        self._key_space = key_space
        self._storage = [Bucket() for _ in range(self._key_space)]

    def put(self, key: int, value: t.Any) -> None:
        hash_key = key % self._key_space
        self._storage[hash_key].update(key, value)

    def get(self, key: int) -> t.Any:
        hash_key = key % self._key_space
        return self._storage[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self._key_space
        self._storage[hash_key].remove(key)
