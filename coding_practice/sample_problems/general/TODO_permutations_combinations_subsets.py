from __future__ import annotations
import typing as t
import itertools


# TODO: Combination + super set
"""
Power set is all possible combinations of all possible lengths, from 0 to n.

Sets:

- A set is a collection of elements.
- A set with no elements is still a set and is known as an empty set.
- A subset is any combination of elements from a set.
- An empty set is a subset of any set. This means every set has an empty subset.
- Sets are represented using the notation: {,}.
- Example: {1,5} is a set. {}, {1}, {5}, & {1,5} are all of its possible subsets.
- There is a formula for working out how many subsets a set has: 
  A set with n elements has 2^n subsets.
- Using our previous example ({1,5}): n = 2 as there are 2 elements in our set. 
  2^n = 2^2 = 4. So a set with 2 elements has 4 subsets. A set with 3 elements 
  has 2^3 subsets, which is 8.
- When dealing with strings, often we refer to subsets as combinations. 
  The idea is the same as subsets: "AB" has 2^2 combinations (as there are 
  2 characters). So all 4 combinations of "AB" are: {}, {'A'}, {'B'}, {'A', 'B'}.

Permutations

- A permutation is essentially an ordered combination, except the total length 
  of each permutation must equal the original input.
- Finding all permutations of a string is sort of the same as saying "find 
  all anagrams of a string" (except our permutations might not all be real words).
- There are two types of permutation: with repetition & without repetition.
- Simple permutation example: "AB" has 2 permutations: "AB" and "BA".
- Repetition example: "AAB" has 6 permutations: "AAB", "ABA", "BAA", "BAA", "ABA", "AAB". 
  Notice there are repeated characters, this is a permutation with repetition 
  allowed (as each "A" is treated as distinct). Without repetition, the total 
  permutations would be 3: "AAB", "ABA", "BAA".
- To calculate the total number of permutations when repetition is allowed use 
  the following formula: n! (! means factorial).
- What does ! (factorial) mean in real terms? Well, we know that n is the 
  number of elements, and ! just means we multiply a series of descending numbers.
- Lets look at an example of n!: Given a string "ABC" how many characters can 
  be placed in the first position? 3. How many can be placed in the second 
  position? 2 (assume we have already placed a character at the first position). 
  How many can be placed in the last position? 1. 
  So n! for "ABC" is simply: 3x2x1 = 6. See how that works? We just take the 
  number of available characters for each position, then multiply.
- So how do we work out how many possible permutations there are when repetition
  is not allowed? Answer: n!/2!^k
  What is k in that formula? k is the number of repeated elements in the input. 
  Example: "AAB" has n!, or 3x2x1, permutations. So the total permutations are 6. 
  Without repetition allowed the formula is: 3x2x1 / 2^1. k is 1 as "A" is the 
  only repeated character. So the total permutations for "AAB" without repetition 
  is 3x2x1 / 2^1 = 6 / 2 = 3
  
  
"""


def get_string_permutations(s: str | t.List[str], step: int = 0) -> list[str]:
    permutations = []
    if step == len(s):
        permutations.append("".join(s))

    for i in range(step, len(s)):
        s_copy = [c for c in s]
        s_copy[step], s_copy[i] = s_copy[i], s_copy[step]
        permutations.extend(get_string_permutations(s_copy, step + 1))

    return permutations


def main():
    # String permutations. Itertool's perm is a generator and returns (b, a, c)
    perms = get_string_permutations("123")
    perms_builtin = ["".join(item) for item in itertools.permutations("abc")]
    """
    Number of chars = N of chars in the original string - permutations
    ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """
    print(perms)
    print(perms_builtin)


if __name__ == "__main__":
    main()
