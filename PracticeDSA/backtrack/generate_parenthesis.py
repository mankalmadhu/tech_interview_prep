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
        self.gen_rec('', result, n, 0, 0)
        return result

    def gen_rec(self, cur, result, n, oc, cc):
        if len(cur) == 2 * n:
            result.append(cur)
            return
        
        if oc < n:
            self.gen_rec(cur + '(', result, n, oc + 1, cc)
        
        if cc < oc:
            self.gen_rec(cur + ')', result, n, oc, cc + 1)
