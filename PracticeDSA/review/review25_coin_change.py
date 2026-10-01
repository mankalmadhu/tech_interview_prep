"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/dp/coin_change.py until you're done.

Problem (Coin Change, LeetCode 322):

Given a list of coin denominations and a target amount, return the
minimum number of coins needed to make up that amount exactly.
If it's not possible, return -1. You have an unlimited supply of
each coin denomination.

Recurrence: dp[i] = min over all coins c <= i of (1 + dp[i - c])
Base case:  dp[0] = 0
Impossible subproblems should be treated as +infinity internally so
they never win a min() comparison; convert back to -1 at the end.

Example:
  coins = [1, 2, 5], amount = 11 -> 3  (5 + 5 + 1)
  coins = [2], amount = 3        -> -1 (impossible)
  coins = [1], amount = 0        -> 0

Write your solution below (top-down memoization or bottom-up tabulation).
"""


def coin_change(coins, amount):
    memo = [-1]*(amount+1)
    coin_change_rec(coins, memo, amount)
    return memo[amount] if memo[amount] != float('inf') else -1


def coin_change_rec(coins, memo, amount):

    if amount < 0:
        return float('inf')

    if amount == 0:
        memo[amount] = 0
        return 0

    if memo[amount] != -1:
        return memo[amount]

    min_amount = float('inf')

    for c in coins:
        result = coin_change_rec(coins,memo, amount - c) +1
        min_amount = min(result,min_amount)

    memo[amount] = min_amount

    return memo[amount]

def coin_change_it(coins, amount):

    dp = [float('inf')] * (amount+1)
    dp[0] = 0

    for i in range(1, amount+1):
        for coin in coins:
            if coin > i:
                continue
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    fixed_cases = [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([1, 2, 5], 100, 20),
        ([186, 419, 83, 408], 6249, 20),
    ]
    for coins, amount, expected in fixed_cases:
        got = coin_change(coins, amount)
        assert got == expected, f"coins={coins}, amount={amount}: expected {expected}, got {got}"
    print("fixed cases passed")

    import random
    from collections import deque

    def brute_force(coins, amount):
        if amount == 0:
            return 0
        visited = {0}
        queue = deque([(0, 0)])
        while queue:
            total, steps = queue.popleft()
            for c in coins:
                nxt = total + c
                if nxt == amount:
                    return steps + 1
                if nxt < amount and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
        return -1

    for _ in range(300):
        coins = random.sample(range(1, 15), random.randint(1, 4))
        amount = random.randint(0, 40)
        got = coin_change(coins, amount)
        got_it = coin_change_it(coins, amount)
        want = brute_force(coins, amount)
        assert got == want, f"coins={coins}, amount={amount}: expected {want}, got {got}"
        assert got_it == want, f"coins={coins}, amount={amount}: expected {want}, got {got_it}"
    print("300 randomized trials passed (top-down + bottom-up)")
