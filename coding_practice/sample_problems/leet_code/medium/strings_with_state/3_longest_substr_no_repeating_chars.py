

"""
Summary:
_______________________________________________________________________________

https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating 
characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not
a substring.
"""


class Solution:

    # My brute force. TLE: 986 / 987 test cases passed.
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        def _check_len_and_if_repeated_chars(string: str) -> tuple[bool, int]:
            set_string = set(string)
            has_repeated = not (len(string) == len(set_string))
            return has_repeated, len(set_string)

        max_len = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_string = s[i: j + 1]

                has_repeated, length = _check_len_and_if_repeated_chars(
                    sub_string
                )
                if has_repeated:
                    continue
                max_len = max(max_len, length)

        return max_len

    # My brute force - slow (O(n2)) and takes a lot of memory
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        if len(s) == 1:
            return 1

        longest_substrings = []
        for i in range(len(s)):
            longest_substring = set()
            for char in s[i:]:
                if char not in longest_substring:
                    longest_substring.add(char)
                else:
                    break
                longest_substrings.append(
                    (len(longest_substring), longest_substring)
                )
        longest_substrings.sort(key=lambda e: e[0])
        return longest_substrings[-1][0]

    # Suggested brute force - super shit (O(n3)), exceeded time limit
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True

        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res

    # SMART - sliding window approach (O(n))
    # We maintain a window (2 pointers, left and right). We increase the window
    # until we meet a duplicate character, then we contract it (from left) till
    # there are no duplicates
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        # This list represents all characters within the window. We update its
        # values as we move the pointers
        characters = [0] * 128

        s_len = len(s)
        left, right = 0, 0
        longest_str = 0

        while right < s_len:
            char_right = s[right]
            char_right_ascii_value = ord(char_right)
            characters[char_right_ascii_value] += 1

            # Contract the window
            while characters[char_right_ascii_value] > 1:
                char_left = s[left]
                char_left_ascii_value = ord(char_left)
                characters[char_left_ascii_value] -= 1
                left += 1

            # Update max window size
            longest_str = max(longest_str, right - left + 1)

            # Expand the window
            right += 1

        return longest_str


def main():
    s = "abcabcbb"
    # s = "bbbb"
    # s = "au"
    print(Solution().lengthOfLongestSubstring(s))


if __name__ == "__main__":
    main()
