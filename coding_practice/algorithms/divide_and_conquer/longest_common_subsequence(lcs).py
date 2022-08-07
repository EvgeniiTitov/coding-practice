import typing as t


"""
The Longest Common Sequence (LCS)

Given 2 strings: s1 and s2
Find the length of the longest subsequence common to both strings

Subsequence - a sequence that can be derived from another sequence by deleting
some elements without changing their relative order

Example 1:
s1 = elephant
s2 = erepat
output = 5 (eepat)

_______________________________________________________________________________

2 things can happen. Chars at index N could either:
    - match
    If match, count it and continue
    
    - mismatch
    If mismatch, we have 2 options: 
        - Skip char in str1 and keep looking for the str2's char 
        - Skip char in str2 and keep looking for the str1's char
        
        return the option which results in the largest LCS
"""


def get_lcs(str1: str, str2: str, index1: int = 0, index2: int = 0) -> int:
    # Base condition - end of either string is reached
    if index1 == len(str1) or index2 == len(str2):
        return 0

    # If chars match, keep going
    if str1[index1] == str2[index2]:
        return 1 + get_lcs(str1, str2, index1 + 1, index2 + 1)
    # If chars mismatch, consider possibilities
    else:
        option1 = get_lcs(str1, str2, index1 + 1, index2)
        option2 = get_lcs(str1, str2, index1, index2 + 1)
        # option3 = get_lcs(str1, str2, index1 + 1, index2 + 1)
        return max(option1, option2)


def main():
    print(get_lcs("elephant", "erepat"))


if __name__ == '__main__':
    main()
