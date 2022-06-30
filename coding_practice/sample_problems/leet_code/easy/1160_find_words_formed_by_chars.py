from typing import List


"""
Sumarry:
_______________________________________________________________________________

https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars 
(each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer 
is 3 + 3 = 6.

Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the 
answer is 5 + 5 = 10.
"""


class Solution:
    # T: O(N2); S: O(N)
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import defaultdict
        available_char = defaultdict(int)
        for char in chars:
            available_char[char] += 1

        sum_of_good_strings = 0
        for word in words:
            word_chars = defaultdict(int)
            for char in word:
                word_chars[char] += 1

            is_good = True
            for char, times_used in word_chars.items():
                if char not in available_char:
                    is_good = False
                    break
                char_availability = available_char[char]
                if times_used > char_availability:
                    is_good = False
                    break

            if is_good:
                sum_of_good_strings += len(word)

        return sum_of_good_strings

    # Slight optimisation
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import defaultdict
        available_char = defaultdict(int)
        for char in chars:
            available_char[char] += 1

        chars_available = set(chars)
        sum_of_good_strings = 0
        for word in words:

            if not len(chars_available.intersection(set(word))):
                continue

            word_chars = defaultdict(int)
            for char in word:
                word_chars[char] += 1
            is_good = True
            for char, times_used in word_chars.items():
                if char not in available_char:
                    is_good = False
                    break
                char_availability = available_char[char]
                if times_used > char_availability:
                    is_good = False
                    break

            if is_good:
                sum_of_good_strings += len(word)

        return sum_of_good_strings

    # From solutions
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = 0
        for w in words:
            included = True
            charsList = [c for c in chars]
            for c in w:
                if c in charsList:
                    charsList.remove(c)
                else:
                    included = False
                    break
            if included: counter = counter + len(w)
        return counter