"""
TODO: TBC - Don't understand the proper way
"""


class Solution:

    # My brute force - slow (O(n2))
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if len(s) == 1:
            return s

        def is_string_a_palindrom(s: str) -> bool:
            return s == s[::-1]

        s_length = len(s)
        longest_poli_substr = s[0]  # fair to assume that
        for i in range(s_length):
            for j in range(i + 1, s_length):
                substring = s[i : j + 1]
                substring_length = len(substring)

                if substring_length < len(longest_poli_substr):
                    continue

                if is_string_a_palindrom(substring):
                    longest_poli_substr = substring

        return longest_poli_substr

    def longestPalindrome(self, s: str) -> str:

        if not s:
            return s
        if len(s) == 1:
            return s

        def expand_around_centre(s: str, left: int, right: int) -> int:
            """
            Move pointers left and right as long as the values of left and
            right are the same
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start, end = 0, 0
        for i in range(len(s)):
            len_1 = expand_around_centre(s, i, i)
            len_2 = expand_around_centre(s, i, i + 1)
            length = max(len_1, len_2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start : end + 1]


def main():
    s = "cbbd"
    print(Solution().longestPalindrome(s))


if __name__ == "__main__":
    main()
