from typing import List


"""
Summary: 
    Brute force - generate all possible solutions, then pick just the valid 
    ones. Very slow. Tree like structure. 

    Backtracking - generate only valid solutions discarding anything that
    cannot be valid - much quicker. All comes down to coming up with the logic
    that would let you to keep track of whether the current solution is still
    valid
_______________________________________________________________________________

https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""


class Solution:

    # Brute force - very close but accepted (214 ms). T: O ((2 ^ 2N) N)
    # The problem here we generate all solutions, we could discard invalid ones
    def generateParenthesis(self, n: int) -> List[str]:

        def _validate_solution(solution: List[str]) -> bool:
            stack = []
            for brace in solution:
                if brace == "(":
                    stack.append(brace)
                else:
                    if not len(stack):
                        return False
                    if stack.pop() != "(":
                        return False
            return not len(stack)

        def _generate_solutions(
            curr_solution: List[str],
            solutions: List[str]
        ) -> None:
            # Base case
            if len(curr_solution) == nb_parentheses:
                if _validate_solution(curr_solution):
                    solutions.append("".join(curr_solution))
                return

            for char in "()":
                curr_solution.append(char)
                _generate_solutions(curr_solution, solutions)
                curr_solution.pop()

        if n == 0:
            return []
        elif n == 1:
            return ["()"]

        nb_parentheses = n * 2
        solutions = []
        _generate_solutions([], solutions)
        return solutions

    # Backtracking (30 ms).
    def generateParenthesis(self, n: int) -> List[str]:

        def _generate_solutions(
            curr_solution: List[str],
            open: int,
            close: int,
            solutions: List[str]
        ) -> None:

            if len(curr_solution) == nb_parentheses:
                solutions.append("".join(curr_solution))
                return

            if open < n:
                curr_solution.append("(")
                _generate_solutions(curr_solution, open + 1, close, solutions)
                curr_solution.pop()

            if close < open:
                curr_solution.append(")")
                _generate_solutions(curr_solution, open, close + 1, solutions)
                curr_solution.pop()

        if n == 0:
            return []
        elif n == 1:
            return ["()"]

        nb_parentheses = n * 2
        solutions = []
        _generate_solutions([], 0, 0, solutions)
        return solutions


def main():
    print(Solution().generateParenthesis(
        n=3
    ))


if __name__ == '__main__':
    main()
