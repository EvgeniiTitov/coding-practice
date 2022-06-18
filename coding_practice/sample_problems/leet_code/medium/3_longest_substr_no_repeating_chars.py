"""
Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""


class Solution:

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
