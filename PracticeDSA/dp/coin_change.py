def coin_change(coins, amount):
    """
    Strategy: Top-Down Dynamic Programming (Memoization)
    ----------------------------------------------------
    1. Define State: dp[i] = Min coins to make amount 'i'.
    2. Base Cases:
       - amount == 0 -> 0 coins (Success).
       - amount < 0  -> +infinity (Impossible; sentinel so it never wins
         a min() comparison during recursion).
    3. Recurrence:
       - Try every coin 'c' in the list.
       - Result = 1 + coin_change_recursive(amount - c)
       - Take the minimum of all valid results.
    4. Memoization: Store results in a table of size (amount + 1) to avoid
       re-calculating the same sub-problems. -1 marks "not yet computed";
       float('inf') marks a cached, confirmed-impossible subproblem. These
       two meanings must use DIFFERENT sentinel values, otherwise an
       impossible subproblem looks "uncomputed" forever and gets
       re-derived from scratch on every reference to it -- causing
       exponential blowup instead of true O(A*N) memoized time.

    Complexity Analysis:
    --------------------
    Time Complexity: O(A * N)
       - A = Amount, N = Number of coins.
       - We solve 'A' sub-problems. Each sub-problem iterates through 'N' coins.

    Space Complexity: O(A)
       - O(A) for the memoization table.
       - O(A) for the recursion stack (worst case depth).

    Example Trace for `coin_change([1, 2], 3)`:
      - The goal is to solve for amount=3.
      - It explores two choices:
        1. Use a '1' coin: The problem becomes 1 + solve(2).
           - solve(2) explores two choices:
             - Use a '1' coin: 1 + solve(1) -> 1 + (1 + solve(0)) = 2 coins.
             - Use a '2' coin: 1 + solve(0) = 1 coin.
           - The minimum for solve(2) is 1.
        2. Use a '2' coin: The problem becomes 1 + solve(1).
           - solve(1) must use a '1' coin: 1 + solve(0) = 1 coin.
      - The final result is the minimum of all top-level choices: min(1 + solve(2), 1 + solve(1))
        which is min(1 + 1, 1 + 1) = 2. The path is (1 + 2).
    """
    memo = [-1] * (amount + 1)
    coin_change_recursive(coins, amount, memo)
    return memo[amount] if memo[amount] != float("inf") else -1


def coin_change_recursive(coins, amount, memo):
    if amount < 0:
        return float("inf")

    if amount == 0:
        memo[0] = 0
        return 0

    if memo[amount] != -1:
        return memo[amount]

    min_coins = float("inf")

    for coin in coins:
        min_coins = min(min_coins, coin_change_recursive(coins, amount - coin, memo) + 1)

    memo[amount] = min_coins
    return memo[amount]


def coin_change_bottom_up(coins, amount):
    """
    Strategy: Bottom-Up Dynamic Programming (Tabulation)
    -----------------------------------------------------
    Builds dp[0..amount] iteratively instead of recursing downward.
    dp[i] = min coins to make amount i, using +infinity internally
    to represent "impossible" so it never wins a min() comparison;
    converted back to -1 only at the very end.

    The `if coin > i: continue` guard prevents a negative index into
    dp (Python would otherwise silently wrap around to the *end* of
    the array instead of raising an error).

    Time Complexity: O(A * N) | Space Complexity: O(A), no recursion stack.
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin > i:
                continue
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


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
        got_bu = coin_change_bottom_up(coins, amount)
        assert got == expected, f"top-down coins={coins}, amount={amount}: expected {expected}, got {got}"
        assert got_bu == expected, f"bottom-up coins={coins}, amount={amount}: expected {expected}, got {got_bu}"
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
        got_bu = coin_change_bottom_up(coins, amount)
        want = brute_force(coins, amount)
        assert got == want, f"top-down coins={coins}, amount={amount}: expected {want}, got {got}"
        assert got_bu == want, f"bottom-up coins={coins}, amount={amount}: expected {want}, got {got_bu}"
    print("300 randomized trials passed (top-down + bottom-up)")
