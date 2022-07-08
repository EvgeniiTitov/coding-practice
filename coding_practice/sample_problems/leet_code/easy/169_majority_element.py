from typing import List


"""
Summary: 
    Brute force: iterate over numbers, counting how many times each appears
    (defaultdict), then return the one that appears the most.
    
------------------------------------------------------------------------------

https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than [n / 2] times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2


The constant space solution:
Intuition

If we had some way of counting instances of the majority element as +1 and 
instances of any other element as -1, summing them would make it obvious that 
the majority element is indeed the majority element.

Algorithm

Essentially, what Boyer-Moore does is look for a suffix suf of nums where 
suf[0] is the majority element in that suffix. To do this, we maintain a 
count, which is incremented whenever we see an instance of our current 
candidate for majority element and decremented whenever we see anything else. 
Whenever count equals 0, we effectively forget about everything in nums up 
to the current index and consider the current number as the candidate for 
majority element. It is not immediately obvious why we can get away with 
forgetting prefixes of nums - consider the following examples 
(pipes are inserted to separate runs of nonzero count).

[7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]

Here, the 7 at index 0 is selected to be the first candidate for majority 
element. count will eventually reach 0 after index 5 is processed, so the 
5 at index 6 will be the next candidate. In this case, 7 is the true majority 
element, so by disregarding this prefix, we are ignoring an equal number of 
majority and minority elements - therefore, 7 will still be the majority 
element in the suffix formed by throwing away the first prefix.

[7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 5, 5, 5, 5]

Now, the majority element is 5 (we changed the last run of the array from 7s 
to 5s), but our first candidate is still 7. In this case, our candidate is not
the true majority element, but we still cannot discard more majority elements 
than minority elements (this would imply that count could reach -1 before we 
reassign candidate, which is obviously false).

Therefore, given that it is impossible (in both cases) to discard more majority
elements than minority elements, we are safe in discarding the prefix and 
attempting to recursively solve the majority element problem for the suffix. 
Eventually, a suffix will be found for which count does not hit 0, and the 
majority element of that suffix will necessarily be the same as the majority 
element of the overall array.
"""


class Solution:

    # COOL! T: O(n), S: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

    # T: O(n2)
    def majorityElement(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        number_out, most_times_seen = 0, 0

        for unique_num in unique_nums:  # O(n)
            times_seen = nums.count(unique_num)  # O(n)

            if times_seen > most_times_seen:
                number_out = unique_num
                most_times_seen = times_seen

        return number_out

    # T: O(n)
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict

        nums_seen = defaultdict(int)
        for num in nums:
            nums_seen[num] += 1

        most_seen_number, times = None, 0
        for number, times_seen in nums_seen.items():
            if times_seen > times:
                most_seen_number = number
                times = times_seen
        return most_seen_number

    # This exceeded the time limit lol
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

    # O(n) for space and time, not quite fair as well
    def majorityElement(self, nums: List[int]) -> int:
        import collections

        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


def main():
    numbers = [
        47,
        47,
        72,
        47,
        72,
        47,
        79,
        47,
        12,
        92,
        13,
        47,
        47,
        83,
        33,
        15,
        18,
        47,
        47,
        47,
        47,
        64,
        47,
        65,
        47,
        47,
        47,
        47,
        70,
        47,
        47,
        55,
        47,
        15,
        60,
        47,
        47,
        47,
        47,
        47,
        46,
        30,
        58,
        59,
        47,
        47,
        47,
        47,
        47,
        90,
        64,
        37,
        20,
        47,
        100,
        84,
        47,
        47,
        47,
        47,
        47,
        89,
        47,
        36,
        47,
        60,
        47,
        18,
        47,
        34,
        47,
        47,
        47,
        47,
        47,
        22,
        47,
        54,
        30,
        11,
        47,
        47,
        86,
        47,
        55,
        40,
        49,
        34,
        19,
        67,
        16,
        47,
        36,
        47,
        41,
        19,
        80,
        47,
        47,
        27,
    ]
    print(Solution().majorityElement(numbers))


if __name__ == "__main__":
    main()
