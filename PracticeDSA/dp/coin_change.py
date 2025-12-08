
def coin_change(coins, amount):
    """
    Strategy: Top-Down Dynamic Programming (Memoization)
    ----------------------------------------------------
    1. Define State: dp[i] = Min coins to make amount 'i'.
    2. Base Cases:
       - amount == 0 -> 0 coins (Success).
       - amount < 0  -> -1 (Impossible).
    3. Recurrence:
       - Try every coin 'c' in the list.
       - Result = 1 + coin_change(amount - c)
       - Take the minimum of all valid results.
    4. Memoization: Store results in a table of size (amount + 1) to avoid 
       re-calculating the same sub-problems.

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
    return coin_change_recursive(coins, amount, memo)


def coin_change_recursive(coins, amount ,memo):
    if amount == 0:
        return 0
    
    if amount < 0:
        return -1
    
    if memo[amount] != -1:
        return memo[amount]
    
    min_coins = -1

    for coin in coins:
        result = coin_change_recursive(coins, amount - coin, memo)
        if result != -1:
            min_coins = min(min_coins, result + 1) if min_coins != -1 else result + 1
    
    memo[amount] = min_coins
    return memo[amount]