from typing import List


"""
Summary: Town judge's outdegree is 0, whereas indegree is n - 1!
_______________________________________________________________________________

https://leetcode.com/problems/find-the-town-judge/

In a town, there are n people labeled from 1 to n. There is a rumor that one 
of these people is secretly the town judge.

If the town judge exists, then:
- The town judge trusts nobody.
- Everybody (except for the town judge) trusts the town judge.
- There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that 
the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be 
identified, or return -1 otherwise.

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
"""


class Solution:
    # T: O(N); S: O(N)
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # This bit is required in case we know there are N people and yet we
        # have no trust info
        if not len(trust):
            if n == 1:
                return n
            else:
                return -1

        people_who_trust = set()
        trusted_people = []
        for pair in trust:
            people_who_trust.add(pair[0])
            trusted_people.append(pair[1])

        from collections import defaultdict

        trust_numbers = defaultdict(int)
        for person in trusted_people:
            trust_numbers[person] += 1

        for trusted_person, n_of_trusts in trust_numbers.items():
            if n_of_trusts == n - 1 and trusted_person not in people_who_trust:
                return trusted_person
        return -1

    # Same ^ but a bit shorter
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not len(trust):
            if n == 1:
                return n
            else:
                return -1

        from collections import defaultdict

        trust_numbers_per_person = defaultdict(int)
        people_who_trust = set()

        for pair in trust:
            people_who_trust.add(pair[0])
            trust_numbers_per_person[pair[-1]] += 1

        for trusted_person, n_of_trusts in trust_numbers_per_person.items():
            if trusted_person not in people_who_trust and n_of_trusts == n - 1:
                return trusted_person
        return -1
