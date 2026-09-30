"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/dp/step_climb.py until you're done.

Problem (Climbing Stairs, LeetCode 70):

You're climbing a staircase with k steps. Each time you can climb
either 1 or 2 steps. In how many distinct ways can you climb to the
top?

Example:
  k=1 -> 1
  k=2 -> 2  (1+1, or 2)
  k=3 -> 3  (1+1+1, 1+2, 2+1)
  k=5 -> 8

Write your solution below. Try at least one DP approach (top-down
memoized recursion, or bottom-up tabulation) — your choice.
"""


def climb(k):
    memo = {}
    return climb_rec(k, memo)

def climb_rec(k, memo):
    if k == 1 or k ==2:
        result = k
    elif k in memo:
        result = memo[k]
    else:
        result = climb_rec (k-1, memo) + climb_rec(k-2, memo)
        memo[k] = result

    return result

def climb1(k):
    if k <=2:
        return k

    dp = [0]*(k+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, k+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[k]




if __name__ == "__main__":
    # add your own test calls here once implemented
    pass
