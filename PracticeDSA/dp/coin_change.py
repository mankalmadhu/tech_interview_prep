
def coin_change(coins, amount):
    """
    Calculates the fewest number of coins needed to make up a given amount.

    This function uses a top-down dynamic programming approach with memoization
    to find the optimal solution.

    Args:
        coins: A list of coin denominations available.
        amount: The target amount to make change for.

    Returns:
        The minimum number of coins required, or -1 if the amount
        cannot be made up.

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