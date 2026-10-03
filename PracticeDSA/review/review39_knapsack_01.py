"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/dp/knapsack_01.py until you're done.

Problem (0/1 Knapsack):

You are given n items, each with a weight and a value. You have a
knapsack that can carry at most `capacity` total weight. For each
item, you can either take it whole (once) or leave it — you cannot
take a fraction of an item, and you cannot take it more than once.

Maximize the total value of items you can carry without exceeding
the capacity.

Example:
  values  = [10, 40, 30]
  weights = [5, 4, 6]
  capacity = 10
  -> 70 (take items with weight 4 and 6: value 40+30=70)

Write your solution below.
"""


def knapsack_01(values, weights, capacity):
    n = len(values)
    memo = [[-1] * (capacity + 1) for _ in range(n + 1)]

    return knapsack_rec(values, weights, capacity, memo, 0)


def knapsack_rec(values, weights, c, memo, i):
    if c == 0 :
        return 0

    if i >= len(weights):
        return 0

    if  memo[i][c] != -1:
        return memo[i][c]

    if weights[i] > c:
        result = knapsack_rec(values, weights, c, memo, i+1)
    else:
        result = max(knapsack_rec(values, weights, c, memo, i+1),  values[i]+knapsack_rec(values, weights, c - weights[i], memo, i+1))

    memo[i][c] = result

    return result

def knapsack_it(values, weights, capacity):

    n = len(values)
    dp = [[-1] * (capacity + 1) for _ in range(n + 1)]

    dp[0][:] = [0] * len(dp[0])

    for c in range(capacity+1):
        for w in range(n):
            if weights[w] > c:
                dp[w+1][c] = dp[w][c]
            else:
                dp[w+1][c] = max(values[w]+ dp[w][c-weights[w]], dp[w][c])

    return dp[n][capacity]


if __name__ == "__main__":
    fixed_cases = [
        ([10, 40, 30], [5, 4, 6], 10, 70),
        ([60, 100, 120], [10, 20, 30], 50, 220),
        ([10], [5], 10, 10),
        ([10], [11], 10, 0),
        ([], [], 10, 0),
        ([10, 20], [5, 5], 0, 0),
    ]
    for values, weights, capacity, expected in fixed_cases:
        got = knapsack_01(values, weights, capacity)
        assert got == expected, (
            f"{values},{weights},{capacity}: expected {expected}, got {got}"
        )
        got_it = knapsack_it(values, weights, capacity)
        assert got_it == expected, (
            f"{values},{weights},{capacity}: expected {expected}, got {got_it}"
        )
    print("fixed cases passed (both knapsack_01 and knapsack_it)")

    import random
    from itertools import combinations

    def brute_force(values, weights, capacity):
        n = len(values)
        best = 0
        for r in range(n + 1):
            for combo in combinations(range(n), r):
                w = sum(weights[i] for i in combo)
                if w <= capacity:
                    best = max(best, sum(values[i] for i in combo))
        return best

    for _ in range(300):
        n = random.randint(0, 8)
        values = [random.randint(1, 50) for _ in range(n)]
        weights = [random.randint(1, 10) for _ in range(n)]
        capacity = random.randint(0, 30)
        got = knapsack_01(values, weights, capacity)
        want = brute_force(values, weights, capacity)
        assert got == want, f"{values},{weights},{capacity}: expected {want}, got {got}"
        got_it = knapsack_it(values, weights, capacity)
        assert got_it == want, (
            f"{values},{weights},{capacity}: expected {want}, got {got_it}"
        )
    print("300 randomized trials passed (both knapsack_01 and knapsack_it)")
