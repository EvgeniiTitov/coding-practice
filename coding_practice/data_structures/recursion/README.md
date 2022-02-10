Tail recursion doesn't exist in Python, but you could emulate it by avoiding
storing any state within your partially complete functions. Instead, pass everything 
as parameters. 

#### Why
- Breaking down complicated problems in a set of smaller ones.


#### Key points:

- Not always quicker as there is some overhead (new function on the stack, 
copying parameters, etc.)
- Good with trees, graphs, etc
- Used in divide and conquer algorithms, greedy and dynamic programming

STOPPED  - https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/learn/lecture/18683676#overview