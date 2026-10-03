"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/backtrack/generate_parenthesis.py until you're done.

Problem (Generate Parentheses, LeetCode 22):

Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.

Example:
  n = 3 -> ["((()))","(()())","(())()","()(())","()()()"]
  n = 1 -> ["()"]

Write your solution below.
"""


def generate_parenthesis(n):
    result = []
    backtrack(n, 0,0, [], result)
    return result

def backtrack(n,o_cnt,c_cnt, cur_result, global_result):

    if len(cur_result) == 2*n:
        cur = "".join(cur_result)
        global_result.append(cur)
        return

    if o_cnt < n:
        cur_result.append('(')
        backtrack(n, o_cnt+1, c_cnt, cur_result, global_result)
        cur_result.pop()

    if c_cnt < o_cnt:
        cur_result.append(')')
        backtrack(n, o_cnt, c_cnt+1, cur_result, global_result)
        cur_result.pop()


if __name__ == "__main__":
    fixed_cases = {
        1: ["()"],
        2: ["(())", "()()"],
        3: ["((()))", "(()())", "(())()", "()(())", "()()()"],
    }
    for n, expected in fixed_cases.items():
        got = generate_parenthesis(n)
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

    for n in range(0, 7):
        results = generate_parenthesis(n) if n > 0 else [""]
        if n == 0:
            continue
        assert len(results) == len(set(results)), f"n={n}: duplicates found"
        for s in results:
            assert len(s) == 2 * n, f"n={n}: {s!r} has wrong length"
            assert is_valid(s), f"n={n}: {s!r} is not valid"
    print("validity + no-duplicates checks passed for n=1..6")
