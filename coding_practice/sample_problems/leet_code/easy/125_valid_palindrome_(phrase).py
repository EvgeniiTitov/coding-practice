import typing as t


"""
Summary: str.isalnum() is crucial to cleanse the string for a head-on solution
with str == str[::-1]
To solve it in constant space use 2 pointers, when encounter a non-alphanumeric
char, just skip it by incrementing left or decrementing right.
_______________________________________________________________________________

https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the 
same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


class Solution:
    # T: O(N); S: O(N)
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True

        def _preprocess_string(s: str) -> str:
            s_out = []
            for char in s:
                if char.isalnum():
                    s_out.append(char.lower())
            return "".join(s_out)

        str_cleaned = _preprocess_string(s)
        return str_cleaned == str_cleaned[::-1]

    # Pointers based. T: O(N); S: O(1)
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True

        left, right = 0, len(s) - 1
        # Don't care about mid element for odd len, still palindrome
        while left < right:
            left_char = s[left]
            if not left_char.isalnum():
                left += 1
                continue

            right_char = s[right]
            if not right_char.isalnum():
                right -= 1
                continue

            if left_char.lower() != right_char.lower():
                return False
            left += 1
            right -= 1
        return True


def main():
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))


if __name__ == '__main__':
     main()
