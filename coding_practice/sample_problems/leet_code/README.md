


### Important points to remember:

- Sequential loops still result in O(n), no nested looping.

- 
```python
l = list(range(10))

# Nested loop only covers the subset of values
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        pass
    
# permutations like approach (start from 0)
for i in range(len(l)):
    for j in range(len(l)):
        pass

```

- Sliding window approach is very good. 2 points that you update within 
a while loop - linear time.
- When measuring *distance* between 2 pointers don't forget to +1 or -1 
depending on what you want to get
```
a b c d e
The number of chars between b (1) and e (4) is: right - left - 1, aka
4 - 1 - 1 = 2
The number of chars inclusive of the pointers: right - left + 1, aka
4 - 1 + 1 = 4
```
-