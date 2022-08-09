import typing as t


"""
Summary: 2 pointers. Your state is the N of chars between the pointers, you 
keep checking if K can handle total_chars_in_window - most_popular char. If it 
cannot, move left once.
IMPORTANT, right pointer moves every iteration, even when we move the left.
_______________________________________________________________________________

https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the 
string and change it to any other uppercase English character. You can perform t
his operation at most k times.

Return the length of the longest substring containing the same letter you can 
get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""


class Solution:
    # Head on brute force - time limit as its super inefficient
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        def _check_if_valid(s: str) -> bool:
            chars_count = defaultdict(int)
            for char in s:
                chars_count[char] += 1
            if len(chars_count) <= 1:
                return True

            counts = sorted(list(chars_count.values()))
            fixes = k
            while fixes > 0:
                if len(counts) == 1:
                    return True
                char_count = counts.pop(0)
                fixes -= char_count
            return True if len(counts) == 1 and fixes >= 0 else False

        length = len(s)
        longest_substr = 0
        for i in range(length):
            for j in range(i + 1, length):
                is_valid = _check_if_valid(s[i : j + 1])
                if is_valid:
                    longest_substr = max(longest_substr, j - i + 1)
        return longest_substr

    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        if length == 1:
            return 1

        chars_between_pointers = {}
        longest_substr = 0
        left = right = 0
        while right < length:
            char_at_right = s[right]

            # State
            if char_at_right not in chars_between_pointers:
                chars_between_pointers[char_at_right] = 0
            chars_between_pointers[char_at_right] += 1

            # If K can still cover the window
            char_at_left = s[left]
            n_chars_in_window = right - left + 1
            if n_chars_in_window - max(chars_between_pointers.values()) <= k:
                longest_substr = max(longest_substr, n_chars_in_window)
            else:
                chars_between_pointers[char_at_left] -= 1
                if not chars_between_pointers[char_at_left]:
                    chars_between_pointers.pop(char_at_left)
                left += 1
            right += 1
        return longest_substr


def main():
    print(Solution().characterReplacement("AABABBA", k=1))


if __name__ == "__main__":
    main()
