'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
'''


class Solution:

    # Seems to be right but exceeds time limit as its
    def validPalindrome(self, s: str) -> bool:

        def _check_if_str_palindrom(s: str) -> bool:
            return s == s[::-1]

        for i in range(len(s)):
            s_minus_one_char = s[: i] + s[i + 1:]
            if _check_if_str_palindrom(s_minus_one_char):
                return True
        return False

    # Mine, doesn't seem to work
    def validPalindrome(self, s: str) -> bool:
        length = len(s)
        left, right = 0, length - 1

        one_error_pass_granted = False
        while left <= right:
            char_left = s[left]
            char_right = s[right]

            if char_left == char_right:
                left += 1
                right -= 1
                continue

            if not one_error_pass_granted and length > 3:
                one_error_pass_granted = True
                left += 1
                right -= 1
                continue
            else:
                return False

        return True

    def validPalindrome(self, s: str) -> bool:

        def _check_if_palindrom(s: str, left: int, right: int) -> bool:
            if not s or len(s) == 1:
                return True
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        '''
        Let's assume we have some string s = 'abbxa'. On its own, s is not a 
        palindrome. However, if we delete the 'x', then s becomes 'abba', which
        is a palindrome. If we use the same algorithm in checkPalindrome, we 
        will see that the first and last characters match as 'a'. The pointers
        move inwards, and the "new" string we're focused on is 'bbx'.

        The next check will be a mismatch - 'b' != 'x'. This means that our 
        original string is not a palindrome. However, we can delete one 
        character. If s can be a palindrome after one deletion, the deletion 
        must be of one of these mismatched characters. Deleting the character
        'b' gives us 'bx', and deleting the character 'x' gives us 'bb'. 
        Because 'bb' is a palindrome (which we can verify using 
        checkPalindrome), the original string 'abbxa' can become a palindrome 
        with at most one character deletion.
        
        This leaves us two scenarios:
        1. s is a palindrome - great, we can just return true.
        2. Somewhere in s, there will be a pair of mismatched characters. 
           We must use our allowed deletion on one of these characters. Try 
           both options - if neither results in a palindrome, then return 
           false. Otherwise, return true. We can "delete" the character at 
           j by moving our bounds to (i, j - 1). Likewise, we can "delete" 
           the character at i by moving our bounds to (i + 1, j).
        
        ! In short, we attempt to skip the mismatched chars from left and right
        and see whether it results in a valid palindrom
        '''
        left, right = 0, len(s) - 1
        while left < right:
            # If the chars mismatch, we need to check whether deletion of
            # either of them results in a palindrom anyway
            if s[left] != s[right]:
                return (
                        _check_if_palindrom(s, left + 1, right)
                        or _check_if_palindrom(s, left, right - 1)
                )
            left += 1
            right -= 1
        return True




def main():
    s = "racecar"
    # s = "keksskek"
    print(Solution().validPalindrome(s))


if __name__ == '__main__':
    main()
