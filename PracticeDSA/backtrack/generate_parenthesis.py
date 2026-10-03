from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generates all valid combinations of n pairs of parentheses.

        Discussion Summary:
        - Time Complexity: O(4^N / sqrt(N)) which corresponds to the n-th Catalan number.
          Each valid sequence has length 2n.
        - Space Complexity: O(N) for the maximum recursion stack depth, plus O(4^N / sqrt(N)) to store results.
        - Optimization Note: Currently uses string concatenation (`cur + '('`), which creates a new
          immutable string per call. To optimize overhead, we could use a mutable list (`cur.append('(')`),
          but you MUST backtrack by calling `cur.pop()` after the recursive call returns!

        State Constraints:
        - Add '(' if open_count < n
        - Add ')' if close_count < open_count
        """
        result = []
        self.gen_rec("", result, n, 0, 0)
        return result

    def gen_rec(self, cur, result, n, oc, cc):
        if len(cur) == 2 * n:
            result.append(cur)
            return

        if oc < n:
            self.gen_rec(cur + "(", result, n, oc + 1, cc)

        if cc < oc:
            self.gen_rec(cur + ")", result, n, oc, cc + 1)


if __name__ == "__main__":
    sol = Solution()

    fixed_cases = {
        1: ["()"],
        2: ["(())", "()()"],
        3: ["((()))", "(()())", "(())()", "()(())", "()()()"],
    }
    for n, expected in fixed_cases.items():
        got = sol.generateParenthesis(n)
        assert sorted(got) == sorted(expected), (
            f"n={n}: expected {sorted(expected)}, got {sorted(got)}"
        )
    print("fixed cases passed")

    def is_valid(s):
        balance = 0
        for ch in s:
            balance += 1 if ch == "(" else -1
            if balance < 0:
                return False
        return balance == 0

    for n in range(1, 7):
        results = sol.generateParenthesis(n)
        assert len(results) == len(set(results)), f"n={n}: duplicates found"
        for s in results:
            assert len(s) == 2 * n, f"n={n}: {s!r} has wrong length"
            assert is_valid(s), f"n={n}: {s!r} is not valid"
    print("validity + no-duplicates checks passed for n=1..6")
