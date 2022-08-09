from coding_practice.utils import times_called

"""
Given 2 strings s1 and s2
Convert s2 to s1 using: delete, insert or replace operations
Return the min N of edit operations required

Example 1:
s1 = catch
s2 = carch
Output: 1
Explanation: "r" must be replaced with "t"

Example 2:
s1 = table
s2 = tbres
Output: 3
Explanation: insert a at index 2, replace r with l, delete s. Just replacements
at each index would result in 4 edits instead of 3.

_______________________________________________________________________________

How do we break down the problem into simpler manageable pieces? Consider 3
cases:

1. 
    s1 = table
    s2 = tgable
    
    required operation - Delete
    
2. 
    s1 = table
    s2 = tble
    
    required operation - Insert

3. 
    s1 = table
    s2 = tcble
    
    required operation - Replace
    
^ are 3 simple (manageable) subproblems, which we know how to solve. 

"""


@times_called
def find_min_operations(s1: str, s2: str, index1: int, index2: int) -> int:
    # Base cases - end of one of the strings
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1

    # If both characters match, consider the next pair
    if s1[index1] == s2[index2]:
        return find_min_operations(s1, s2, index1 + 1, index2 + 1)

    # Haven't reached the end and chars do not match, find what to do
    # by considering 3 subproblems and picking the one needs the fewest edits
    delete = 1 + find_min_operations(s1, s2, index1, index2 + 1)
    insert = 1 + find_min_operations(s1, s2, index1 + 1, index2)
    replace = 1 + find_min_operations(s1, s2, index1 + 1, index2 + 1)
    return min(delete, insert, replace)


def main():
    print(find_min_operations("table", "tbrles", 0, 0))


if __name__ == "__main__":
    main()
