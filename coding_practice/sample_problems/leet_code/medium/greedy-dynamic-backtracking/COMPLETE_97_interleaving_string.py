import typing


"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/interleaving-string/

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving 
of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are 
divided into n and m non-empty substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
"""


class Solution:

    '''
    D&C Brute Force. TLE 66 / 1o6 tests
    '''
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        def _interleave(
            curr_s1: int, curr_s2: int, curr_interleave: list[str]
        ) -> bool:

            if (
                "".join(curr_interleave) == s3
                and curr_s1 == len(s1)
                and curr_s2 == len(s2)
            ):
                return True

            if curr_s1 < len(s1):
                if _interleave(curr_s1 + 1, curr_s2, curr_interleave + [s1[curr_s1]]):
                    return True

            if curr_s2 < len(s2):
                if _interleave(curr_s1, curr_s2 + 1, curr_interleave + [s2[curr_s2]]):
                    return True

            return False

            # # Base cases
            # TODO: Fix the base case and check if looping works as ^
            # if len(curr_interleave) == len(s3):
            #     return "".join(curr_interleave) == s3
            #
            # if curr_s1 == len(s1) or curr_s2 == len(s2):
            #     return False
            #
            # # Probe the solution space
            # for i in range(curr_s1, len(s1)):
            #     curr_interleave.append(s1[i])
            #
            #     for j in range(curr_s2, len(s2)):
            #         curr_interleave.append(s2[j])
            #         if _interleave(i + 1, j + 1, curr_interleave):
            #             return True
            #         curr_interleave.pop()
            #
            #     curr_interleave.pop()
            #
            # return False

        if len(s1) + len(s2) < len(s3):
            return False

        return _interleave(0, 0, [])


def main():
    print(Solution().isInterleave(
        s1="aabcc",
        s2="dbbca",
        s3="aadbbcbcac"
    ))


if __name__ == '__main__':
    main()
