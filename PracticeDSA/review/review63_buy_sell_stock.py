"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/buy_sell_stock.py until you're done.

Problem (Best Time to Buy and Sell Stock, single transaction):

Given an array of prices where prices[i] is the stock price on
day i, find the maximum profit achievable from a single buy and
a single sell (buy must happen before sell). Return 0 if no
profit is possible.

Example:
  prices = [7, 1, 5, 3, 6, 4]
  output = 5  (buy at 1, sell at 6)

Write your solution below.
"""


def max_profit(prices):
    min_price = float('inf')
    max_gain = 0

    for price in prices:
        if min_price > price:
            min_price = price
        if max_gain < (price -  min_price):
            max_gain = (price-min_price)

    return max_gain


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # expect 5
    print(max_profit([7, 6, 4, 3, 1]))  # expect 0
    print(max_profit([2, 4, 1]))  # expect 2
    print(max_profit([]))  # expect 0

    import random

    def brute_force_profit(prices):
        best = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                best = max(best, prices[j] - prices[i])
        return best

    for trial in range(300):
        n = random.randint(0, 50)
        prices = [random.randint(1, 100) for _ in range(n)]
        got = max_profit(prices)
        expected = brute_force_profit(prices)
        assert got == expected, f"Mismatch on {prices}: got {got}, expected {expected}"

    print("All stress tests passed!")
