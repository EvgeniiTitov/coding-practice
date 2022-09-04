import typing as t


"""
Summary:
    - To check whether s2 has enough chars for s1 (char frequency) could be done
    much smarter: len(s1) > len(s2) haha, instead of loops and the dict.
    
    - The sliding window approach is much efficient then generating all
    permutations. The idea is you slide through the s2, the window size == len(s1),
    if the char frequency is the same --> one of the permutations.
_______________________________________________________________________________

https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""


class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # One string is a permutation of the other if their char frequencies
        # are the same + sliding window technique.
        s1_length = len(s1)
        s2_length = len(s2)

        if s1_length > s2_length:
            return False

        from collections import Counter
        s1_chars = Counter(s1)
        for i in range(s2_length - s1_length + 1):
            s2_sub_string = s2[i: s1_length + i]
            s2_sub_string_chars = Counter(s2_sub_string)
            if s1_chars == s2_sub_string_chars:
                return True

        return False

    # My attempt 1 - Time Limit Exceeded. (~30 tests)
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # No need to keep track of permutations, so just 2 parameters
        def _generate_permutations(s: list[str], curr_perm: list[str]) -> bool:
            # Base case
            if not len(s):
                result_str = "".join(curr_perm)
                return True if result_str in s2 else False

            # Iterate over available chars generating permutations
            for i in range(len(s)):
                curr_char = s[i]
                remaining_chars = s[: i] + s[i+1:]
                curr_perm.append(curr_char)
                if _generate_permutations(remaining_chars, curr_perm):
                    return True
                curr_perm.pop()

            return False

        return _generate_permutations(list(s1), [])

    # Adding char frequency check improved the performance - TLE (~69 tests)
    def checkInclusion(self, s1: str, s2: str) -> bool:

        from collections import defaultdict

        def _get_char_frequency(s: str) -> dict:
            char_freq = defaultdict(int)
            for char in s:
                char_freq[char] += 1
            return char_freq

        s1_char_freq_map = _get_char_frequency(s1)
        s2_char_freq_map = _get_char_frequency(s2)
        for char, char_freq in s1_char_freq_map.items():
            s2_char_freq = s2_char_freq_map.get(char)
            if not s2_char_freq or s2_char_freq < char_freq:
                return False

        # No need to keep track of permutations, so just 2 parameters
        def _generate_permutations(s: list[str],
                                   curr_perm: list[str]) -> bool:
            # Base case
            if not len(s):
                result_str = "".join(curr_perm)
                return True if result_str in s2 else False

            # Iterate over available chars generating permutations
            for i in range(len(s)):
                curr_char = s[i]
                remaining_chars = s[: i] + s[i + 1:]
                curr_perm.append(curr_char)
                if _generate_permutations(remaining_chars, curr_perm):
                    return True
                curr_perm.pop()

            return False

        return _generate_permutations(list(s1), [])


def main():
    print(Solution().checkInclusion(
        s1="ab",
        s2="eidboaooab"
    ))


if __name__ == '__main__':
    main()
