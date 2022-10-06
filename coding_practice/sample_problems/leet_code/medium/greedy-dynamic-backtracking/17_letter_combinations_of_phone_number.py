from typing import List


"""
Summary:
    Brute force: Tree like approach again, for each char consider all other chars
_______________________________________________________________________________

https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given 
below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
"""


class Solution:

    # Brute force. T: O(2 ^ N); S: O(N)
    def letterCombinations(self, digits: str) -> List[str]:

        def _generate_combinations(
            curr_index: int,
            curr_combination: List[str],
            combinations: List[str]
        ) -> None:
            # Base case
            if curr_index == length:
                combinations.append("".join(curr_combination))
                return

            # Generate combinations
            digit = digits[curr_index]
            chars = num_chars_mapping[digit]
            for char in chars:
                curr_combination.append(char)
                _generate_combinations(
                    curr_index + 1, curr_combination, combinations
                )
                curr_combination.pop()

        num_chars_mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        length = len(digits)
        if length == 0:
            return []
        elif length == 1:
            return list(num_chars_mapping.get(digits[0]))

        combinations = []
        _generate_combinations(0, [], combinations)
        return combinations


def main():
    print(Solution().letterCombinations(digits="2345"))


if __name__ == '__main__':
    main()
