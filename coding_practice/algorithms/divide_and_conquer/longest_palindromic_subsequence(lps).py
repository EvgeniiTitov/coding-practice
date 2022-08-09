import typing as t


"""
The Longest Palindromic Subsequence (LPS)

Given a str
Find the longest palindromic subsequence

Subsequence - a sequence that can be derived from another sequence by deleting
some elements without changing their relative order

Palindrome - a str that reads the same backwards

Example:
s = ELRMENMET
Output = 5
LPS: EMEME

Example:
s = AMEEWMEA
Output = 6
LPS: AMEEMA
_______________________________________________________________________________

Start at both ends. The base case is when the pointers have crossed each other.

If chars at both ends match: counter + 2 and consider the remaining substring,
i.e. string[left + 1: right - 1]

If chars do not match, we could either:
    - Skip the one on the left: string[left + 1, right]
    - Skip the one on the right: string[left: right - 1]
    Pick the one which results in the greatest value
"""


def get_lps(string: str, left: int, right: int) -> int:
    # Base cases
    # length = len(string)
    # if left >= right and not length % 2:
    #     return 0
    # elif left >= right and length % 2:
    #     return 1

    # ^ Could be simplified to:
    if left > right:  # Even length
        return 0
    elif left == right:  # Odd length
        return 1

    if string[left] == string[right]:
        return 2 + get_lps(string, left + 1, right - 1)
    else:
        option1 = get_lps(string, left + 1, right)
        option2 = get_lps(string, left, right - 1)
        return max(option1, option2)


def main():
    string = "AMEEWMEA"
    # string = "ELRMENMET"
    print(get_lps(string, 0, len(string) - 1))


if __name__ == "__main__":
    main()
