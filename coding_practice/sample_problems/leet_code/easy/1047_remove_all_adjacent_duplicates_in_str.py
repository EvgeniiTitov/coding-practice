import typing as t


"""
Summary: The most efficient solution would require to be able to see chars
before a pair you popped, stack does this job well. You iterate over chars, if
the last value on the stack is the same, pop it off the stack - now you handled
a pair. In the stack you have a char coming before the popped pair and a new 
char during your iteration, so you get to compare again.
_______________________________________________________________________________

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

You are given a string s consisting of lowercase English letters. A duplicate 
removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. 
It can be proven that the answer is unique.

 

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent 
and equal, and this is the only possible move.  The result of this move is 
that the string is "aaca", of which only "aa" is possible, so the final 
string is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay"
"""


class Solution:
    # Time Limit Exceeded
    def removeDuplicates(self, s: str) -> str:
        s = list(s)

        def _dedup(s: list) -> str:
            found_pair = True
            while found_pair:
                s_copy = s[:]
                for i in range(len(s_copy) - 1):
                    char1 = s[i]
                    char2 = s[i + 1]
                    if char1 == char2:
                        s.pop(i)
                        s.pop(i)  # !! Since it shifts right !!
                        break
                else:
                    found_pair = False

            return "".join(s)

        return _dedup(s)

    # Time Limit Exceeded
    def removeDuplicates(self, s: str) -> str:
        s = list(s)

        found_pair = True
        while found_pair:
            for i in range(len(s) - 1):
                char1 = s[i]
                char2 = s[i + 1]
                if char1 == char2:
                    s.pop(i)
                    s.pop(i)
                    break
            else:
                found_pair = False
        return "".join(s)

    def removeDuplicates(self, s: str) -> str:
        out = []
        for char in s:
            if len(out) and char == out[-1]:
                out.pop()
            else:
                out.append(char)
        return "".join(out)


def main():
    # s = "aababaab"
    s = "abbaca"
    print(Solution().removeDuplicates(s))


if __name__ == "__main__":
    main()
